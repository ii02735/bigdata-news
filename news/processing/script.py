#!/usr/bin/env python3

from currentsapi import CurrentsAPI
from dotenv import load_dotenv
from pyspark.sql import SparkSession
from pymongo import MongoClient
from sys import argv # read input arguments (if script is called by CRON for example)
from datetime import datetime
import udf_functions as udf
import os
import re
import json

load_dotenv()

# API CONNECTION
api = CurrentsAPI(api_key=os.getenv('API_KEY'))
news = api.latest_news()    # get all data
# print(api.search(keywords='Trump'))

#write json file
with open('../data.json','w') as file_resource:
    json.dump(news['news'],file_resource)


#SPARK CONNECTION
spark = (
    SparkSession
    .builder
    .appName("news_data_app") \
    .config("spark.mongodb.input.uri", os.getenv('MONGO_URL')) 
    .config("spark.mongodb.output.uri", os.getenv('MONGO_URL')) 
    .config("spark.mongodb.output.collection", 'data') 
    .getOrCreate()
)

df = spark.read.json('../data.json')    # read json data
df = df.withColumn("published", udf.transform_timestamp_in_date("published"))
df = df.withColumn("origin", udf.url_to_origin("url"))
df = df.withColumn("description", udf.delete_unicode_char("description"))

df.write.format("mongo").mode("append").save()

# write log after execution

mongo_client = MongoClient(os.getenv('MONGO_URL'))
db = mongo_client.news
logs = db.logs
log_record = { 'execution_time': datetime.utcnow() }

if len(argv) > 1 and argv[1] == 'cron':
    log_record['cron'] = True
else:
    log_record['cron'] = False

logs.insert_one(log_record)
