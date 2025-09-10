from django.urls import path
from . import views

app_name = "news"

urlpatterns = [
    path('',views.home, name="home"),
    path('stocknews',views.stock_news,name="stock_news")
]
