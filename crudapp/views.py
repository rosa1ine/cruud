from django.shortcuts import render, get_object_or_404, redirect
from django.db import connection
from .models import User

def home(request):
    tables = connection.introspection.table_names()
    return render(request, 'crudapp/home.html', {'tables': tables})

def user_list(request):
    users = User.objects.all()
    return render(request, 'crudapp/user_list.html', {'users': users})

def user_detail(request, email):
    user = User.objects.get(email=email)
    return render(request, 'crudapp/user_detail.html', {'user': user})

def user_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        salary = request.POST.get('salary')
        cname = request.POST.get('cname')

        User.objects.create(
            name=name, 
            surname=surname, 
            email=email, 
            phone=phone, 
            salary=salary, 
            cname=cname
        )
        return redirect('user_list')

    return render(request, 'crudapp/user_form.html')

def user_update(request, email):
    user = get_object_or_404(User, email=email)

    if request.method == "POST":

        user.name = request.POST.get('name')
        user.surname = request.POST.get('surname')
        user.email = request.POST.get('email')
        user.phone = request.POST.get('phone')
        user.salary = request.POST.get('salary')
        user.cname = request.POST.get('cname')
        user.save()  
        return redirect('user_list')

    return render(request, 'crudapp/user_form.html', {'user': user})

def user_delete(request, email):
    user = get_object_or_404(User, email=email)

    if request.method == "POST":
        user.delete()
        return redirect('user_list')

    return render(request, 'crudapp/user_confirm_delete.html', {'user': user})
