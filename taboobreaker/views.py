from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import QuestionModelForm, AnswerForm
from . models import QuestionForm, Answer
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

def index(request):
    return HttpResponse("Hello")

def login_user(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:   
            auth.login(request, user)
            return redirect('swechha')
        else:
            return HttpResponse("NO")
    else:
        return render(request, "taboobreaker/login.html")


@login_required(login_url='login_user')
def answer(request, id):
    ques = QuestionForm.objects.get(id=id)
    form = AnswerForm()

    if request.method=='POST':
        form=AnswerForm(request.POST)
        if form.is_valid():
            ans = form.cleaned_data['ans']
            ob = Answer(ques=ques, ans=ans)
            ob.save()
            ques.answered=True
            ques.save()
            return redirect('blog')
        

    return render(request, "taboobreaker/answer.html", {'ques':ques, 'form':form})
    

        

def blog(request):
    q = Answer.objects.all()
    context = {'q':q}
    return render(request, "taboobreaker/blog.html", context)

def logout_user(request):
    auth.logout(request)
    return redirect('login_user') 

@login_required(login_url='login_user')
def swechha(request):
    return render(request, "taboobreaker/swechha.html", {'ques': QuestionForm.objects.all()})

def ask(request):
    form = QuestionModelForm()
    if request.method == 'POST':
        form = QuestionModelForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.info(request, 'Please fill all the details')
    context = {'form': form}
    return render(request, "taboobreaker/askquestion.html", context)