import logging
import logging.handlers
from logging.handlers import WatchedFileHandler
import os
import multiprocessing
command = '/home/django_env/bin/gunicorn'
pythonpath = '/home/ztube'
bind = '192.168.3.101:8000'
workers = multiprocessing.cpu_count() * 2 + 1
loglevel = 'info'
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'
accesslog = "/home/log/gunicorn_access.log"      #访问日志文件
errorlog = "/home/log/gunicorn_error.log"        #错误日志文件