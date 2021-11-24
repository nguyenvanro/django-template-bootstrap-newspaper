from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.conf import settings
import requests
import json

class Detail_Trending(View):
    def get(self, request):
        page = request.GET.get('page', 1)
        search = request.GET.get('search', None)

        if search is None or search=="top":
            # get the top news
            url = "https://newsapi.org/v2/top-headlines?country={}&page={}&apiKey={}".format(
                "us",1,settings.APIKEYNEWS
            )
        else:
            # get the search query request
            url = "https://newsapi.org/v2/everything?q={}&sortBy={}&page={}&apiKey={}".format(
                search,"popularity",page,settings.APIKEYNEWS
            )
        r = requests.get(url=url)

        data = r.json()
        if data["status"] != "ok":
            return HttpResponse("<h1>Request Failed</h1>")

        data = data["articles"][1:4]
        print(data)

        context = {
            "success": True,
            "search": search,
            'data':data,
        }
        
        # send the news feed to template in context
        return render(request, 'detail/detail.html',context)
        
    def post(self, request):
        pass