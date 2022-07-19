from django.urls import path
from news.views import scrape_latest,homepage,scrape_science,scrape_india,scrape_world,scrape_jobs,scrape_hatke
urlpatterns = [
  path('scrape_latest',scrape_latest, name="scrape_latest"),
  path('scrape_science',scrape_science, name="scrape_science"),
  path('scrape_india',scrape_india, name="scrape_india"),
  path('scrape_world',scrape_world, name="scrape_world"),
  path('', homepage, name="home"),
  path('scrape_jobs',scrape_jobs, name="scrape_jobs"),
  path('scrape_hatke',scrape_hatke, name="scrape_hatke"),
  
 ]
