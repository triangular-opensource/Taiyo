import secrets
import sys

from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events

from services.functions import send_newsletter

token = secrets.token_urlsafe(20)

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), 'Newsletterdefault') 
    scheduler.add_job(func=send_newsletter, id=f"Newsletter {token}", trigger='interval', minutes=10, name='newsletter', jobstore='Newsletterdefault')
    register_events(scheduler)
    scheduler.start()
    print('Newsletter Started!!!!', file=sys.stdout)
