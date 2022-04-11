from django.contrib import admin
from django.urls import path
from api.views import SnippetList, SnippetDetail
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', SnippetList.as_view()),
    path('<int:pk>/', SnippetDetail.as_view()),
    
]
