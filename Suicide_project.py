#!/usr/bin/env python
# coding: utf-8

# In[6]:


# mention the directory where the data sets are present

dir_path = "D:\\Drexel MSDS\\DSCI 511 Project\\"
print("The data sets are present in " + dir_path)


# In[8]:


# Importing Suicide data set

import pandas as pd
import numpy as np
import random

# Make sure to use raw string or escape backslashes in the file path
dfSuicide = pd.read_csv(r'Users\prayujateli\Downloads\Suicide Project\Suicide.csv')

dfSuicide.columns = ["Country","Gender","85+ years","75-84 years","65-74 years","55-64 years","45-54 years","35-44 years","25-34 years","15-24 years"]
print(dfSuicide)


# In[ ]:


#processing suicide data set

dfSuicideFiltered = dfSuicide.iloc[2: , :]
dfSuicideFiltered.reset_index(drop=True, inplace=True)
print(dfSuicideFiltered)


# In[ ]:


#pd.options.display.float_format = '{:,.3f}'.format


# In[ ]:


# Importing Population data set

dfPopulation = pd.read_csv(r"C:\Users\Srinivas Pai\Downloads\Data-Project\Population.csv")
print(dfPopulation)


# In[ ]:


#performing pre processing on dataset

dfPopulationFiltered = dfPopulation
#computing the values for population in 2019 using growth rate and population in 2020
dfPopulationFiltered['pop2019'] =  (dfPopulationFiltered.pop2020 - (dfPopulationFiltered.pop2020 **dfPopulationFiltered.GrowthRate/100))
dfPopulationFiltered.drop(["pop2022","pop2021","pop2020","pop2050","pop2030","pop2015","pop2010","pop2000","pop1990","pop1980","pop1970","area","landAreaKm","density","GrowthRate","WorldPercentage","rank"],axis = 1, inplace=True)
dfPopulationFiltered.columns = ["Abbrievation","Country","Population (2019)"]

print(dfPopulationFiltered)


# In[ ]:


# Importing Human Resources Data Set

from pprint import pprint
filename1 = r"C:\Users\Srinivas Pai\Downloads\Data-Project\Human Resourses Data.csv"
dfHumanresoursesdata = pd.read_csv(filename1, header = 0)
percentage = 0

temp=0
k = 0
r=dfHumanresoursesdata.shape[0]
dfHumanresoursesdata['year_diff'] = dfHumanresoursesdata['Year'] 

for i in dfHumanresoursesdata['Country']:
    year=dfHumanresoursesdata['Year']#.astype(int)

    temp=2019-(year[k])
    dfHumanresoursesdata.at[k,'year_diff']=temp
    percentage = random.randint(-3, 9)
    j=0
    if(k==r):
        break
    else:
        k=k+1
        dfHumanresoursesdata['New_Psychiatrist_count_2019']=dfHumanresoursesdata['Psychiatrists working in mental health sector (per 100 000 population)']
        dfHumanresoursesdata['New_Nurses_count_2019']=dfHumanresoursesdata['Nurses working in mental health sector (per 100 000 population)']
        dfHumanresoursesdata['New_Social workers_count_2019']=dfHumanresoursesdata['Social workers working in mental health sector (per 100 000 population)']
        dfHumanresoursesdata['New_Psychologists_count_2019']=dfHumanresoursesdata['Psychologists working in mental health sector (per 100 000 population)']
    
        #we are calculating statistics for 2019 using data from other columns
        #percentage increase is assumed to range between -3 and 9
        #we are including a negative range to take into account that certain countries may show decline in growth
    
        while j!=temp:

            dfHumanresoursesdata['New_Psychiatrist_count_2019']=dfHumanresoursesdata['New_Psychiatrist_count_2019']+(dfHumanresoursesdata['New_Psychiatrist_count_2019']*(percentage/100))
            dfHumanresoursesdata['New_Nurses_count_2019']=dfHumanresoursesdata['New_Nurses_count_2019']+(dfHumanresoursesdata['New_Nurses_count_2019']*(percentage/100))
            dfHumanresoursesdata['New_Social workers_count_2019']=dfHumanresoursesdata['New_Social workers_count_2019']+(dfHumanresoursesdata['New_Social workers_count_2019']*(percentage/100))
            dfHumanresoursesdata['New_Psychologists_count_2019']=dfHumanresoursesdata['New_Psychologists_count_2019']+(dfHumanresoursesdata['New_Psychologists_count_2019']*(percentage/100))
            j=j+1

dfHumanresoursesdata.reset_index(drop=True, inplace=True)
pprint(dfHumanresoursesdata)


