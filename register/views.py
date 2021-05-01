from django.shortcuts import render
from .models import register
# Create your views here.


def index(request):

    if request.POST:
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        mail = request.POST.get('mail')
        name = request.POST.get('name')
        if name == '':
            return render(request, 'register/index.html', {'hint': '输入的用户为空'})
        elif register.objects.filter(name=name):
            return render(request, 'register/index.html', {'hint': '已经存在用户'})
        elif password1 == '':
            return render(request, 'register/index.html', {'hint': '输入的密码为空'})
        elif mail == '':
            return render(request, 'register/index.html', {'hint': '输入邮箱为空'})
        elif password1 != password2:
            return render(request, 'register/index.html', {'hint': '输入的密码前后不一致'})
        else:
            store = register(name=name, password=password1, mail=mail)
            store.save()
            return render(request, 'register/index.html', {'hint': '注册成功'})
    else:
        return render(request, 'register/index.html')
