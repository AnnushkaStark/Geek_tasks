from django.shortcuts import render, HttpResponse
from django.views.generic import View
import lorem

# Create your views here.
import logging

logger = logging.getLogger(__name__)


class IndexPageView(View):
    """
    Представление стартовой страницы
    """
    def get(self,request):
        """
        Отображение параграфа lorem
        """
        text = lorem.text()
        logger.info("Пользователь прешел на  стартовую страницу ")
        return HttpResponse(f"{text}")


class PageAbout(View):
    """
    Представление страницы обо мне
    """
    def get(self,request):
        """
        Отображение параграфа lorem
        """
        text = lorem.text()
        logger.info("Пользователь прешел на страницу обо мне")
        return HttpResponse(f"{text}")
   

