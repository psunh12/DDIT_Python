from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import pymysql

def index(request):
    return HttpResponse("Hello, Django")

def param(request):
    menu = request.GET["menu"]
    print("menu",menu)
    return HttpResponse("PARAM:"+menu)

@csrf_exempt
def post(request):
    menu = request.POST["menu"]
    print("menu",menu)
    return HttpResponse("POST:"+menu)

def forw(request):
    a = "홍길동"
    b = ["전우치","이순신","강감찬"]
    c = [
        {'e_id':'1','e_name':'1','gen':'1','addr':'1'},
        {'e_id':'2','e_name':'2','gen':'2','addr':'2'},
        {'e_id':'3','e_name':'3','gen':'3','addr':'3'}
        
    ]
    return render(request, 'forw.html',{'a':a,'b':b,'c':c})

def emp(request):
    conn = pymysql.connect(host='localhost', user='root', password='python',
                           db='python', charset='utf8',port=3305)
    curs = conn.cursor(pymysql.cursors.DictCursor)
    
    sql = "select * from emp"
    curs.execute(sql)
    
    rows = curs.fetchall()
    print(rows) 
       
    curs.close()
    conn.close()
    return render(request, 'emp.html',{'rows':rows})

