from rest_framework import serializers
from .models import userDetails

class UserDetailsSeri(serializers.ModelSerializer):
    class Meta:
        model = userDetails
        fields = ['id','name','email','roll_no']
