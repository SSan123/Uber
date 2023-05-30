from rest_framework import serializers
from users.models import *


class StudentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

class OrdersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'


class StudentsAddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentsAddress
        fields = '__all__'


class StudentsDetailAddressSerializers(serializers.ModelSerializer):
    student_address = StudentsAddressSerializers(many=True)
    class Meta :
        model = Students
        fields = ('first_name','last_name','date_of_birth','student_address')