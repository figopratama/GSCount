from django.http import HttpResponse
from django.template import loader
from statsmodels.tsa.stattools import adfuller
from .models import Date
from  .resources import DateResource
from django.contrib import messages
from tablib import Dataset
from django.shortcuts import render
import sys



#data = Date.objects.all().values_list('Clicks')

#def adfuller(request):
#	mydata = Date.objects.values_list('Clicks')
#	template = loader.get_template('adfuller.html')
#	context = {
#		'date': mydata,
#	}
#	mydata = Date.objects .all().values()
#	template = loader.get_template('adfuller.html')
#	context = {
#		'date': mydata,
#	}
#	
#	data = [4, 7, 9, 4, 10]
#     
#	stat, p, crit, lags, obs, t = adfuller(data)
#	print('stat=%.f, p=%.f, crit=%.3f' % (stat, p, crit))
#	if p > 0.05:
#		print('Probably not Stationary')
#	else:
#		print('Probably Stationary')
            
#	for count in mydata:
#		
#		result= adfuller(mydata)
#		print('ADF Statistic: %f' % result[0])
#		print('p-value: %f' % result[1]) #Apabila <5% atau <0.05, maka variabel dikatakan stasioner
#		print('Critical Values:')
#		for key, value in result[4].items():
#			print('\t%s: %.3f' % (key, value))
#			sys.setrecursionlimit(mydata)
	
#	return HttpResponse(template.render(context, request))

#def upload(request):

	#if request.method == 'GET':
		#result = adfuller(data, regression='ct', autolag='AIC')
		#print('ADF Statistic: %f' % result[0])
		#print('p-value: %f' % result[1]) #Apabila <5% atau <0.05, maka variabel dikatakan stasioner
		#print('Critical Values:')
		#for key, value in result[4].items():
			#print('\t%s: %.3f' % (key, value)) 

	#return(request, 'home.html')

#def adfuller1(request):
    # Sample data
#    data = [4, 7, 9, 4, 10]

#    try:
        # Run the Augmented Dickey-Fuller test
#        result = adfuller(data)

        # Extracting the results
#        adf_statistic = result[0]
#        p_value = result[1]
#        used_lag = result[2]
#        n_obs = result[3]
#        critical_values = result[4]

#        context = {
#            'adf_statistic': adf_statistic,
#            'p_value': p_value,
#            'used_lag': used_lag,
#            'n_obs': n_obs,
#            'critical_values': critical_values,
#        }

#        return render(request, 'run_adfuller.html', context)

#    except Exception as e:
#        print("Error:", e)
#        context = {
#            'error': str(e)
#        }
#        return render(request, 'run_adfuller.html', context)