# In[ ]:


#dropping columns from Humanresoursesdata data set

dfHumanresoursesdataFiltered = dfHumanresoursesdata.drop(dfHumanresoursesdata.columns[[1,2,3,4,5,6]], axis=1)
print(dfHumanresoursesdataFiltered)


# In[ ]:


# importing Happiness Index Code

import pandas as pd
filename = r"C:\Users\Srinivas Pai\Downloads\Data-Project\Happiness Index.csv"
dfHappinessindex = pd.read_csv(filename, header = 0)

#The happiness2019 is calculated by considering the scoreDifference between the year 2021 and 2020. Here we are assuming that the value difference between 2020 and 2019 follows the same pattern.
dfHappinessindex['happiness2019']=dfHappinessindex['happiness2020']-dfHappinessindex['scoreDifference'] 
dfHappinessindex.reset_index(drop=True, inplace=True)
print(dfHappinessindex)


# In[ ]:


#dropping cols from Happiness index

dfHappinessindexFiltered = dfHappinessindex.drop(dfHappinessindex.columns[[2,3,4]], axis=1)
dfHappinessindexFiltered.columns = ["Happiness Rank","Country","Happiness index"]

print(dfHappinessindexFiltered)


# In[ ]:


# Importing Literacy Rate data set

import pandas as pd

dfLiteracy = pd.read_csv(r"C:\Users\Srinivas Pai\Downloads\Data-Project\Literacy Rate.csv")
dfLiteracy['Year_2019'] = dfLiteracy['dataYear'] 
r=dfLiteracy.shape[0]
k=0
percentage = 0

for i in dfLiteracy['country']:
    year=dfLiteracy['dataYear']#.astype(int)

    percentage = random.randint(-3, 9)
    temp=(2019-(year[k]))
    dfLiteracy.at[k,'Year_2019']=int(dfLiteracy.iloc[k,2] + temp)
    #print(temp)
    j=0
    if(k==r):
        break
    else:
        k=k+1
        dfLiteracy['latestRate_2019']=dfLiteracy['latestRate']
        while j!=temp:

        #we are calculating statistics for 2019 using data from other columns
        #percentage increase is assumed to range between -3 and 9
        #we are including a negative range to take into account that certain countries may show decline in growth
        
            dfLiteracy['latestRate_2019']=dfLiteracy['latestRate_2019']+(dfLiteracy['latestRate_2019']*(percentage/100))
            j=j+1

print(dfLiteracy)


# In[ ]:


#dropping cols and filtering literacy dataset

dfLiteracyFiltered = dfLiteracy
dfLiteracyFiltered = dfLiteracyFiltered.drop(dfLiteracyFiltered.columns[[1,2,3,4]], axis=1)
dfLiteracyFiltered.columns = ["Country","Literacy Rate in 2019"]

print(dfLiteracyFiltered)


# In[ ]:


# Importing Mental Health data set

import pandas as pd
from pprint import pprint

dfMental_Health = pd.read_csv(r"C:\Users\Srinivas Pai\Downloads\Data-Project\Mental Health Governance.csv")
dfMental_Health = dfMental_Health.drop(['Year','Year the law was enacted (latest revision)','Publication year of the policy or plan (latest revision)'], axis=1)
dfMental_Health = dfMental_Health.reset_index(drop=True)
print(dfMental_Health)


# In[ ]:


# Importing Drug_Addiction data set

import pandas as pd

dfDrugAddiction = pd.read_csv(r"C:\Users\Srinivas Pai\Downloads\Data-Project\Drug Addiction.csv", header=0)
dfDrugAddiction=dfDrugAddiction.drop(['Code'], axis=1)

dfDrugAddiction.columns = ["Country","Year","Prevalence - Substance use disorders - Sex: Both - Age: Age-standardized (Percent)"]

print(dfDrugAddiction)


# In[ ]:


#performing pre processing on drug addiction data set

dfDrugAddictionFiltered = dfDrugAddiction
#eliminating all rows which do not belong to 2019
dfDrugAddictionFiltered.drop(dfDrugAddiction[dfDrugAddiction['Year'] != 2019].index, inplace=True)
dfDrugAddictionFiltered.reset_index(inplace=True)

dfDrugAddictionFiltered = dfDrugAddictionFiltered.drop(dfDrugAddictionFiltered.columns[[0]], axis=1)
print(dfDrugAddictionFiltered)


# In[ ]:


#Importing Facilities data set

import pandas as pd
from pprint import pprint

