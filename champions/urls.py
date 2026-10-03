from django.urls import path
from . import views

urlpatterns = [
    # مسیردهی صفحه اصلی / home page route
    path("", views.home,  name="Home" ),
    #مسیردهی صفحه قهرمانان و بخش سرچ بار در این اینجا / champions page and champions searchbar route
    path("champions/", views.champions_view, name="Champions"),
    path("search/", views.champion_search, name="ChampionSearch"),
    #از slug برای قشنگ تر کردن و فهمیدنی تر کردن مسیر صفحات چمپ ها کردم.
    path("ChampionPage/<slug:slug>/", views.champion_page, name="ChampionPage"),
    

    
]