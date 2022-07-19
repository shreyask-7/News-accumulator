from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from news.models import Headline

#function for scrapping
def scrape_latest(request):
  session = requests.Session()
  session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
  url = "https://www.ndtv.com/latest?pfrom=home-ndtv_mainnavgation"

  #content = session.get(url, verify=False).content
  r1=requests.get(url)
  #page=requests.get(url)
  coverpage=r1.content 
  soup = BSoup(coverpage, 'html.parser')
  News = soup.find_all('div', {"class":"news_Itm-cont"})
  for artcile in News:
    main = artcile.find_all('a')[0]
    paragraph=artcile.find_all('p')[0]
    link = main['href']
    #image_src = str(main.find('img')['srcset']).split(" ")[-4]
    title = main.get_text()
    real_para=paragraph.get_text()
    new_headline = Headline()
    new_headline.title = title
    new_headline.url = link
    new_headline.para=real_para
    #new_headline.image = image_src
    new_headline.save()
  #return redirect("../")
  headlines = Headline.objects.all()[::-1]
  context = {
        'object_list': headlines,
  }
  return render(request,"latest.html", context)

#Function for science news
def scrape_science(request):
  session = requests.Session()
  session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
  url = "https://www.ndtv.com/science"

  #content = session.get(url, verify=False).content
  r1=requests.get(url)
  #page=requests.get(url)
  coverpage=r1.content 
  soup = BSoup(coverpage, 'html.parser')
  News = soup.find_all('div', {"class":"news_Itm-cont"})
  for artcile in News:
    main = artcile.find_all('a')[0]
    paragraph=artcile.find_all('p')[0]
    link = main['href']
    #image_src = str(main.find('img')['srcset']).split(" ")[-4]
    title = main.get_text()
    real_para=paragraph.get_text()
    new_headline = Headline()
    new_headline.title = title
    new_headline.url = link
    new_headline.para=real_para
    #new_headline.image = image_src
    new_headline.save()
  #return redirect("../")
  headlines = Headline.objects.all()[::-1]
  context = {
        'object_list': headlines,
  }
  return render(request,"science.html", context)



#Function for india news
def scrape_india(request):
  session = requests.Session()
  session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
  url = "https://www.ndtv.com/india"

  #content = session.get(url, verify=False).content
  r1=requests.get(url)
  #page=requests.get(url)
  coverpage=r1.content 
  soup = BSoup(coverpage, 'html.parser')
  News = soup.find_all('div', {"class":"news_Itm-cont"})
  for artcile in News:
    main = artcile.find_all('a')[0]
    paragraph=artcile.find_all('p')[0]
    link = main['href']
    #image_src = str(main.find('img')['srcset']).split(" ")[-4]
    title = main.get_text()
    real_para=paragraph.get_text()
    new_headline = Headline()
    new_headline.title = title
    new_headline.url = link
    new_headline.para=real_para
    #new_headline.image = image_src
    new_headline.save()
  #return redirect("../")
  headlines = Headline.objects.all()[::-1]
  context = {
        'object_list': headlines,
  }
  return render(request,"india.html", context)

#Function for world news
def scrape_world(request):
  session = requests.Session()
  session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
  url = "https://www.ndtv.com/world-news"

  #content = session.get(url, verify=False).content
  r1=requests.get(url)
  #page=requests.get(url)
  coverpage=r1.content 
  soup = BSoup(coverpage, 'html.parser')
  News = soup.find_all('div', {"class":"news_Itm-cont"})
  for artcile in News:
    main = artcile.find_all('a')[0]
    paragraph=artcile.find_all('p')[0]
    link = main['href']
    #image_src = str(main.find('img')['srcset']).split(" ")[-4]
    title = main.get_text()
    real_para=paragraph.get_text()
    new_headline = Headline()
    new_headline.title = title
    new_headline.url = link
    new_headline.para=real_para
    #new_headline.image = image_src
    new_headline.save()
  #return redirect("../")
  headlines = Headline.objects.all()[::-1]
  context = {
        'object_list': headlines,
  }
  return render(request,"world.html", context)



#function for jobs
def scrape_jobs(request):
  session = requests.Session()
  session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
  url = "https://www.ndtv.com/jobs"

  #content = session.get(url, verify=False).content
  r1=requests.get(url)
  #page=requests.get(url)
  coverpage=r1.content 
  soup = BSoup(coverpage, 'html.parser')
  News = soup.find_all('div', {"class":"news_Itm-cont"})
  for artcile in News:
    main = artcile.find_all('a')[0]
    paragraph=artcile.find_all('p')[0]
    link = main['href']
    #image_src = str(main.find('img')['srcset']).split(" ")[-4]
    title = main.get_text()
    real_para=paragraph.get_text()
    new_headline = Headline()
    new_headline.title = title
    new_headline.url = link
    new_headline.para=real_para
    #new_headline.image = image_src
    new_headline.save()
  #return redirect("../")
  headlines = Headline.objects.all()[::-1]
  context = {
        'object_list': headlines,
  }
  return render(request,"jobs.html", context)

#function for hatke
def scrape_hatke(request):
  session = requests.Session()
  session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
  url = "https://www.ndtv.com/offbeat"

  #content = session.get(url, verify=False).content
  r1=requests.get(url)
  #page=requests.get(url)
  coverpage=r1.content 
  soup = BSoup(coverpage, 'html.parser')
  News = soup.find_all('div', {"class":"news_Itm-cont"})
  for artcile in News:
    main = artcile.find_all('a')[0]
    paragraph=artcile.find_all('p')[0]
    link = main['href']
    #image_src = str(main.find('img')['srcset']).split(" ")[-4]
    title = main.get_text()
    real_para=paragraph.get_text()
    new_headline = Headline()
    new_headline.title = title
    new_headline.url = link
    new_headline.para=real_para
    #new_headline.image = image_src
    new_headline.save()
  #return redirect("../")
  headlines = Headline.objects.all()[::-1]
  context = {
        'object_list': headlines,
  }
  return render(request,"hatke.html", context)

#function for homepage
def homepage(request):
    return render(request,"home.html")


