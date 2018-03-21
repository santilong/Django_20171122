from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse
from django.shortcuts import redirect

def login(request):
    print(request.method)
    print(request.POST)
    print(request.POST.get('user'))
    print(request.POST.get('pwd'))
    error_msg = ''
    if request.method == 'POST':
        u = request.POST.get('user',None)
        p = request.POST.get('pwd', None)
        if u == 'root' and p == '123':
            return redirect('/home')
        else:
            error_msg = '用户名或密码错误'
    return render(request, "login.html", {'error_msg':error_msg})
    # return HttpResponse('OK')

USER_LIST = []
for index in range(5,11):
    user_dict = {'user': 'santi' + str(index),'gender':'Male','email':'santi@16' + str(index) + '.com'}
    USER_LIST.append(user_dict)

def home(request):

    if request.method == 'POST':
        print(request.method)
        user = request.POST.get('user')
        gender= request.POST.get('gender')
        email = request.POST.get('email')
        new_dict = {'user':user,'gender':gender,'email':email}
        USER_LIST.append(new_dict)
    return render(request,'home.html',{'user_list': USER_LIST})