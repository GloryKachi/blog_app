from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('greet/', views.greet, name='greet'),
    path('eatpizza/', views.eat_pizza, name='eat_pizza'),
    path('detail/<int:pk>/', views.post_detail, name='detail'),
    path('', views.PostListView.as_view(), name='home'),
    path('new/', views.PostCreateView.as_view(), name='post_new'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='post_delete'),
    path('<int:pk>/edit', views.PostUpdateView.as_view(), name="post_edit"),
    # path('signup/<int:pk>/', views.SignUp.as_view(), name="post_edit")
]
