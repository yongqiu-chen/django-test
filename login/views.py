from django.shortcuts import render, redirect
from register.models import register

# Create your views here.


def index(request):
    if request.POST:
        name = request.POST.get('j_username')
        password = request.POST.get('j_password')
        j_from = request.POST.get('from')
        if_name = register.objects.filter(name=name)
        if j_from != '/login':
            return render(request, 'login/login.html', {'hint': '非法路径登录'})
        if name == '':
            return render(request, 'login/login.html', {'hint': '输入的用户名为空'})
        if if_name:
            if if_name[0].password == password:
                rep = redirect('/mian/')
                rep.set_cookie('is_login', True, max_age=60*60)
                return rep
            else:
                return render(request, 'login/login.html', {'hint': '密码错误'})
        else:
            return render(request, 'login/login.html', {'hint': '输入的邮箱或用户不存在'})
    else:
        return render(request, 'login/login.html')
