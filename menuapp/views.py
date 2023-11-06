from django.shortcuts import render
from .templatetags.menu_tags import draw_menu


def index(request):
    menu_data = draw_menu('main_menu') or {'menu_tree': [], 'current_url': ''}
    return render(request, 'menuapp/index.html', {'menu_data': menu_data})



