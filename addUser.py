#!/usr/bin/python
# -*- coding: UTF-8 -*-

from TestApp.models import Register

from tools.register import RegisteUser, XyEncode
import random




#for i in range(0,10,1):
#    
#    radstr= random.randint(999, 10000)
#    str2 = random.randint(999, 10000)
#    str3 = random.randint(999, 10000)
#
#    r = RegisteUser('user'+str(radstr),'1091976750@qq.com',str(radstr)+str(str2)+str(str3),'')
#    
#    Register.objects.create(userId=r.id,name=r.name,email=r.email,password=r.password,timestamp=r.timestamp)

def addRegister(user,email,password,headImg):
    
    if queryRegister(user,email):
        r = RegisteUser(user,email,password,'',headImg)
        return Register.objects.create(userId=r.id,name=r.name,email=r.email,password=r.password,timestamp=r.timestamp,headImg = r.headImg)

def queryRegister(user,email):
    import types
    if len(user):
        r = Register.objects.filter(name=user)
        print r
        if r.count():
            print "has same name"
            return False

    if len(email):
        r = Register.objects.filter(email= email)
        if r.count():
            print "has same email"
            return False
    return True

if __name__ == '__main__':
    import os
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
