# -*- coding: utf-8 -*-

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from sentiment_analysis import tools

@csrf_exempt
def test_api(request):
    data = tools.predict(request.GET.get("sentence"))
    return JsonResponse({"code": 200, "msg": data}, json_dumps_params={'ensure_ascii': False})

@csrf_exempt
def identify(request):
    if request.is_ajax() and request.method == "POST":
        sentence = request.POST.get("sentence")
        data = tools.predict(sentence)
        return JsonResponse({"code": 200, "data": data}, json_dumps_params={'ensure_ascii': False})

def to_index(request):
    return render(request, 'index.html')