import streamlit as st
import os
from dotenv import load_dotenv
from PIL import Image
from pyspark.sql import SparkSession

load_dotenv()
spark = (SparkSession
    .builder
    .appName("myApp2") 
    .config("spark.mongodb.input.uri", os.getenv('MONGO_URL')) 
    .config("spark.mongodb.input.collection", 'data')  
    .config("spark.jars.packages","org.mongodb.spark:mongo-spark-connector_2.12:3.0.1")
    .getOrCreate())
df = spark.read.format("mongo").load()

st.header('Latest news !')
st.text(f" total : {df.count()}")

st.title('Les 10 derniers :')
ten_articles = df.select('title', 'image', 'url').filter(df.image != 'None').take(10)

col = 0
cols = st.beta_columns(2)
for article in ten_articles:
    st.text(f'start {col}')
    cols[col].image(article.image, caption=article.title,  use_column_width=True)
    cols[col].write(f"[En savoir +]({article.url})")
    if col < 1:
        col += 1
    else:
        col = 0
    st.text(f'end{col}')

