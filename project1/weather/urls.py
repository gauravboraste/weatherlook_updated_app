from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path("result", views.result, name="result"),
    path("previous",views.previous,name="previous"),
    # path('social_links', views.social_links),
]