from currentsapi import CurrentsAPI
from dotenv import load_dotenv
from pyspark.sql.functions import udf
from pyspark.sql.types import TimestampType
from pyspark.sql import SparkSession, SQLContext
from pyspark import SparkContext
import os
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
spark = SparkSession.builder.getOrCreate()
df = spark.read.json('../data.json')    # read json data
print(df.take(3))