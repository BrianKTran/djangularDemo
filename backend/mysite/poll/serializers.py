from rest_framework import serializers
from poll.models import ExampleModel
from poll.models import AvocadoModel
class ExampleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleModel
        fields = ('firstname', 'lastname')
class AvocadoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvocadoModel
        fields = ('avocadoType', 'avocadoPrice')
