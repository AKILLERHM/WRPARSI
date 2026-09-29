from django.urls import path
from . import views


urlpatterns = [

    path("Items/", views.items_page, name="ItemsPage"),
    path("items/search/", views.item_search, name="ItemSearch"),
    
    path("items/<slug:slug>/detail", views.item_page, name="ItemDetail"),
]