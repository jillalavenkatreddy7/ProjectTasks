from django.shortcuts import render
from app import scraping
def articles(request):
    news=[]
    news2=[]
    data=scraping.headings
    data2=scraping.headings1
    for x in data:
        news.append(x.text)
    for y in data2:
        news2.append(y.text)
    print(news2)
    news2.remove(news2[-1])
    news2.remove(news2[-2])
    news2.remove(news2[-3])
    re_news=news2
    re_news.remove(re_news[-1])

    return render(request,"articles.html",{"data":news,"data1":re_news})