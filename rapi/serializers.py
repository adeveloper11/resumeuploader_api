from rest_framework import serializers
from .models import Profile

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'name', 'email', 'dob', 'state', 'gender','location', 'pimage', 'rdoc']