# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect, reverse
def index(request):
    #if 'total_charge' not in request.session:
        request.session['total_charge']= 0
        request.session['total_items']= 0
	return render(request, 'amadon_app/index.html')
def process(request):
    print request.POST['item']
    price = {
        "DTS":19.99,
        "DS":29.99,
        "DC":4.99,
        "AB":49.99,
    }
    print int(request.POST['amount'])
    request.session['charge']= int(request.POST['amount'])* price[request.POST["item"]]
    request.session['total_items']= int(request.POST['amount'])+ request.session['total_items']
    request.session['total_charge']= int(request.session['charge'])+ request.session['total_charge']
    return redirect('/receipt')
def receipt(request):
    return render(request, 'amadon_app/receipt.html')


# Create your views here.
