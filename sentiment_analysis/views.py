# -*- coding: utf-8 -*-

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from sentiment_analysis import tools

@csrf_exempt
def test_api(request):
    print(request.GET.get("sentence"))
    data = tools.predict(request.GET.get("sentence"))
    return JsonResponse({"code": 200, "msg": data}, json_dumps_params={'ensure_ascii': False})