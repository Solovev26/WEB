from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserData, Message
from .forms import UserDataForm, MsgForm


# Create your views here.

def index(request):
  
    if request.method == 'POST':
        email = request.POST.get('email', False)
        password = request.POST.get('password', False)
        print(email)
        print(password)
        flag = False
        users = UserData.objects.all()
        for user in users:
          if(user.e_mail == email and user.password == password):
            flag = True
            id = user.id
            break

          
        if flag:
            request.session['id'] = id
            return redirect('/user')
            #return redirect('/user', {'email': email, 'password':password})
        else:
            return redirect("/index")
      
    return render(request,'main/index.html')


def info(request):
    return render(request,'main/info.html')


def works(request):
    return render(request,'main/works.html')


def links(request):
    form = MsgForm()
    if request.method == 'POST':
      email = request.POST.get('email', False)
      name = request.POST.get('name', False)
      message = request.POST.get('message', False)
      form=Message()
      form.e_mail = email
      form.f_name = name
      form.msg = message
      form.save()
      return redirect('/links')
    context = {
      'form': form
    }
    return render(request,'main/links.html', context)


def registration(request):
    error = ''
    if request.method == 'POST':
      form = UserDataForm(request.POST)
      if form.is_valid():
        form.save()
        return redirect('/index')
      else:
        error = 'invalid input'
        
  
    form = UserDataForm()
    context = {
      'form': form,
      'error': error
    }
    return render(request,'main/registration.html', context)


def user(request):
    id = request.session['id']
    flag = False
    true_user=[]
    users = UserData.objects.all()
    for user in users:
        if user.id == id:
          true_user = user
          break
    print(true_user.l_name,true_user.f_name)
    return render(request,'main/user.html', {'true_user': true_user})