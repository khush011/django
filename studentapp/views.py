from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Loginpy
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages


def home_view(request):
    return render(request ,'student/home.html')

def about_view(request):
    return render(request ,'student/about.html',{'color1':'red','color2':'cyan','color3':'yellow'})

def login(request):
    if request.method == "POST":
        u = request.POST['username']
        f = request.POST['first_name']
        l = request.POST['last_name']
        e = request.POST['email']
        p = request.POST['pwd']
        p1 = request.POST['pwd1']
        if p == p1:
            user = User.objects.create_user(
                username = username,
                first_name = first_name,
                last_name = last_name,
                password = password,
                email = email
            )
            user.save()
            return render(request, student/studorm)
        else:
            messages.info(request, 'password doesnt match')
            return redirect('../login')

    # if request.method == 'POST':
    #     s = request.POST['hobbies']

    #     w = request.POST['name']
    #     e = request.POST['eid']
    #     r = request.POST['gender']
    #     t = request.POST['mob']
    #     y = request.POST['eng']
    #     return render(request ,'student/login.html',{'i':s,'j':w,'k':e,'l':r,'m':t,'n':y})
    else:
        return render(request ,'student/login.html')

def simple(request):
    return render(request ,'base2.html')

def info(request):
    s = request.GET["id"]
    w = request.GET["pass"]
    if(s=='qwer' and w=='1234'):
        p = "login successfull"
        return render(request ,'student/result.html',{'d': p} )
    else:
        return render(request ,'student/result.html',{'d': 'login failed'} )
    return render(request ,'student/result.html')
 


def loginpy(request):
    if request.method == 'POST':
        form = Loginpy(request.POST)
        if form.is_valid():
            n = form.cleaned_data['n']
            p = form.cleaned_data['p']
            t = form.cleaned_data['t']
            e = form.cleaned_data['e']
            d = form.cleaned_data['dob']
            g = form.cleaned_data['g']
            c = form.cleaned_data['c']
            s = form.cleaned_data['m']
            return render(request, 'student/outpy.html', {'n':n, 't':t, 
                                                        't':t, 'e':e,
                                                        'd':d, 'g':g,
                                                        'c' :c, 's':s,'p':p})   
    else:
        form = Loginpy()
        return render(request, 'student/loginpy.html', {'form': form})

def studorm(request):
    qs = Stud_Sub.objects.all()
    if request.method == 'POST':
        sub = request.POST['orm_sub']
        obj = Stud_Data.objects.filter(subject__subject = sub)
        return render(request, 'student/orm.html', {'obj':obj, 'qs_sub':qs, 'sub':sub })
    
    else:
        return render(request, 'student/orm.html', {'qs_sub':qs})



def add_Data(request):
    obj_sub = Stud_Sub.objects.all()
    obj_teacher = Teacher.objects.all()
    if request.method=="POST":
        getsub = request.POST['sub']
        getteach = request.POST['teach']
        objs = Stud_Data()
        objs.name = request.POST['name']
        objs.roll_number = request.POST['roll_number']
        objs.subject = Stud_Sub.objects.get(subject= getsub)
        objs.teacher = Teacher.objects.get(name = getteach)
        objs.save()
        m='you record was added successfully'
        # for i in teacher:
        #     print(i)
        
        return render(request, "student/add_studdata.html",{ 'obj_sub':obj_sub,'obj_teacher':obj_teacher, 'm':m})
    return render(request, "student/add_studdata.html",{ 'obj_sub':obj_sub,'obj_teacher':obj_teacher})



def more(request):
    id = request.GET.get('id')
    obj = Stud_Data.objects.get(id = id)
    print(obj.name)
    return render(request, "student/more.html",{'obj':obj})

def delete(request):
    id = request.GET.get('id')
    sub = request.GET.get('sub')
    obd = Stud_Data.objects.get(id = id)         #objet to be deleted
    obd.delete()
    return redirect('../studorm')

def update(request):
    pass
    
 
def jobs(request):
    job_name = Job_Details.objects.all()    
    job_list = list(set([x.name for x in job_name ]))
    loc_list = list(set([x.location for x in job_name ]))
    
    if request.method == "POST":
        loc = request.POST['job_loc']
        title = request.POST['job_name']
        
        pref = Job_Details.objects.filter(name = title,location = loc)
        return render(request, 'student/jobs.html', {'job_list':job_list, 'loc_list':loc_list, 
                                                        'pref':pref})

    else:
        return render(request, 'student/jobs.html', {'job_list':job_list, 'loc_list':loc_list})