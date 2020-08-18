from django.shortcuts import render
from newsapi import NewsApiClient
 
def bbc(request):
    newsapi = NewsApiClient(api_key="fc173b1c0f264d0685987b66e418fd8e")
    topheadlines = newsapi.get_top_headlines(sources='bbc-news')
 
 
    articles = topheadlines['articles']
 
    desc = []
    news = []
    img = []
 
    for i in range(len(articles)):
        myarticles = articles[i]
 
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
 
 
    mylist = zip(news, desc, img)
 
 
    return render(request, 'bbc.html', context={"mylist":mylist})
