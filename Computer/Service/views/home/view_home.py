from django import conf
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import requests, json
from bs4 import BeautifulSoup
from django.conf import settings
import time
# Create your views here.

class HomeView(View):
    def get(self, request):
        while True:
            try:
                # Give city name
                url = "https://ipgeolocation.abstractapi.com/v1/"
                querystring = {"api_key":"a738621682674587aa916f25aa686072"}
                headers = {}
                response = requests.request("GET", url, headers=headers, params=querystring)
                city_name = json.loads(response.text)['city']

                
                # API Google 
                city = city_name+" weather"
                city = city.replace(" ", "+")
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
                res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
                print("Searching...\n")
                soup = BeautifulSoup(res.text, 'html.parser')
                location = soup.select('#wob_loc')[0].getText().strip()
                time = soup.select('#wob_dts')[0].getText().strip()
                info = soup.select('#wob_dc')[0].getText().strip()
                weather = soup.select('#wob_tm')[0].getText().strip()
                print(location)
                print(time)
                print(info)
                print(weather+"°C")

            
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
                title_1 = data["articles"][1]['title']
                title_2 = data["articles"][2]['title']

                data = data["articles"][0]
                context = {
                    "success": True,
                    "search": search,
                    'title':data['title'],
                    'title_1':title_1,
                    'title_2':title_2,
                    'url':data['url'],
                    'urlToImage':data['urlToImage'],
                    'author':data['author'],

                    'location':str(location).split(',')[-1],
                    'time':str(time),
                    'info':str(info),
                    'weather':str(weather),
                }     
            except Exception as e:
                print(str(e))
                time.sleep(2)
                continue
            return render(request, 'home/index.html',context)
            
    def post(self, request):
        pass