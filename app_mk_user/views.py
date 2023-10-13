from django.shortcuts import render
from .models import user

def home(request):
    return render(request,'users/index.html')
def users(request):
    new_user = user()
    new_user.nome = request.POST.get('nome')
    new_user.idade = request.POST.get('idade')
    new_user.save()

    users = {
        'users' : user.objects.all()
    }
    return render(request,'users/users.html',users)