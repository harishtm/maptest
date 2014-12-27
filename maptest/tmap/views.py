# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404, render
from django.template import Context, loader, RequestContext
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib.contenttypes.models import ContentType
import json
from models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import csv
from django.http import HttpResponse
import os
from uuid import uuid4
from datetime import *
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.forms.fields import DateField
from django.template.defaultfilters import slugify
from collections import OrderedDict


def myhome(request):
    return render(request,'test.html',locals())



def get_country(taddr):
    country = taddr[-1].strip()
    return country


def get_state_pincode(taddr):

    state ,pincode = '' , ''
    st_list = taddr[-2].split( )
    for i in st_list:
        try:
            if i.isalpha():
                state = state + i
            if i.isdigit():
                pincode = i
        except:
            state , pincode = st_list , ''
            
    return (state,pincode)

#def get_pincode(taddr):
    #pincode = taddr[-2].split( )[1]
    #return pincode


def get_city(taddr):
    city = taddr[-3].strip()
    return city


def capture_address(request):
    #import ipdb;ipdb.set_trace()
    resp = {}
    status , msg = False , ''
    #print "Addresss=============>",request.GET.copy()

    lat = request.GET.get('lat')
    lng = request.GET.get('lng')
    address = request.GET.get('address')

    try:
        taddr = str(address).split(',')
        add_len = len(taddr)
    except:
        add_len = ''

    if add_len:
        try:
            if add_len == 7:
                country = get_country(taddr)
                state,pincode = get_state_pincode(taddr)
                city = get_city(taddr)
                address1 = taddr[0] + "," + taddr[1] + "," + taddr[2] + "," + taddr[3]
            elif add_len == 6:
                country = get_country(taddr)
                state,pincode = get_state_pincode(taddr)
                city = get_city(taddr)
                address1 = taddr[0] + "," + taddr[1] + "," + taddr[2]
            elif add_len == 5:
                country = get_country(taddr)
                state,pincode = get_state_pincode(taddr)
                city = get_city(taddr)
                address1 = taddr[0] + "," + taddr[1]
            elif add_len == 4:
                country = get_country(taddr)
                state,pincode = get_state_pincode(taddr)
                city = get_city(taddr)
                address1 = taddr[0]
            else:
                country = get_country(taddr)
                state,pincode = get_state_pincode(taddr)
                address1 = taddr[0]

            address_obj = Address.objects.create(country = country,\
                                                    state=state,city = city,pincode=pincode,latitiude=lat,\
                                                    longitude=lng,address1=address1)
            status = True
            msg = "Address added successfully"
        except Exception as e:
            msg = e.message
            if add_len == 3 or add_len == 2:
                try:
                    country = get_country(taddr)
                    address1 = taddr[0]
                    address_obj = Address.objects.create(country = country,\
                                                        latitiude=lat,\
                                                        longitude=lng,address1=address1)
                    status = True
                    msg = "Address added successfully"
                except:
                    msg = "Sorry address details could not be added"
            

    else:
        msg = "Sorry address details could not be added"

    resp = {'status': status, 'msg':msg} 
    return HttpResponse(json.dumps(resp), mimetype = "application/json")




def scroll(request):
    address_list = Address.objects.all()
    return render(request,'scroll.html',locals())










