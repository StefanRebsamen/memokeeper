from django.conf.urls import url
from .views import MemoList

urlpatterns = [
    url(r'^memos/$', MemoList.as_view()),
]
