from django.urls import path
from .views import *
urlpatterns = [
     path("",home.as_view(),name='modir'),
     path("create/",create.as_view(),name='create'),
     path("delete/<int:pk>",delete,name='delete'),
     path("update/<int:pk>",update.as_view(),name='update'),
     path("comment/",update_comment,name='comment'),
     path("checkouts/",checkouts.as_view(),name='checkouts'),
     path("checkout/<int:pk>",checkoutdet.as_view(),name='checkout'),
     path("checkouts/delete/<int:pk>",deletecheck,name='deletecheck'),
     path("about/<int:pk>",aboutup.as_view(),name='aboutup'),
     path("homewidgets/",homewidgets.as_view(),name='homewidgets'),
     path("homewidget/",homewidget.as_view(),name='homewidget'),
     path("homewidgets/delete/<int:pk>",deletewi,name='deletewi'),
     path("favpost/<int:pk>",favpost.as_view(),name='favpost'),

]
