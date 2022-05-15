# -*- coding: utf-8 -*-
"""
Created on Sat May 14 23:36:21 2022

@author: Night
"""

import pandas as  pd

df = pd.read_csv('glassdoor_jobs.csv')








# salary parsing
df["Hourly"] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df["Employer Provided"] = df['Salary Estimate'].apply(lambda x: 1 if 'Empoyeer Provided Salary:' in x.lower() else 0)

#salary
df =  df[df['Salary Estimate'] != "-1"]
salary =  df['Salary Estimate'].apply(lambda x: x.split('(') [0])
salary = salary.apply(lambda x: x.replace('K','').replace('$',''))

min_hr = salary.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary + df.max_salary)/2


# company name
df['company_details'] =  df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis = 1)

#states
df['States of jobs'] = df['Location'].apply(lambda x: x.split(',') [1])

#to count how many jobs in each state 
print(df['States of jobs'].value_counts())


df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)


# company age
df['age'] = df.Founded.apply(lambda x: x if x < 1 else 2022 - x)


# job desc parse
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
 
#r studio 
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
df.R_yn.value_counts()

#spark 
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark.value_counts()

#aws 
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws.value_counts()

#excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel.value_counts()

#machine learning
df['ML'] = df['Job Description'].apply(lambda x: 1 if 'machine learning' in x.lower() else 0)
df.ML.value_counts()


#statistics
df['Stats'] = df['Job Description'].apply(lambda x: 1 if 'statistics' in x.lower() else 0)
df.Stats.value_counts()

df= df.drop(['Unnamed: 0'], axis =1)

#send to csv
df.to_csv('salary_data_cleaned.csv',index = False)