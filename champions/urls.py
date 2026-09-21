from django.urls import path
from . import views

urlpatterns = [
    # مسیردهی صفحه اصلی / home page route
    path("", views.home,  name="Home" ),
    #مسیردهی به صفحه آیتم ها و جستجو در آن
    #
    path("champions/", views.champions_view, name="Champions"),
    path("search/", views.champion_search, name="ChampionSearch"),

    path("ChampionPage/<slug:slug>/", views.champion_page, name="ChampionPage"),
    
    path("Items/", views.items_page, name="ItemsPage"),
    path("items/search/", views.item_search, name="ItemSearch"),

    path("item/<slug:slug>/detail", views.item_page, name="ItemDetail"),
]