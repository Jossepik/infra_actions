from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось! Я смог это сделать!')


def second_page(request):
    return HttpResponse('А это вторая страница! Я смог это сделать!!')
