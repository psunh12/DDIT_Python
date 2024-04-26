from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import pymysql
from django.http.response import JsonResponse
import json
from HELLO_MVVM.dao_emp import DaoEmp


@csrf_exempt
def ajax(request):
    # menu = request.POST["menu"]
    # print("menu",menu)
    data = json.loads(request.body)
    print(data['menu'])
    
    return JsonResponse({'result':'success'})


@csrf_exempt
def select_list(request):
    de = DaoEmp()
    list = de.selectList()
    return JsonResponse({'list':list})


@csrf_exempt
def select_one(request):
    data = json.loads(request.body)
    e_id = data['e_id']
    print("e_id",e_id)
    
    de = DaoEmp()
    vo = de.select(e_id)
    return JsonResponse({'vo':vo})


@csrf_exempt
def insert(request):
    data = json.loads(request.body)
    e_id = data['e_id']
    e_name = data['e_name']
    gen = data['gen']
    addr = data['addr']
    
    de = DaoEmp()
    cnt = de.insert(e_id, e_name, gen, addr)
    return JsonResponse({'cnt':cnt})


@csrf_exempt
def update(request):
    data = json.loads(request.body)
    e_id = data['e_id']
    e_name = data['e_name']
    gen = data['gen']
    addr = data['addr']
    
    de = DaoEmp()
    cnt = de.update(e_id, e_name, gen, addr)
    return JsonResponse({'cnt':cnt})



@csrf_exempt
def delete(request):
    data = json.loads(request.body)
    e_id = data['e_id']
    
    de = DaoEmp()
    cnt = de.delete(e_id)
    return JsonResponse({'cnt':cnt})







