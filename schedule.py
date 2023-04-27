# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 20:32:58 2023

@author: Mahmoud Saeed
"""

from apscheduler.schedulers.blocking import BlockingScheduler

from main import pipeline


sched = BlockingScheduler()


@sched.scheduled_job('interval', days=7)
def sched_job():
    pipeline()
 
    
sched.start()    
