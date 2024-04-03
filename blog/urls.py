from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns=[
    path("",views.index,name="index"),
    path("post/<str:title>",views.post,name="post"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("category/<str:name>",views.category,name="category"),
    path("tag/<str:name>",views.tag,name="tag"),
    path("search",views.search,name="search"),
    path("create",views.create,name="create"),
    path("subscribe",views.subscribe,name="subscribe"),
    path("post/<str:title>/comment/", views.add_comment_to_post, name="comment"),
    path("login",LoginView.as_view(),name="blog_login"),
    path("logout",LogoutView.as_view(),name="blog_logout")
]
