from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json

def index(request):
    return HttpResponse("designate some characters")

def suggest(request, input_value):
    print(input_value)
    #return HttpResponse("['indian curry']")
    #listed = ["serval", "hoge", "india", "bag"]
    listed = [
        input_value + "77",
        input_value + "78",
        input_value + "79"
    ]
    ret = json.dumps(listed)
    print(ret)
    return HttpResponse(ret)
