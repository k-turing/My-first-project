from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import Article

# Create your views here.
def index(request):
    """トップページ"""
    return render(request, 'menter/index.html')

def menter(request):
    """メンター"""
    return render(request, 'menter/menter.html')

def comment(request):
    """コメント"""
    if request.method == 'POST':
        article = Article(title=request.POST['title'], text=request.POST['text'], posted_at=timezone.now())
        article.save()
    articles = Article.objects.order_by('-posted_at')
    context = {
        'articles': articles
    }
    return render(request, 'menter/comment.html', context)

def detail(request, article_id):
    """"ディテール"""
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    context = {
        'article': article
    }
    return render(request, 'menter/detail.html', context)

def like(request, article_id):
    """ライク"""
    try:
        article = Article.objects.get(pk=article_id)
        article.like += 1
        article.save()
    except Article.DoesNotExist:
        raise Http404('Article does not exist')

    return HttpResponseRedirect(reverse(detail, args=[article_id]))


def contact(request):
    """コンタクト"""
    return render(request, 'menter/contact.html')

def philosophy(request):
    """哲学"""
    return render(request, 'menter/philosophy.html')

def about(request):
    """アバウト"""
    return render(request, 'menter/about.html')
