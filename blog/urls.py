from django.urls import path,include
from . import views

urlpatterns=[
    path('api-auth/',include('rest_framework.urls')),
    path('users/',views.UserList.as_view(),name='users'),
    path('posts/',views.PostList.as_view(),name='posts'),
    path('posts/<slug:slug>/',views.PostDetails.as_view()),
    # path('login/',views.LoginView.as_view()),
    # path('logout/',views.LogoutView.as_view()),
]