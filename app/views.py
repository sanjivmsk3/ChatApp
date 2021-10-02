from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import UpdateView

from app.forms import RegistrationForm, PostForm
from app.models import PostDetails
import random


# Create your views here.


class UserRegistration(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('user-details')
        else:
            form = RegistrationForm()
            no1 = random.randint(20,50)
            opr = random.choice(['+','-','*'])
            no2 = random.randint(0,20)
            ans = eval(str(no1) + opr + str(no2))
            context = {
                'forms':form,
                'no1':no1,
                'no2':no2,
                'opr':opr,
                'ans':ans
            }
            return render(request, 'signup.html',context)

    def post(self, request,):
        form = RegistrationForm(request.POST or None)
        f_ans = request.POST.get('anss')
        c_ans = request.POST.get('c-ans')
        if f_ans == c_ans:
            if form.is_valid():
                form.save()
                return redirect('login')
            else:
                return redirect('home')
        else:
            return redirect('home')

class Home(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('user-details')
        else:
            return render(request, 'home.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = authenticate(username = username, password = password)
        except:
            #msg
            return redirect('login')
        if user is not None:
            login(request, user)
            return redirect('user-details')
        else:
            #msg
            return redirect('login')

class LogOut(View):
    def get(self, request):
        logout(request)
        #msg
        return redirect('login')



class UserDetails(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'allPost': PostDetails.objects.all().order_by('-id'),
            'forms':PostForm()
        }
        return render(request, 'user-details.html',context)

class Search(LoginRequiredMixin,View):
    def get(self, request):
        sdata = request.GET.get('ssearch')
        cond = Q(title__icontains=sdata) | Q(author__username__icontains=sdata)

        context = {
            'allPost':PostDetails.objects.filter(cond)
        }
        return render(request,'user-details.html',context)

class AddPost(LoginRequiredMixin,View):
    def post(self, request):
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            f = form.save(commit=False)
            f.author = request.user
            f.save()
            #msg
            return redirect('user-details')
        else:
            #msg
            return redirect('user-details')


class UpdatePost(LoginRequiredMixin,UpdateView):
    model = PostDetails
    form_class = PostForm
    template_name = 'update-post.html'

    def form_valid(self, form):
        form.save()
        return redirect('user-details')


class Chat(LoginRequiredMixin,View):
    def get(self, request):
        return render(request, 'chat.html', {})