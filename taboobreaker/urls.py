from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login_user'),
    path('swechha/', views.swechha, name='swechha'),
    path('ask/', views.ask, name='ask'),
    path('logout/', views.logout_user, name='logout_user'),
    path('answer/<int:id>', views.answer, name='answer'),
    path('swechha-blog/', views.blog, name='blog')
]