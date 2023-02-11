from django.contrib import admin
from django.urls import include, path
from machina import urls as machina_urls

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('forum/', include(machina_urls)),
    path('blog/', include('blog.urls')),
]