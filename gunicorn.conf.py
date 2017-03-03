from __future__ import unicode_literals
import multiprocessing

bind = "unix:/home/tanker/TANKER/MAIN/gunicorn.sock"
workers = multiprocessing.cpu_count() * 2 + 1
errorlog = "/home/tanker/logs/MAIN_error.log"
loglevel = "error"
proc_name = "MAIN"
