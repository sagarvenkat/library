from django.urls import path
from .import views
urlpatterns=[
              path('',views.index, name='index'),
              path('books/',views.l.as_view(),name='books'),
              path('Author',views.author,name='author'),
              path('book/<int:pk>', views.BookDetailView.as_view(), name='book-deta'),
              path('author/<int:pk>',views.a, name='a'),
              path('f/',views.re),
              path('f/k/',views.re)
            ]
