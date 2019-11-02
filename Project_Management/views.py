from django.shortcuts import render
from django.shortcuts import redirect
from Project_Management.models import *
import json
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from dwebsocket.decorators import accept_websocket
from time import sleep
import operator as op
import numpy as np
from scipy.fftpack import fft,ifft

# Create your views here.
def welding_task(request):
	weldingtask = Station.objects.all()
	return render(request, 'Project_Management/welding_task.html', {'tasks': weldingtask})

def create_weldingtask(request):
	X = request.GET['X']
	Y = request.GET['Y']
	Station.objects.create(x_coordinates=X,y_coordinates=Y)
	return HttpResponse(None)

def delete_weldingtask(request):
	ID = request.GET['ID']
	Station.objects.filter(id = ID).delete();
	return HttpResponse(None)

def welding_task_detail(request, ID):
	weldingtask = Station.objects.get(id = ID)
	return render(request, 'Project_Management/welding_task_detail.html', {'weldingtask': weldingtask})

def edit_welding_task(request, ID):
	welding_task = Station.objects.get(id=ID)
	form = WeldingTaskForm2(instance = welding_task)
	if request.method == 'POST':
		form = WeldingTaskForm2(request.POST, instance=welding_task)
		if form.is_valid():
			form.save(commit=True)
			return HttpResponseRedirect('/Project_Management/welding_task_detail/'+ID)
		else:
			print(form.errors)
	return render(request, 'Project_Management/edit_welding_task.html', {'form': form, 'ID':ID })

@accept_websocket
def refresh_current(request, ID):
	past_id = Current.objects.order_by('-id')[0].id

	#print('WebSocket open')
	while True:
		context = {}
		signal = []
		context['current'] = []
		context['FFTx'] = []
		context['FFTy'] = []
		context['pow'] = []
		context['flag'] = 1
		current = Current.objects.order_by('-id')[0].current
		current = current.split('|')
		context['current'] = current

		counter = 0
		for i in range(len(current)-1):
			signal.append(float(current[i]))
			counter = counter + signal[i]
		base = counter/len(signal)

		y = [signal[i]-base for i in range(len(signal))]

		yf = abs(fft(y))
		yf1=abs(fft(y))/len(signal)           #归一化处理
		yf2 = yf1[range(int(len(signal)/2))]  #由于对称性，只取一半区间

		xf = np.arange(len(y))        # 频率
		xf2 = xf[range(int(len(signal)/2))]  #取一半区间

		xf0 = [float(xf2[i]) for i in range(len(xf2))]
		yf0 = [float(yf2[i]) for i in range(len(yf2))]
		#print(yf0)
		#print(len(yf0))
		context['FFTx'] = xf0
		context['FFTy'] = yf0
		pow = 0
		for i in range(len(yf)):
			pow = pow + yf[i]**2
		context['pow'] = pow/len(yf)

		present_id = Current.objects.order_by('-id')[0].id
		if (past_id == present_id):
			context['flag'] = 0
		request.websocket.send(json.dumps(context))
		sleep(0.5)

@accept_websocket
def refresh_voltage(request, ID):
	past_id = Voltage.objects.order_by('-id')[0].id

	#print('WebSocket open')
	while True:
		context = {}
		signal = []
		context['voltage'] = []
		context['FFTx'] = []
		context['FFTy'] = []
		context['pow'] = []
		context['flag'] = 1
		voltage = Voltage.objects.order_by('-id')[0].voltage
		voltage = voltage.split('|')
		context['voltage'] = voltage

		counter = 0
		for i in range(len(voltage)-1):
			signal.append(float(voltage[i]))
			counter = counter + signal[i]
		base = counter/len(signal)

		y = [signal[i]-base for i in range(len(signal))]

		yf = abs(fft(y))
		yf1=abs(fft(y))/len(signal)           #归一化处理
		yf2 = yf1[range(int(len(signal)/2))]  #由于对称性，只取一半区间

		xf = np.arange(len(y))        # 频率
		xf2 = xf[range(int(len(signal)/2))]  #取一半区间

		xf0 = [float(xf2[i]) for i in range(len(xf2))]
		yf0 = [float(yf2[i]) for i in range(len(yf2))]
		#print(yf0)
		#print(len(yf0))
		context['FFTx'] = xf0
		context['FFTy'] = yf0
		pow = 0
		for i in range(len(yf)):
			pow = pow + yf[i]**2
		context['pow'] = pow/len(yf)

		present_id = Voltage.objects.order_by('-id')[0].id
		if (past_id == present_id):
			context['flag'] = 0
		request.websocket.send(json.dumps(context))
		sleep(0.5)


