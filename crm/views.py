from django.shortcuts import render
from .models import Date
from  .resources import DateResource
import csv,io

from .models import ADFResult

from django.shortcuts import redirect
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse


import numpy as np
import pandas as pd
from numpy.random import randn
from pandas import Series, DataFrame
from scipy import stats
import scipy.stats as scs
import matplotlib.pyplot as plt
#import matplotlib as mpl
#import seaborn as sns
#import pandas_datareader.data as web
import statsmodels.formula.api as smf
import statsmodels.tsa.api as smt
import statsmodels.api as sm
import statsmodels.tsa.stattools as smtools
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.stats.diagnostic import acorr_breusch_godfrey
from statsmodels.tsa.stattools import adfuller
from bs4 import BeautifulSoup
from django.http import JsonResponse
import json



def format_percentage(value, decimal_places=1):
    try:
        return f"{value * 100:.{decimal_places}f}%"
    except (ValueError, TypeError):
        return ''

def evaluate_significance(coef, t_stat):
    if coef > 0 and t_stat > 0:
        return "The variable is significant to the dependent variable."
    else:
        return "The variable is not significant to the dependent variable."

def extract_coef_and_t(html_summary):
    soup = BeautifulSoup(html_summary, 'html.parser')
    table = soup.find_all('table')[1]  # Second table contains the coefficients
    rows = table.find_all('tr')
    results = {}

    for row in rows[1:]:  # Skip the header row
        cols = row.find_all('td')
        variable = cols[0].get_text()
        coef = float(cols[1].get_text())
        t_stat = float(cols[2].get_text())
        results[variable] = {'coef': coef, 't': t_stat}
    
    return results

