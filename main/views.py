from django.shortcuts import render,redirect


def mian(request):
    status = request.COOKIES.get('is_login')
    if status:
        return render(request, 'mian/index.html')
    else:
        return redirect('/login/')


def init(request):
    return redirect('/login/')


def logout(request):
    rep = redirect('/login/')
    rep.delete_cookie('is_login')
    return rep
