from django.shortcuts import render,HttpResponse,redirect
from todolistapp import models
from todolistapp import forms
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate



def registerview(request):
    if request.method == 'POST':
        if request.POST.get('password') == request.POST.get('password1'):
            try:
                User.objects.get(username=request.POST.get('username'))
                return HttpResponse("Already registered")
            except:
                user = User.objects.create_user(username=request.POST.get('username'), 
                                           password=request.POST.get('password'))
                return redirect(loginview)
        else:
            return HttpResponse("Passwords are not same")
    return render(request, 'registration.html')



def loginview(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect(dashboard)
        else:
            return HttpResponse("User not found")
    return render(request, 'login.html')



def dashboard(request):
    # if request.user.is_authenticated():
    data = models.note.objects.all()
    print(data)
    context ={'data': data}
    # else:
    #     return render(request,'login.html')
    return render(request,'dashboard.html',context=context)



def addnote(request):
    
    form = forms.noteform(request.POST)
    if request.method == "POST":
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect(dashboard)
        else:
            print(form.errors)
            print("errorr")
    return render(request,"addnote.html") 



def noteview(request):
    form = forms.noteform(request.POST)
    if request.method == "POST":
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect(dashboard)
        else:
            print(form.errors)
    return render(request,"addnote.html")



def editnote(request,id):
    data = models.note.objects.get(id=id)
    context = {'data':data}
    return render(request,'editform.html',context=context)



def updatenote(request,id):
    data = models.note.objects.get(id=id)
    form = forms.noteform(request.POST,instance=data)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(dashboard)
        else:
            print(form.errors)
            print("errorr")
    return render(request,'editform.html')



def deletenote(request,id):
    data= models.note.objects.get(id=id) 
    data.delete()
    return redirect(dashboard)

