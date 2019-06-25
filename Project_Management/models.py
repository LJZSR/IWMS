from django.db import models

# Create your models here.

class Station(models.Model):
	x_coordinates = models.FloatField(blank=True,null=True,)
	y_coordinates = models.FloatField(blank=True,null=True,)
	name = models.CharField(max_length=50,blank=True,null=True,help_text="请输入工位名字.",)
	description = models.TextField(blank=True,null=True,help_text="工位描述.",)

class Current(models.Model):
	station = models.ForeignKey(Station,on_delete=models.CASCADE,blank=True,null=True)
	time = models.CharField(max_length=50,blank=True,null=True)
	current = models.TextField(blank=True,null=True,)

class Voltage(models.Model):
	station = models.ForeignKey(Station,on_delete=models.CASCADE,blank=True,null=True)
	time = models.CharField(max_length=50,blank=True,null=True)
	voltage = models.TextField(blank=True,null=True,)

class Sound(models.Model):
	station = models.ForeignKey(Station,on_delete=models.CASCADE,blank=True,null=True)
	time = models.CharField(max_length=50,blank=True,null=True)
	sound = models.TextField(blank=True,null=True,)

class MonitorPic(models.Model):
	station = models.ForeignKey(Station,on_delete=models.CASCADE,blank=True,null=True)
	time = models.CharField(max_length=50,blank=True,null=True)
	monitorpic = models.TextField(blank=True,null=True,)

class WeldpoolPic(models.Model):
	station = models.ForeignKey(Station,on_delete=models.CASCADE,blank=True,null=True)
	time = models.CharField(max_length=50,blank=True,null=True)
	weldpoolPic = models.TextField(blank=True,null=True,)

class Robot(models.Model):
	station = models.ForeignKey(Station,on_delete=models.CASCADE,blank=True,null=True)
	time = models.CharField(max_length=50,blank=True,null=True)
	robot = models.TextField(blank=True,null=True,)