@accept_websocket
def refresh_sound(request, ID):
	past_id = Sound.objects.order_by('-id')[0].id
	
	#print('WebSocket open')
	while True:
		context = {}
		signal = []
		context['sound'] = []
		context['FFTx'] = []
		context['FFTy'] = []
		context['pow'] = []
		context['flag'] = 1
		sound = Sound.objects.order_by('-id')[0].sound
		sound = sound.split('|')
		context['sound'] = sound

		counter = 0
		for i in range(len(sound)-1):
			signal.append(float(sound[i]))
			counter = counter + signal[i]
		base = counter/len(signal)

		y = [signal[i]-base for i in range(len(signal))]

		yf = abs(fft(y))
		yf1=abs(fft(y))/len(signal)           #归一化处理
		yf2 = yf1[range(int(len(signal)/2))]  #由于对称性，只取一半区间

		xf = np.arange(len(y))        # 频率
		xf2 = xf[range(int(len(signal)/2))]  #取一半区间

		xf0 = [float(xf2[i]) for i in range(len(xf2))]
		yf0 = [float(yf2[i]) for i in range(len(yf2))]
		#print(yf0)
		#print(len(yf0))
		context['FFTx'] = xf0
		context['FFTy'] = yf0
		pow = 0
		for i in range(len(yf)):
			pow = pow + yf[i]**2
		context['pow'] = pow/len(yf)

		present_id = Sound.objects.order_by('-id')[0].id
		if (past_id == present_id):
			context['flag'] = 0
		request.websocket.send(json.dumps(context))
		sleep(0.5)

@accept_websocket
def refresh_robot(request, ID):
	while True:
		context = {}
		context['robot'] = []
		robot = Robot.objects.order_by('-id')[0].robot
		robot = robot.replace('CURRENT JOINT POSITION','当前角坐标')
		robot = robot.replace('CURRENT USER FRAME POSITION','当前用户坐标')
		robot = robot.replace('CURRENT WORLD POSITION','当前世界坐标')
		robot = robot.replace('Frame #:  1  Tool #:  5</br>','')
		robot = robot.replace('CFG: N U T, 0, 0, 0</br>','')
		robot = robot.replace('Tool #:  5</br>','')
		context['robot'] = robot
		request.websocket.send(json.dumps(context))
		sleep(0.5)

@accept_websocket
def refresh_monitor(request, ID):
	#i = 0
	while True:
		context = {}
		context['monitorpic'] = []
		context['monitorpic'] = MonitorPic.objects.order_by('-id')[0].monitorpic
		request.websocket.send(json.dumps(context))
		#i = i + 1
		sleep(0.1)

@accept_websocket
def refresh_sound_summary(request, ID):
	past_id = Sound.objects.order_by('-id')[0].id
	
	#print('WebSocket open')
	while True:
		context = {}
		context['sound'] = []
		context['flag'] = 1
		sound = Sound.objects.order_by('-id')[0].sound
		sound = sound.split('|')
		context['sound'] = sound
		present_id = Sound.objects.order_by('-id')[0].id
		if (past_id == present_id):
			context['flag'] = 0
		request.websocket.send(json.dumps(context))
		sleep(0.5)

@accept_websocket
def refresh_voltage_summary(request, ID):
	past_id = Voltage.objects.order_by('-id')[0].id

	#print('WebSocket open')
	while True:
		context = {}
		context['voltage'] = []
		context['flag'] = 1
		voltage = Voltage.objects.order_by('-id')[0].voltage
		voltage = voltage.split('|')
		context['voltage'] = voltage
		present_id = Voltage.objects.order_by('-id')[0].id
		if (past_id == present_id):
			context['flag'] = 0
		request.websocket.send(json.dumps(context))
		sleep(0.5)

@accept_websocket
def refresh_current_summary(request, ID):
	past_id = Current.objects.order_by('-id')[0].id

	#print('WebSocket open')
	while True:
		context = {}
		context['current'] = []
		context['flag'] = 1
		current = Current.objects.order_by('-id')[0].current
		current = current.split('|')
		context['current'] = current
		present_id = Current.objects.order_by('-id')[0].id
		if (past_id == present_id):
			context['flag'] = 0
		request.websocket.send(json.dumps(context))
		sleep(0.5)

@accept_websocket
def refresh_weldpool_summary(request, ID):
	#i = 0
	while True:
		context = {}
		context['weldpoolPic'] = []
		context['weldpoolPic'] = WeldpoolPic.objects.order_by('-id')[0].weldpoolPic
		request.websocket.send(json.dumps(context))
		#i = i + 1
		sleep(0.1)


def sound(request, ID):
	return render(request, 'Project_Management/sound.html')

def current_voltage(request, ID):
	return render(request, 'Project_Management/current_voltage.html')

def weldpool(request, ID):
	return render(request, 'Project_Management/weldpool.html')

def monitor(request, ID):
	return render(request, 'Project_Management/monitor.html')

def intro1(request, ID):
	return render(request, 'Project_Management/intro1.html')

def intro2(request, ID):
	return render(request, 'Project_Management/intro2.html')

def mon(request, ID):
	return render(request, 'Project_Management/mon.html')

def equip(request, ID):
	return render(request, 'Project_Management/equip.html')

def robot(request, ID):
	return render(request, 'Project_Management/robot.html')

def spectrum(request, ID):
	return render(request, 'Project_Management/spectrum.html')