from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, Http404
import crawltop
import BeautifulSoup as bs
import requests

SOOLVE_URL = 'http://soovle.com/top/'
GOOGLE_URL = 'https://trends.google.com/trends/hottrends/atom/hourly'


# Create your views here.
def get_top_from_soolve(request):
    top_keywords = crawltop.craw_and_parse(SOOLVE_URL, 'soolve')
    return JsonResponse(top_keywords, safe=False)


def get_top_from_google(request):
    response = requests.get(GOOGLE_URL, timeout=3)
    response.raise_for_status()
    soup = bs.BeautifulSoup(response.content)
    c = soup.findAll(text=lambda x:isinstance(x, bs.CData))
    c = '<html>' + ''.join(c) + '</html>'
    ps = bs.BeautifulSoup(c)
    links = ps.findAll('a')
    top_kwgs = map(lambda x:str(x.string), links)
    return JsonResponse(top_kwgs, safe=False)