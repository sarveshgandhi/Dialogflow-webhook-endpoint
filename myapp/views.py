# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Person

# Create your views here.
def home(request):
    return HttpResponse('Halelo')

@csrf_exempt
def webhook(request):
    # ----------------------------------
    fhand = open('mysite/myapp/console.txt', 'a+')
    fhand.write('\n>>>request.body = ')
    a = str(request.body, "utf-8")
    fhand.write(a + "\n")
    fhand.write('\n>>>request.headers = ')
    fhand.write(str(request.headers))
    fhand.write('\n>>>request = ')
    fhand.write(str(request))
    fhand.close()
    # ----------------------------------
    req = json.loads(request.body)
    height = req.get('queryResult').get('parameters').get("height")/100 #(meters)
    weight = req.get('queryResult').get('parameters').get("weight") #(kgs)
    bmi = weight/(height**2)
    # ----------------------------------
    q = Person.objects.create(height = height, weight = weight, bmi = bmi)
    q.save()
    # ----------------------------------
    fulfillmentText = {'fulfillmentText': f'Your BMI came out to be {bmi}'}
    return JsonResponse(fulfillmentText, safe=False)
