from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testapp.forms import signupform
from django.http import HttpResponseRedirect


# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')
@login_required
def java_exam_view(request):
    return render(request,'testapp/javaexam.html')
def logout_view(request):
    return render(request,"testapp/logout.html")
def signupview(request):
    form=signupform()
    if request.method=='POST':
        form=signupform(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')


    return render(request,'testapp/signup.html', {'form1':form})