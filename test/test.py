import numpy as np
import pandas as pd
from numpy.random import randn
from pandas import Series, DataFrame
from scipy import stats
#import matplotlib as mpl
import matplotlib.pyplot as plt
#import seaborn as sns
#import pandas_datareader.data as web
import statsmodels.formula.api as smf
import statsmodels.tsa.api as smt
import statsmodels.api as sm
import statsmodels.tsa.stattools as smtools
import scipy.stats as scs
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.stats.diagnostic import acorr_breusch_godfrey
from statsmodels.tsa.stattools import adfuller



df = pd.read_csv('test/dates.csv')
print(df.head())



for i in ['Clicks', 'Impressions', 'Position']:
    result = adfuller(df[i], regression='ct', autolag='AIC')
    print('ADF Statistic: %f' % result[0])
    print('p-value: %f' % result[1]) #Apabila <5% atau <0.05, maka variabel dikatakan stasioner
    print('Critical Values:')
    for key, value in result[4].items():
    	print('\t%s: %.3f' % (key, value))



df['Clicks'].plot() 
plt.show()
df['Impressions'].plot() 
plt.show()
df['Position'].plot() 
plt.show()



#creating lagged variables
df['lag1_dclicks'] = df['Clicks'].shift(1)
df['lag1_dimpressions'] = df['Impressions'].shift(1)
df['lag1_dposition'] = df['Position'].shift(1)
df.dropna(inplace=True)
print(df)
df['Clicks'] = pd.DataFrame(np.arange(5))
df['lag1_dclicks'] = df['Clicks'].shift(1)
print(df)



# Prepare target and input variables. 
X_multi=df.drop(['Clicks','Impressions', 'Position', 'CTR', 'Date'], axis=1)
Y_target=df.Clicks

# Add the costant to our input variables
X_multi=sm.tools.tools.add_constant(X_multi, prepend=True, has_constant='skip')
#print(X_multi)
#print(Y_target)

# OLS Regression
mod = sm.OLS(Y_target.astype(float), X_multi.astype(float))
res = mod.fit()
res = np.asarray(Y_target, X_multi)
print(res.summary())



residuals = DataFrame(res.resid)
residuals.plot()
plt.show()
print(residuals.describe())
plot_acf(residuals,lags=5)
plt.show()