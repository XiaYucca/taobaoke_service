#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TestProject.settings")
    from time import ctime,sleep
#    import threading
#
#    def music(func):
#        while True:
#            for i in range(2):
#                print "I was listening to music. %s --%s" %(ctime(),func)
#                sleep(1)
#
#
#    def logData(data):
#        print data
#
##    threading.Thread(target=music,args=('testMuseic',)).start()
#    from tools.tcps import *
#    #    startServer()
#    
#    addSocketListen(logData)
#    threading.Thread(target=startServer).start()
#
#    sleep(2)


    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    
    execute_from_command_line(sys.argv)