dfFacilitiesData = pd.read_csv(r"C:\Users\Srinivas Pai\Downloads\Data-Project\Facilities Data.csv", header=0)
temp=0
k = 0
r=dfFacilitiesData.shape[0]
dfFacilitiesData['year_diff'] = dfFacilitiesData['Year'] 
percentage = 0
for i in dfFacilitiesData['Country']:
    year=dfFacilitiesData['Year']#.astype(int)
    percentage = random.randint(-3, 9)
    temp=2019-(year[k])
    dfFacilitiesData.at[k,'year_diff']=temp
    j=0
    if(k==r):
        break
    else:
        k=k+1
        dfFacilitiesData['New_MentalHospital_count_2019']=dfFacilitiesData['Mental hospitals (per 100 000 population)']
        dfFacilitiesData['New_MentalHealthUnits_count_2019']=dfFacilitiesData['Mental health units in general hospitals (per 100 000 population)']
        dfFacilitiesData['New_OutpatientFacilities_count_2019']=dfFacilitiesData['Mental health outpatient facilities (per 100 000 population)']
        dfFacilitiesData['New_MentalHealthDayTreatmentFacilities_count_2019']=dfFacilitiesData['Mental health day treatment facilities (per 100 000 population)']
        dfFacilitiesData['New_CommunityResidentialFacilities_count_2019']=dfFacilitiesData['Community residential facilities (per 100 000 population)']
        while j!=temp:

        #we are calculating statistics for 2019 using data from other columns
        #percentage increase is assumed to range between -3 and 9
        #we are including a negative range to take into account that certain countries may show decline in growth
        
            dfFacilitiesData['New_MentalHospital_count_2019']=dfFacilitiesData['New_MentalHospital_count_2019']+(dfFacilitiesData['New_MentalHospital_count_2019']*(percentage/100))
            dfFacilitiesData['New_MentalHealthUnits_count_2019']=dfFacilitiesData['New_MentalHealthUnits_count_2019']+(dfFacilitiesData['New_MentalHealthUnits_count_2019']*(percentage/100))
            dfFacilitiesData['New_OutpatientFacilities_count_2019']=dfFacilitiesData['New_OutpatientFacilities_count_2019']+(dfFacilitiesData['New_OutpatientFacilities_count_2019']*(percentage/100))
            dfFacilitiesData['New_MentalHealthDayTreatmentFacilities_count_2019']=dfFacilitiesData['New_MentalHealthDayTreatmentFacilities_count_2019']+(dfFacilitiesData['New_MentalHealthDayTreatmentFacilities_count_2019']*(percentage/100))
            dfFacilitiesData['New_CommunityResidentialFacilities_count_2019']=dfFacilitiesData['New_CommunityResidentialFacilities_count_2019']+(dfFacilitiesData['New_CommunityResidentialFacilities_count_2019']*(percentage/100))
            j=j+1

dfFacilitiesData.reset_index(drop=True, inplace=True)
print(dfFacilitiesData)


# In[ ]:


#dropping unwanted columns from facilities data set

dfFacilitiesDataFiltered = dfFacilitiesData
dfFacilitiesDataFiltered = dfFacilitiesDataFiltered.drop(dfFacilitiesDataFiltered.columns[[1,2,3,4,5,6,7]], axis=1)
print(dfFacilitiesDataFiltered)


# In[ ]:


#performing web scrapping using beautiful soup

from bs4 import BeautifulSoup
import urllib # We'll still need this to download webpages
from pprint import pprint
import re


html_text = urllib.request.urlopen("https://www.worldometers.info/gdp/gdp-by-country//").read()
soup = BeautifulSoup(html_text, 'html.parser')

country = []

for href_tags in soup.find_all("a",href=True):
    #print(href_tags.text)
    country.append(href_tags.text)

del country[len(country) - 9:]
country = country[7:]

sample_list = []
for td_tags in soup.find_all("td",style=True):
    print(td_tags.text)
    sample_list.append(td_tags.text)
country = sample_list[1::8]

gdp_dollar = sample_list[2::8]

gdp = [re.sub(r'[^a-zA-Z0-9]','',string) for string in gdp_dollar]
gdp=[int(x) for x in gdp]

gdp_growth_perc=sample_list[4::8]
gdp_growth = [re.sub(r'[^a-zA-Z0-9]','',string) for string in gdp_growth_perc]


# In[ ]:


list_name_country = ['country']
dfcountry = pd.DataFrame (country, columns = ['Country'])


list_name_country = ['gdp']
dfgdp = pd.DataFrame (gdp, columns = ['gdp'])

dfGdp = pd.concat([dfcountry, dfgdp], axis="columns")

