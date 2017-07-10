#!/usr/bin/python
# -*- coding: UTF-8 -*-

from django.shortcuts import render

# Create your views here.
from TestApp.models import BlogsPost
from django.shortcuts import render_to_response
from django.http import HttpResponse

from django import forms

from tools.forms import AddForm

from addUser import addRegister

import json

# Create your views here.
def index(request):
    blog_list = BlogsPost.objects.all()
    return render_to_response('index.html',{'blog_list':blog_list})

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))

def add2(request,a, b):
    c = int(a)+int(b)
    return HttpResponse(str(c))


from django.views.decorators.csrf import csrf_exempt, csrf_protect
@csrf_exempt
def my_view(request):
    
    @csrf_protect
    def protected_path(request):
        do_something()
    
    if some_condition():
        return protected_path(request)
    else:
        do_something_else()


from django.views.decorators.csrf import csrf_exempt, csrf_protect
@csrf_exempt
def home(request):

    @csrf_protect
    def protected_path(request):
        print 'protected_path'
        print request
    
#    if some_condition():
#        print 'some_condition'
#        return protected_path(request)
#    else:
#        print 'do_something_else'
#        do_something_else()

    
    from TestApp.models import Register
    if request.method == 'POST':
        print 'receive post request'
        print request.get_host();
        #      help(request)
        print request.upload_handlers
        # print request.body
        print type(request.body)
        
        temp = json.loads(request.body)
        if isinstance(temp, list):
            print 'type of list'
            if len(temp) > 0:
                index = 0;
                for item in temp:
                    index += 1
                    print "\n************商品%d**********\n"%(index)
                    for key in item:
                        print" %s: %s" % (key ,item[key])
        
                        if key == u'商品id':
                            print "-----> \n"
            
                print '\n************到这没有了**********\n'
#                print t['id']

        return HttpResponse('yes this is post')
        
        form = AddForm(request.POST)
        
        if form.is_valid():
            a = form.cleaned_data['name']
            b = form.cleaned_data['email']
        

            return HttpResponse(str(int(a)+int(b)))
    else :
        form = AddForm()
    string = "test string"
    info_dict = {'site': "test html", 'content': u'各种IT技术教程'}
    #m = Register.objects.create(userId=1,name=name,email=email,password=password,timestamp='2017-01-01 10:10',headImg=imageIcon)
        
        
    articles = Register.objects.order_by("-id").all()[0]

    return render_to_response('home.html',{'imgurl':articles})


def home_add(request):
    if request.method == 'POST':
        
        form = AddForm(request.POST,request.FILES)
        
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            imageIcon = form.cleaned_data['image']
            print name
            print email
            print password
            
            if (name and email and password):
                addRegister(name,email,password,imageIcon)
            
            return HttpResponse("user: "+name+'\n' +'      email:'+email+"    add db successed")

        info_dict = {'site': "test html", 'content': u'各种IT技术教程'}

        m = Register.objects.create(userId=1,name=name,email=email,password=password,timestamp='2017-01-01 10:10',headImg=imageIcon)
            

        articles = Register.objects.order_by("-id").all()[0]


        return render(request,'home.html',{'imageUrl':articles})


def upload_pic(request):
    from TestApp.models import Register
    print 'upload_pic'
    print request.method
    if request.method == 'POST':
        form = AddForm( request.POST, request.FILES )  # 有文件上传要传如两个字段
        print form.is_valid()
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            imageIcon = form.cleaned_data['image']
            
            print name
            print imageIcon
            
            m = Register.objects.create(userId=1,name=name,email=email,password=password,timestamp='2017-01-01 10:10',headImg=imageIcon)

            articles = Register.objects.order_by("-id").all()[0]
            
            str = "test str"
            
            return render(request,'home.html',{"str":str})


            return HttpResponse('image upload success')
    return render(request,'home.html')



def static(request):
    print request.get_raw_uri()
    print "request ----"

#    return render(request,'home.html')




















