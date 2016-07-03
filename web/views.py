from django.views.generic import ListView
from .models import Memo

class MemoList(ListView):
    model = Memo
