from django import template
from ..models import MenuItem

register = template.Library()


@register.inclusion_tag('menuapp/draw_menu.html')
def draw_menu(menu_name):
    try:
        menu_item = MenuItem.objects.filter(menu_name=menu_name).first()
        menu_tree = menu_item.get_descendants(include_self=True)
    except MenuItem.DoesNotExist:
        menu_tree = None

    return {'menu_tree': menu_tree}










