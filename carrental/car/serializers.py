from rest_framework import serializers
from car.models import contactUs

class contactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = contactUs
        fields = "__all__"
