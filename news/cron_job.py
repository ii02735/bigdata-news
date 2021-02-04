#!/usr/bin/env python3

import os
from dotenv import load_dotenv
from crontab import CronTab

with CronTab(user=True) as cron:

    # --packages option : download / add specific package before run spark command
    # cron argument for logging

    job = cron.new(command="""cd /home/jovyan/work/processing && 
                              /spark/bin/spark-submit --packages 
                              org.mongodb.spark:mongo-spark-connector_2.12:3.0.1 
                              --master spark://spark-master:7077 ./script.py cron""")
    job.minute.every(15)
    cron.write()

print("Job written !")