# Create your views here.
# Views for home.html
def upload_and_count(request):
    context = {}
    if request.method == 'POST':
        date_resource = DateResource()
        dataset = Dataset()
        new_date = request.FILES['myfile']

        if not new_date.name.endswith('csv'):
            messages.info(request,'Please Upload the CSV file only')
            return render(request,'count.html')
        else:
            messages.info(request,'File sucessfully uploaded')

        data_set = new_date.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            created = Date.objects.update_or_create(
                Date=column[0],
                Clicks=column[1],
                Impressions=column[2],
                CTR=column[3],
                Ranking=column[4])
    
    # Count logic here
    # 01 Stationery Test   
    # Prepare data for the template
    date = Date.objects.all()
    
    data = {
        'Clicks': [metric.Clicks for metric in date],
        'Impressions': [metric.Impressions for metric in date],
        'Ranking': [metric.Ranking for metric in date],
        'CTR': [convert_to_float(metric.CTR) for metric in date],
    }

    all_data = pd.DataFrame(data)

    results = []
    conclusions_stationarity = []
    try:
        for column in all_data.columns:
            result = adfuller(all_data[column], regression='ct', autolag='AIC')
            adf_statistic = result[0]
            p_value = result[1]
            critical_values = result[4]

            # Save to database
            adf_result = ADFResult(
                variable_name=column,
                adf_statistic=adf_statistic,
                p_value=p_value,
                critical_value_1=critical_values['1%'],
                critical_value_5=critical_values['5%'],
                critical_value_10=critical_values['10%']
            )
            adf_result.save()


            results.append({
                'variable_name': column,
                'adf_statistic': adf_statistic,
                'p_value': p_value,
                # 'critical_values': critical_values
            })

            if p_value < 0.05:
                conclusions_stationarity.append(f"{column} is stationary")
            else:
                conclusions_stationarity.append(f"{column} is not stationary")

            


        # 02. Lag Optimum Test
        # Append result to list for display (optional)

        all_data['lag1_dclicks'] = all_data['Clicks'].shift(1)
        all_data['lag2_dclicks'] = all_data['lag1_dclicks'].shift(2)
        all_data['lag3_dclicks'] = all_data['lag2_dclicks'].shift(3)
        all_data['lag1_dimpressions'] = all_data['Impressions'].shift(1)
        all_data['lag1_dranking'] = all_data['Ranking'].shift(1)
        all_data['lag1_dctr'] = all_data['CTR'].shift(1)

        # Drop rows with NaN values
        all_data.dropna(inplace=True)

        # Convert DataFrame to dictionary
        lagged_data = all_data.to_dict(orient='records')

        # for item in lagged_data:
        #     item['CTR'] = format_percentage(item['CTR'])
        #     item['lag1_dctr'] = format_percentage(item['lag1_dctr'])



        # 03. Regressions Test (Dep. Variable = Clicks)
        # Prepare target and input variables
        Nondep_var = all_data.drop(['Clicks', 'lag1_dclicks', 'lag2_dclicks', 'lag3_dclicks', 'lag1_dimpressions', 'lag1_dranking', 'lag1_dctr'], axis=1)
        Dep_var = all_data.Clicks

        # Add the constant to input variables
        Nondep_var = sm.add_constant(Nondep_var)

        # OLS Regression
        Clicks_mod = sm.OLS(Dep_var.astype(float), Nondep_var.astype(float))
        Clicks_res = Clicks_mod.fit()

        # Extract summary as HTML
        Clicks_sum = Clicks_res.summary().as_html()

        

        # 03. Regressions Test (Dep. Variable = CTR)
        # Prepare target and input variables
        Nondep_var2 = all_data.drop(['CTR', 'lag1_dclicks', 'lag2_dclicks', 'lag3_dclicks', 'lag1_dimpressions', 'lag1_dranking', 'lag1_dctr'], axis=1)
        Dep_var2 = all_data.CTR

        # Add the constant to input variables
        Nondep_var2 = sm.add_constant(Nondep_var2)

        # OLS Regression
        CTR_mod = sm.OLS(Dep_var2.astype(float), Nondep_var2.astype(float))
        CTR_res = CTR_mod.fit()

        # Extract summary as HTML
        CTR_sum = CTR_res.summary().as_html()

        # Extract variable names, coefficients, and t-statistics for Conclusions Table
        Clicks_conclusions = []
        Clicks_finalconclusions = []
        for idx, param in enumerate(Clicks_res.params.index):
            coef = Clicks_res.params[idx]
            t_stat = Clicks_res.tvalues[idx]
            if coef > 0 and t_stat > 0:
                conclusion = f"{param} has positive value and significancy towards variable Clicks"
                Final_conclusion  = f"{param}, "
            else:
                conclusion = f"{param} has no significancy towards variable Clicks"
                Final_conclusion  = f""
            Clicks_conclusions.append(conclusion)
            Clicks_finalconclusions.append(Final_conclusion)

        CTR_conclusions = []
        CTR_finalconclusions = []
        for idx, param in enumerate(CTR_res.params.index):
            coef = CTR_res.params[idx]
            t_stat = CTR_res.tvalues[idx]
            if coef > 0 and t_stat > 0:
                conclusion = f"{param}  has positive value and significancy towards variable CTR"
                Final_conclusion  = f"{param}, "
            else:
                conclusion = f"{param} has no significancy towards variable CTR"
                Final_conclusion  = f""
            CTR_conclusions.append(conclusion)
            CTR_finalconclusions.append(Final_conclusion)


        # Display the results in a template (optional)
        context = {
            'results': results,
            'conclusions_stationarity': conclusions_stationarity,
            'lagged_data': json.dumps(lagged_data),
            'Clicks_sum': Clicks_sum,
            'Clicks_conclusions': Clicks_conclusions,
            'CTR_sum': CTR_sum,
            'CTR_conclusions': CTR_conclusions,
            'Clicks_finalconclusions': Clicks_finalconclusions,
            'CTR_finalconclusions': CTR_finalconclusions,       
            }

    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        context = {
            'results': results,
            'conclusions_stationarity': conclusions_stationarity,
            'lagged_data': [],
            'Clicks_sum': 'Not enough data for regression analysis',
            'Clicks_conclusions': [],
            'CTR_sum': 'Not enough data for regression analysis',
            'CTR_conclusions': [],
        }



    return render(request, 'count.html', context)

















def delete_data(request):
    if request.method == 'POST':
        Date.objects.all().delete()
        ADFResult.objects.all().delete()
        messages.success(request, 'All data has been deleted.')
    return redirect('upload_and_count')




# Views for count.html
# def count(request):
#     return render(request, 'count.html')

def convert_to_float(ctr_string):
    # Replace comma with dot
    # ctr_string = ctr_string.replace(',', '.')
    # Remove percentage sign
    ctr_string = ctr_string.replace('%', '')
    # Convert to float and divide by 100 to get the decimal value
    ctr_float = float(ctr_string) / 100
    return ctr_float

# Views for alldata.html
def alldata(request):
    # Fetch all objects from Date
    all_data = Date.objects.all()
    
    # Pass the data to the template
    context = {
        'all_data': all_data
    }
    
    return render(request, 'alldata.html', context)

def listview(request):
    data = Date.objects.all()
    return render(request, 'home.html', {'data': data})
