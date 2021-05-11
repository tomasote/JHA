from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Entry
from .serializers import EntrySerializer
from rest_framework.parsers import JSONParser

@csrf_exempt
def entry_all(request):
    if request.method == 'GET':    
        entries = Entry.objects.all()
        serializers = EntrySerializer(entries, many=True)
        return JsonResponse(serializers.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EntrySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
