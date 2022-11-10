from django.urls import path
from . import views

app_name='blog'
urlpatterns = [
    # path('', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('detail/<slug:post>/<int:pk>/',views.post_detail,name="post-detail"),
    path('account-form/', views.UserAccount, name="UserAccount")
]