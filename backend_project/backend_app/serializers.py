from rest_framework import serializers
from .models import basic_info

class basic_info_serializer(serializers.ModelSerializer):
        class Meta:
                model = basic_info
                fields = ['name', 'endpoint_url', 'github_url']