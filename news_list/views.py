from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from .forms import RegistrationForm
from .models import News, NewsCategory


def homepage(request):
    news = News.objects.all()
    categories = NewsCategory.objects.all()
    context = {'news': news, 'categories': categories}

    return render(request, 'index.html', context)


def news_page(request, pk):
    news = News.objects.get(id=pk)
    context = {'news': news}

    return render(request, 'news-single-page.html', context)


def category_page(request, pk):
    category = NewsCategory.objects.get(id=pk)
    news = News.objects.filter(category=category)
    context = {'category': category, 'news': news}

    return render(request, 'category.html', context)


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {'form': RegistrationForm}
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegistrationForm(request.POST)

        if form.is_valid():
            username = form.clean_username()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password2')
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password)
            user.save()
            login(request, user)

            return redirect('/')

        context = {'form': form, 'message': 'Password or email is incorrect'}
        return render(request, self.template_name, context)
