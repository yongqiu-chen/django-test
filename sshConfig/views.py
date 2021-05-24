from django.shortcuts import render

from .models import ssh_user, ssh_gourp

from django.core import serializers


# Create your views here.

def index(request):
    my_format = {}
    if request.POST:
        if request.POST.get('type') == 'alter_group':
            store = ssh_gourp.objects.get(id=request.POST.get('id'))
            store.group_name = request.POST.get('group_name')
            store.email_name = request.POST.get('email_name')
        elif request.POST.get('type') == 'add_user':
            username = request.POST.get('user_name')
            group_id = request.POST.get('group_id')
            ipaddr = request.POST.get('ipaddr')
            password = request.POST.get('password')
            store = ssh_user(username=username, userpaaword=password, group_id=group_id, ipaddress=ipaddr)
        else:
            gourp_name = request.POST.get('group_name')
            email_name = request.POST.get('email_addr')
            store = ssh_gourp(group_name=gourp_name, email_name=email_name)
        store.save()
    if request.GET.get('type') == 'delete_group':
        store = ssh_gourp.objects.get(id=request.GET.get('id'))
        store.delete()
    elif request.GET.get('type') == 'add_user':
        my_format.update({'type': 'add_user'})
        my_format.update({'group_id': request.GET.get('group_id')})
    elif request.GET.get('type') == 'alter_group':
        my_format.update({'type': 'alter_group'})
        my_format.update({'id': request.GET.get('id'), 'group_name': request.GET.get('group_name'), 'email_name': request.GET.get('email_name')})
    else:
        pass
    getallgourp = serializers.serialize("python", ssh_gourp.objects.all())
    getalluser = serializers.serialize("python", ssh_user.objects.all())
    return render(request, 'sshConfig/index.html', {'datas': getallgourp, 'my_format': my_format, 'userdatas': getalluser})

