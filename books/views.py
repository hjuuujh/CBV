from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from .models import *

class BooksModelView(TemplateView):
    template_name = "books/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_list'] = ['Book', 'Author', 'Publisher']
        return context


class BookList(ListView):
    model = Book 
    #   object_list = Book.objects.all()
    #   context = {"object_list":object_list}
    #   return render(request,"books/book_list.html",context) 이 세줄 내장함수로 자동 실행
    #    context  변수명으로 object_list 사용, 템플릿 파일명을 모델명소문자_list.html 로 알아서 지정


class BookDetail(DetailView):
    model = Book
    #   object = Book.objects.get(pk=id)
    #   context={"object":object} 
    #   return render(request, "books/book_detail.html", context)
    #   detailview를 상속받는 경우 특정 객체 하나를 컨텍스트 변수에 담아 템플릿 시스템에 넘겨주면됨
    #   => pk로 조회하는 경우 모델 클래스 명(테이블명)만 지정해주면 됨
    #   (pk값은 url에서 추출하여 사용)
    #   context변수로 object 사용, 템플릿 파일명을 모델명소문자_detail.html로 자동 지정


class AuthorList(ListView):
    model = Author


class AuthorDetail(DetailView):
    model = Author


class PublisherList(ListView):
    model = Publisher


class PublisherDetail(DetailView):
    model = Publisher