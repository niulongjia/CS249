# -*- coding: utf-8 -*-
"""
A December 2015 export of the Crunchbase data is available at https://github.com/notpeter/crunchbase-data
Individual tables can be downloaded directly:
companies.csv: https://github.com/notpeter/crunchbase-data/blob/master/companies.csv?raw=true
investments.csv: https://github.com/notpeter/crunchbase-data/blob/master/investments.csv?raw=true
acquisitions.csv: https://github.com/notpeter/crunchbase-data/blob/master/acquisitions.csv?raw=true
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline  
companies = pd.read_csv("https://github.com/notpeter/crunchbase-data/blob/master/companies.csv?raw=true")
companies.head()
print "len:"+str(len(companies))
companies.funding_total_usd.values . max()  #  This finds the maximum STRING value
companies[ companies.funding_total_usd.values == '9999999' ]
funding_values = pd.Series( companies.funding_total_usd )
print(len(funding_values))
funding_values.max()  #  funding_values still contains only strings
# PROBLEM:  funding_values  contains the string value  '-'  as a null value marker
sum( (funding_values == '-') )  #  it contains a lot of these...
nonnull_values = (funding_values != '-') & (funding_values != '9999999')
nonnull_funding_values = np.array( funding_values[ nonnull_values ], dtype=float )

len(nonnull_funding_values)
max(nonnull_funding_values)  #  This time the max() is of numeric values
plt.rcParams['figure.figsize'] = (10.0,6.0)

plt.hist(np.log10(nonnull_funding_values), bins=100)
_ = plt.title('log10(funding value) for companies in the Crunchbase dataset')
( nonnull_funding_values.min(), nonnull_funding_values.max() )
investments = pd.read_csv("https://github.com/notpeter/crunchbase-data/blob/master/investments.csv?raw=true")
investments.shape
investments.head()
companies_investments = pd.merge(companies, investments, left_on='name', right_on='company_name' )
companies_investments.shape
companies_investments.head(3)