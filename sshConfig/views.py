from django.shortcuts import render

from .models import ssh_user, ssh_gourp

from django.core import serializers


# Create your views here.

def index(request):
    if request.POST:
        gourp_name = request.POST.get('group_name')
        email_name = request.POST.get('email_addr')
        store = ssh_gourp(group_name=gourp_name, email_name=email_name)
        store.save()
    getallgourp = serializers.serialize("python", ssh_gourp.objects.all())
    return render(request, 'sshConfig/index.html', {'datas': getallgourp})

