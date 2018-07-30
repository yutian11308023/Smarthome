# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.shortcuts import render
from django.http import HttpResponse


from . import models
# Create your views here.

def index(request):
	nodedata = models.Nodedata.objects.order_by('-id')[0]
	commands = models.Commands.objects.get(pk=1)
	return render(request, 'myhome/index.html', {'commands': commands, 'nodedata': nodedata})
#	return render(request, 'myhome/index.html', {'commands': commands, 'nodedata': nodedata.toJSON})

def bar1(request):
	nodedatas = models.Nodedata.objects.all()
	listx = []
	listy = []
	datetmp = '0'
	flag = 0
	for nodedata in nodedatas[::-1]:
		date = str(nodedata.time)[0:10]
		if datetmp == date:
			pass
		else:
			datetmp = date
			flag = flag + 1
			if flag == 8:
				break
			else:
				listx.append(str(date))
				listy.append(float(nodedata.temperature))
	listx = listx[::-1]
	listy = listy[::-1]
	return render(request, 'myhome/bar1.html', {'nodedatas':nodedatas, 'X':listx, 'Y':listy})

def bar2(request):
	nodedatas = models.Nodedata.objects.all()
	listx = []
	listy = []
	datetmp = '0'
	flag = 0
	for nodedata in nodedatas[::-1]:
		date = str(nodedata.time)[0:10]
		if datetmp == date:
			pass
		else:
			datetmp = date
			flag = flag + 1
			if flag == 8:
				break
			else:
				listx.append(str(date))
				listy.append(float(nodedata.humidity))
	listx = listx[::-1]
	listy = listy[::-1]
	return render(request, 'myhome/bar2.html', {'nodedatas':nodedatas, 'X':listx, 'Y':listy})

def bar3(request):
	nodedatas = models.Nodedata.objects.all()
	listx = []
	listy = []
	datetmp = '0'
	flag = 0
	for nodedata in nodedatas[::-1]:
		date = str(nodedata.time)[0:10]
		if datetmp == date:
			pass
		else:
			datetmp = date
			flag = flag + 1
			if flag == 8:
				break
			else:
				listx.append(str(date))
				listy.append(float(nodedata.light))
	listx = listx[::-1]
	listy = listy[::-1]
	return render(request, 'myhome/bar3.html', {'nodedatas':nodedatas, 'X':listx, 'Y':listy})

def bar4(request):
	nodedatas = models.Nodedata.objects.all()
	listx = []
	listy = []
	datetmp = '0'
	flag = 0
	for nodedata in nodedatas[::-1]:
		date = str(nodedata.time)[0:10]
		if datetmp == date:
			pass
		else:
			datetmp = date
			flag = flag + 1
			if flag == 8:
				break
			else:
				listx.append(str(date))
				listy.append(float(nodedata.co2_simulation))
	listx = listx[::-1]
	listy = listy[::-1]
	return render(request, 'myhome/bar4.html', {'nodedatas':nodedatas, 'X':listx, 'Y':listy})

def bar5(request):
	nodedatas = models.Nodedata.objects.all()
	listx = []
	listy = []
	datetmp = '0'
	flag = 0
	for nodedata in nodedatas[::-1]:
		date = str(nodedata.time)[0:10]
		if datetmp == date:
			pass
		else:
			datetmp = date
			flag = flag + 1
			if flag == 8:
				break
			else:
				listx.append(str(date))
				listy.append(float(nodedata.noise))
	listx = listx[::-1]
	listy = listy[::-1]
	return render(request, 'myhome/bar5.html', {'nodedatas':nodedatas, 'X':listx, 'Y':listy})
