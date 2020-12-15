from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#from .views import SignUpViews

urlpatterns = [
	path('admin/', admin.site.urls),
#	path('signup/', SignUpViews.as_view(), name='signup'),
	path('', include('blog.urls')),
	path('polls/', include('polls.urls')),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)