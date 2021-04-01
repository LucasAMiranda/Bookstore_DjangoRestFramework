from django.conf.urls import url
from books.views import BookCollection


urlpatterns = [
    url(
        r'books$',
        BookCollection.as_view()
    )
]
