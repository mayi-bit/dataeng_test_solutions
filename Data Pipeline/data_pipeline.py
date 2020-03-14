
# coding: utf-8

"""
DESCRIPTION: Processing the file with following functionalities.
- Split the `name` field into `first_name`, and `last_name`
- Remove any zeros prepended to the `price` field
- Delete any rows which do not have a `name`
- Create a new field named `above_100`, which is `true` if the price is strictly greater than 100
DATE CREATED: 12/03/2020
DATE FINISHED:12/03/2020
AUTHOR: Mrunmayi Saoji
VERSION: 1.0.0

"""

import pandas as pd
import numpy as np



# file processing function
def processing_file(path):
	# Reading dataset.csv file from /abc/abc/dataset.csv
    df0 = pd.read_csv(path)
    #removing all the rows with no names
    df1 = df0.dropna(axis=0, subset=['name'])
    # splitting name column to first name and last name
    df1['last_name'] = df1['name'].str.split().str[-1]
    df1['first_name'] = df1['name'].str.split().str[-2]
    # creating a new field named `above_100`, which is `True` if the price is  greater than 100
    df1['above_100'] = np.where(df1['price']>100, 'True', 'False')
    # removing left padding of zeroes from price column
    df1['new_price']= df1['price'].astype(str).str.lstrip("0")
    df1.drop(['name', 'price'], axis=1, inplace=True)
    df1=df1.rename(columns = {'new_price':'price'})
    df1 = df1[['first_name','last_name','price','above_100']]
    #saving output file
    df1.to_csv('/Users/processed_output.csv')



# main function call
if __name__=="__main__": 
    path = '/Users/dataset.csv'
    processing_file(path) 











