from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from HELLO_MVC.dao_emp import DaoEmp

def emp_list(request):
    de = DaoEmp()
    list = de.selectList()
    return render(request, 'emp_list.html',{'list':list})


def emp_detail(request):
    de = DaoEmp()
    e_id = request.GET["e_id"]
    vo = de.select(e_id)
    return render(request, 'emp_detail.html',{'vo':vo})


def emp_mod(request):
    de = DaoEmp()
    e_id = request.GET["e_id"]
    vo = de.select(e_id)
    return render(request, 'emp_mod.html',{'vo':vo})


def emp_mod_act(request):
    de = DaoEmp()
    e_id = request.POST["e_id"]
    e_name = request.POST["e_name"]
    gen = request.POST["gen"]
    addr = request.POST["addr"]
    cnt = de.update(e_id, e_name, gen, addr)
    return render(request, 'emp_mod_act.html',{'cnt':cnt})

def emp_add_act(request):
    de = DaoEmp()
    e_id = request.POST["e_id"]
    e_name = request.POST["e_name"]
    gen = request.POST["gen"]
    addr = request.POST["addr"]
    cnt = de.insert(e_id, e_name, gen, addr)
    return render(request, 'emp_add_act.html',{'cnt':cnt})



def emp_add(request):
    return render(request, 'emp_add.html')


def emp_del_act(request):
    de = DaoEmp()
    e_id = request.POST["e_id"]
    cnt = de.delete(e_id)
    return render(request, 'emp_del_act.html',{'cnt':cnt})




