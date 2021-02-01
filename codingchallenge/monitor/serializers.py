from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class Data_TerminalSerializer(serializers.ModelSerializer):

	class Meta:
		model = Data_Terminal
		fields = ['switch_label','t1_status','t2_status','t3_status','t4_status','t5_status','time_stamp']