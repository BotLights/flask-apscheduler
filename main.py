from flask import Flask
import os
import requests, json
from flask_apscheduler import APScheduler

app = Flask(__name__)

scheduler = APScheduler()
scheduler.init_app(app)

@scheduler.task('cron', id='do_job_1', hour=20, minute=0)
def job1():
    print("Job 1")

scheduler.start()

@app.route('/')
def default():
   return "Home"

if __name__ == '__main__':
   port = int(os.environ.get("PORT", 5000))
   app.run(host='0.0.0.0', port=port)
   #app.run()
