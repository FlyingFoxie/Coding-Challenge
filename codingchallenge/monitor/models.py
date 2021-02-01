from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from datetime import datetime

class Data_Terminal(models.Model):
	SWITCH = [
		("S1","S1"),
		("S2","S2"),
		("S3","S3"),
	]

	STATUS = [
		(0, "OFF"),
		(1, "ON"),
	]
	switch_label = models.CharField(max_length=10, choices=SWITCH)
	t1_status = models.IntegerField(choices=STATUS)
	t2_status = models.IntegerField(choices=STATUS)
	t3_status = models.IntegerField(choices=STATUS)
	t4_status = models.IntegerField(choices=STATUS)
	t5_status = models.IntegerField(choices=STATUS)
	time_stamp = models.DateTimeField(default=timezone.now)
	email_time_stamp = models.DateTimeField(blank=True, null=True)
	switch_status = models.IntegerField(choices=STATUS)

	@property
	def get_switch_status(self):
		if (self.t1_status == self.t2_status == self.t3_status == self.t4_status == self.t5_status == 0):
			switch_status = 0
		else:
			switch_status = 1
		return switch_status

	def save(self,*args,**kwargs):
		self.switch_status = self.get_switch_status
		if self.switch_status == 0:
			print("Notification")
			send_mail(
				'NOTIFICATION FROM DJANGO MONITOR',
				'Please note that there is a disconnection for {} at time {}.'.format(self.switch_label,self.time_stamp),
				'DJANGO BACKEND',
				['williamcwc89@gmail.com'],
				fail_silently = False,
				)
			self.email_time_stamp = timezone.now()
		super(Data_Terminal, self).save(*args, **kwargs)


	def __str__(self):
		return self.switch_label + "_" + str(self.time_stamp)

class Data_Terminal_BulkUpload(models.Model):
	date_uploaded = models.DateTimeField(auto_now=True)
	csv_file = models.FileField(upload_to='data_terminal/bulkupload/')