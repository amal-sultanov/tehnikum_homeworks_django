from django.shortcuts import render

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
