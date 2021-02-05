#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from crontab import CronTab

load_dotenv()

schedule = int(os.getenv("JOB_SCHEDULE"))

if schedule and schedule > 0:

    with CronTab(user=True) as cron:

        # cron argument for logging
        
        job = cron.new(command="cd /home/jovyan/work/processing && /spark/bin/spark-submit --master spark://spark-master:7077 ./script.py cron")
        job.minute.every(schedule)
        cron.write()
    print("Job written !")