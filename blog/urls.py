from django.urls import path
from . import views
#from .views import signup_view

urlpatterns = [
    path('', views.post_list, name='post_list'),
#	path('polls/', views. ('polls.urls')),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
#	path('signup/', signup_view, name="signup"),
	path("register/", views.register_request, name="register"),
	path("login/", views.login_request, name="login"),
	path("logout/", views.logout_request, name= "logout"),
	path('<slug:slug>/', views.post_detail, name='post_detail')


]