gdp_growth=[int(x) for x in gdp_growth]

myInt = 100
gdp_growth_float = [x / myInt for x in gdp_growth]
list_name_growth_percetage = ['growth percentage']
dfgrowth_percetage = pd.DataFrame (gdp_growth_float, columns = ['growth percentage'])
dfGdpwithpercent=pd.concat([dfGdp, dfgrowth_percetage], axis="columns")
dfGdpwithpercent['Year']=2017
print(dfGdpwithpercent)


# In[ ]:


import random
from pprint import pprint
percentage = 0
temp=0
k = 0
r=dfHumanresoursesdata.shape[0]
dfGdpwithpercent['year_diff'] = dfGdpwithpercent['Year'] 

for i in dfGdpwithpercent['Country']:
    year=dfGdpwithpercent['Year']#.astype(int)

    temp=2019-(year[k])
    dfGdpwithpercent.at[k,'year_diff']=temp
  
    #dfGdpwithpercent.at[k,'year_diff']=temp
    percentage = random.randint(-3, 9)
    j=0
    if(k==r):
        break
    else:
        k=k+1
        dfGdpwithpercent['gdp_2019']=dfGdpwithpercent['gdp']
        
        while j!=temp:

            dfGdpwithpercent['gdp_2019']=dfGdpwithpercent['gdp_2019']+(dfGdpwithpercent['gdp_2019']*(percentage/100))
            
            j=j+1

dfGdpwithpercent.reset_index(drop=True, inplace=True)
pprint(dfGdpwithpercent.head(15))


# In[ ]:


dfGdpwithpercentFiltered = dfGdpwithpercent
dfGdpwithpercentFiltered = dfGdpwithpercent.drop(dfGdpwithpercent.columns[[1,3,4]], axis=1)
dfGdpwithpercentFiltered.columns = ["Country","GDP Growth Rate (in %)","GDP (2019)"]
print(dfGdpwithpercentFiltered)


# In[ ]:


#converting data sets to csv to draw plots in Tableau

dfPopulation.to_excel("dfPopulation.xlsx")
dfPopulationFiltered.to_excel("dfPopulationFiltered.xlsx")

dfHumanresoursesdata.to_excel("dfHumanresoursesdata.xlsx")
dfHumanresoursesdataFiltered.to_excel("dfHumanresoursesdataFiltered.xlsx")

dfHappinessindex.to_excel("dfHappinessindex.xlsx")
dfHappinessindexFiltered.to_excel("dfHappinessindexFiltered.xlsx")

dfLiteracy.to_excel("dfLiteracy.xlsx")
dfLiteracyFiltered.to_excel("dfLiteracyFiltered.xlsx")

dfDrugAddiction.to_excel("dfDrugAddiction.xlsx")
dfDrugAddictionFiltered.to_excel("dfDrugAddictionFiltered.xlsx")

dfFacilitiesData.to_excel("dfFacilitiesData.xlsx")
dfFacilitiesDataFiltered.to_excel("dfFacilitiesDataFiltered.xlsx")


# In[ ]:


#merging all the pre processed datasets 

merged_df=pd.merge(dfPopulationFiltered,dfHumanresoursesdataFiltered, how = 'outer', on = "Country")
merged_df = pd.merge(merged_df,dfHappinessindexFiltered, how = 'outer', on = "Country")
merged_df = pd.merge(merged_df,dfLiteracyFiltered, how = 'outer', on = "Country")
merged_df = pd.merge(merged_df,dfDrugAddictionFiltered, how = 'outer', on = "Country")
merged_df = pd.merge(merged_df,dfFacilitiesDataFiltered, how = 'outer', on = "Country")
merged_df = pd.merge(merged_df,dfSuicideFiltered, how = 'outer', on = "Country")
merged_df = pd.merge(merged_df,dfMental_Health, how = 'outer', on = "Country")
print(merged_df)


# In[ ]:


#for all the missing values in merged data set, we are populating it with NaN

column_headers  = list(merged_df.columns.values) 

for i in (column_headers):
    merged_df[i].fillna(np.nan, inplace = True)
    
#filling some values values for Year
merged_df['Year'].fillna("2019", inplace = True)
merged_df = merged_df.drop(merged_df.columns[[0]], axis=1)
print(merged_df)


# In[ ]:


#printing stats for null values

merged_df.isnull().sum()


# In[ ]:


# coverting the final data set to csv to draw plots

merged_df.to_excel("Final_merged_dataset.xlsx")
print('DataFrame is written to Excel File successfully.');file_name = 'Final_merged_dataset.xlsx'


# In[ ]:




