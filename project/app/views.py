from django.shortcuts import render 
from .forms import userform , Profileform

def home(request):
    context={}
    context['user'] = userform
    context['profile'] = Profileform
    return render(request, 'home.html',context)

def userdata(request):
    if request.method=='POST':
        form=userform(request.POST)
        print(form)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            contact=form.cleaned_data['contact']
            address=form.cleaned_data['address']
            print(name)
            print(email)
            print(contact)
            print(address)
            form.save()



