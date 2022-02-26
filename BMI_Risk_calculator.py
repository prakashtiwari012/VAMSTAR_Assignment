import pandas as pd
import numpy as np
import json
from datetime import datetime

def calculate_BMI_RISK(df,df_BMI_category):
    df['Heightmeter']=df.HeightCm/100
    df['BMI']=df.WeightKg/(df.Heightmeter*df.Heightmeter)
    df['BMI']=df.BMI.round(decimals=1)
    x=df.merge(df_BMI_category, how='cross')
    x=x[(x.BMI>=x.bmi_lower) & (x.BMI<=x.bmi_upper)]
    return x[['Gender','HeightCm','WeightKg','BMI','bmi_category','health_risk']]

# This could read data in millions
df= pd.read_json('data/data.json')
df_BMI_category=pd.read_csv('config/BMI_category.csv')
datetime_now= datetime.now()
file_name='output/final_results_'+ str(datetime_now)[0:10]+'.csv'
calculate_BMI_RISK(df,df_BMI_category).to_csv(file_name,index=False)
print("Final output file can be found in output/final_results_xxxx-xx-xx.csv")