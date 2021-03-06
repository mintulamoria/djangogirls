from django.urls import path
from .import views
#from .views import signup_view

urlpatterns = [
    path('', views.post_list, name='post_list'),
#	path('polls/', views. ('polls.urls')),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
	path("register/", views.register_request, name="register"),
	path("login/", views.login_request, name="login"),
	path("logout/", views.logout_request, name= "logout"),
	path('<slug:slug>/', views.post_detail, name='post_detail'),
	path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
	path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
	path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),

]
