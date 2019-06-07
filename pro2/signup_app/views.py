from django.shortcuts import render
from .forms import Signupform_1,Signupmodel_form
# Create your views here.

def signup_view(request):
    form = Signupform_1()
    if request.method=='POST':
        form = Signupform_1(request.POST)
        if form.is_valid():
            print(form.cleaned_data['user_name'])
    return render(request,'form_signup.html',{'myform':form})



def  signup_model_view(request):
    form = Signupmodel_form()
    if request.method=='POST':
        form = Signupmodel_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print(form.cleaned_data['name'])
    return render(request,'form_signup.html',{'myform':form,'text':'heyyyy'})
    
