import os
import csv
from io import StringIO
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils.timezone import make_aware
from datetime import datetime
import pytz

from .models import *

local_tz = pytz.timezone("Asia/Singapore") 

#bulk upload save
@receiver(post_save, sender=Data_Terminal_BulkUpload)
def create_bulk_data(sender, created, instance, *args, **kwargs):
	if created:
		opened = StringIO(instance.csv_file.read().decode())
		reading = csv.DictReader(opened, delimiter=',')
		data = []
		for row in reading:
			switch_label = row['SW(Switch Lable)']
			t1_status = row['T1(Terminal 1)']
			t2_status = row['T2(Terminal 2)']
			t3_status = row['T3(Terminal 3)']
			t4_status = row['T4(Terminal 4)']
			t5_status = row['T5(Terminal 5)']
			time_stamp = datetime.utcfromtimestamp(int(row['TS(Unix Timestamp)'])).replace(tzinfo=pytz.utc)

			if (t1_status == t2_status == t3_status == t4_status == t5_status == '0'):
				switch_status = 0
			else:
				switch_status = 1

			#check if there's duplicate data
			check = Data_Terminal.objects.filter(switch_label=switch_label,time_stamp=time_stamp).exists()
			if not check:
				data.append(
					Data_Terminal(
						switch_label=switch_label,
						t1_status=t1_status,
						t2_status=t2_status,
						t3_status=t3_status,
						t4_status=t4_status,
						t5_status=t5_status,
						time_stamp=time_stamp,
						switch_status=switch_status,
						)
					)

		Data_Terminal.objects.bulk_create(data)
		instance.csv_file.close()
		instance.delete()

def _delete_file(path):
   """ Deletes file from filesystem. """
   if os.path.isfile(path):
       os.remove(path)

