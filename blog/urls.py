from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('detail/<slug:post>/<int:pk>',views.post_detail,name="post-detail")
]