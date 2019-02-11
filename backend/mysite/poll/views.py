from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse

from poll.models import ExampleModel
from poll.serializers import ExampleModelSerializer
from poll.models import AvocadoModel
from poll.serializers import AvocadoModelSerializer

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_data(request):
	data = ExampleModel.objects.all()
	if request.method == 'GET':
		serializer = ExampleModelSerializer(data, many=True)
		return JsonResponse(serializer.data, safe=False)

def avocado_thanks(request):
	data = AvocadoModel.objects.all()
	if request.method == 'GET':
		serializer = AvocadoModelSerializer(data, many=True)
		return JsonResponse(serializer.data, safe=False)
