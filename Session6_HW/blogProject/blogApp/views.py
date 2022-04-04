from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def new(request):
    if request.method == 'POST':
        print(request.POST)
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'],
        )
        return redirect('list')

    return render(request, 'new.html')

def count_articles(category_name):
    result = 0
    for article in Article.objects.all():
        if article.category == category_name:
            result += 1
    return result

def list(request):
    return render(request, 'list.html', {'articles': Article.objects.all(), 'article_nums':
    {
        'hobby': count_articles('hobby'),
        'food': count_articles('food'),
        'programming': count_articles('programming'),
    }})

def category(request, category_name):
    result = []
    if category_name == 'none':
        category_name = ''
    for article in Article.objects.all():
        if article.category == category_name:
            result.append(article)
    return render(request, 'category.html', {'articles': result})

def detail(request, article_id):
    print(article_id)
    return render(request, 'detail.html', {'article': Article.objects.get(id=article_id)} )