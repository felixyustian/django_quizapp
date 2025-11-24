from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quiz_app.urls')), # Sambungkan ke aplikasi quiz
]