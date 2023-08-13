from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import now
from apps.bulb.models import News
from datetime import time


# Create your views here.
def index(request):
    content = News.objects.filter(publish_date__lte = now()).order_by('-id')[:6]
    news = []
    for i in content:
        news.append({
            'news_id': i.pk,
            'news_title': i.title,
            'html_content': i.html_content, 
            'publish_date':i.publish_date,
            'news_description':i.description,
            'action_click': i.action_click,
            'tag':i.tags,
            'img':i.main_img_url
        })
    return render(request, 'main/index.html',
        {
            'title': 'Главная',
            'news': news
        })

def favicon(request):
    pass