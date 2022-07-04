from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from forum.models import Article, Category
# Created decorators to restrict access
from .decorators import unauthenticated_user
from django.utils.decorators import method_decorator

# Create your views here.


@method_decorator(unauthenticated_user, name='dispatch')
class Home(View):
    template_name = 'forum/MainPage_ClickMe.html'

    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request):
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            signed_in_user = authenticate(
                request, username=username, password=password)
            if signed_in_user is not None:
                login(request, signed_in_user)
                return redirect('description')
            else:
                messages.error(request, 'Username or Password incorrect')

        return render(request, self.template_name, {})


class SignUp(View):
    template_name = 'forum/create.html'

    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request):
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            name = request.POST.get('name')

            # print(username, password, email)
            try:
                user = User.objects.create(
                    username=username,
                    email=email,
                    first_name=name
                )
                user.set_password(password)
                user.save()

                login(request, user)
                return redirect('description')
            except Exception as e:
                print(e)
                messages.error(request, "Username already in use")

        return render(request, self.template_name, {})


@method_decorator(unauthenticated_user, name='dispatch')
class RecoverPassword(View):
    template_name = 'forum/reset.html'

    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request):
        if request.method == "POST":
            email = request.POST.get('email')
        messages.success(
            request, f"Reset Email sent to {email}")  # Not working
        return render(request, self.template_name, {})


class Description(View):
    template_name = 'forum/Description.html'

    def get(self, request):
        return render(request, self.template_name, {})


class Forum(View):
    template_name = 'forum/Forum.html'

    def get(self, request, category):
        context = {}
        context["category"] = category.title()

        try:
            category_id = Category.objects.get(name=category).id
        except:
            category_id = 1

        latest_article = Article.objects.filter(category=category_id)
        if latest_article:
            latest_article = latest_article[0]
        context["latest_article"] = latest_article

        return render(request, self.template_name, context)


class Content(View):
    template_name = 'forum/content.html'  # Not available

    def get(self, request):
        return render(request, self.template_name, {})


def Logout(request):
    logout(request)
    return redirect('Home')
