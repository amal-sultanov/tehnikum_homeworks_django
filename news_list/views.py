from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from .forms import RegistrationForm
from .models import News, NewsCategory, Wishlist


def homepage(request):
    news = News.objects.all()
    categories = NewsCategory.objects.all()
    context = {'news': news, 'categories': categories}

    return render(request, 'index.html', context)


def news_page(request, pk):
    news = News.objects.get(id=pk)
    is_in_wishlist = Wishlist.objects.filter(user_id=request.user.id,
                                             user_news=news).exists() if (
        request.user.is_authenticated) else False

    context = {'news': news, 'is_in_wishlist': is_in_wishlist, }

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


def logout_view(request):
    logout(request)
    return redirect('/')


def add_to_wishlist(request, pk):
    if request.method == 'POST':
        news = News.objects.get(id=pk)
        Wishlist.objects.create(user_id=request.user.id, user_news=news).save()

        return redirect(f'/news/{pk}')


def delete_from_wishlist(request, pk):
    news = News.objects.get(id=pk)
    Wishlist.objects.filter(user_news=news).delete()

    return redirect('/wishlist')


def wishlist_page(request):
    wishlist = Wishlist.objects.filter(user_id=request.user.id)
    context = {'wishlist': wishlist}

    return render(request, 'wishlist.html', context)
