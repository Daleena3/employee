from rest_framework import serializers
from  api.models import Employes


class EmployeSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)

    class Meta:
        model=Employes
        fields="__all__"
         