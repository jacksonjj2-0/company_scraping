import csv 
import pymongo
from pymongo import MongoClient
import pandas as pd

# Connect to MongoDB
connect = pymongo.MongoClient(host='localhost', port= 27017)
database = connect['Company_Scraping']
collection = database['job']

# Read the CSV file using pandas
data = pd.read_csv('company_scraping.csv')

# Convert the data to a list of dictionaries (each row as a dictionary)
records = data.to_dict(orient='records')

# Insert the data into MongoDB
collection.insert_many(records)


