"""
Celery configuration and tasks
"""

import os
from celery import Celery

app = Celery('eve-app')
app.conf.update(
    BROKER_URL=os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost//'),
    BROKER_POOL_LIMIT=1
)


FEEDS = {
    'daily': 'https://itsc.autotrader.com:3000/scorecard/daily',
    'daily_composite': 'https://itsc.autotrader.com:3000/scorecard/daily_composite',
    'daily_notes': 'https://itsc.autotrader.com:3000/scorecard/daily_notes',
}

@app.task
def add(a, b):
    return(a + b)
