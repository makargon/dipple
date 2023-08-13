from django.shortcuts import render
from django.views.generic import DetailView
from django.utils.timezone import now
from apps.bulb.models import News
from datetime import time


# Create your views here.
def index(request, page):
    content = News.objects.filter(publish_date__lte = now()).order_by('-id')[page*10 : page*10 + 10]
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
        print(news)
    return render(request, 'bulb\index.html',
        {
            'title': 'Наши новости',
            'news': news
        })

def none_pagination(request):
    return index(request, 0)

def views_post(request, post):
    content = News.objects.filter(pk = post)
    print(312321312312312313123211231)
    return render(request, 'bulb\index.html',
        {
            'title': i.title,
            'news_id': i.pk,
            'html_content': i.html_content, 
            'publish_date':i.publish_date,
            'news_description':i.description,
            'img':i.main_img_url
        })


class NewsView(DetailView):
    model = News