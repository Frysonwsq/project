from django.conf.urls import url, include
from xm import views

# api url 配置
urlpatterns = [
    url(r'^catagory/$',views.GetGoodView.as_view()),
    url(r'^commodity/detail/$',views.GoodView.as_view()),
]