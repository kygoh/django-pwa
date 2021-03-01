import json

from django import template
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.html import mark_safe

register = template.Library()


# refer: https://stackoverflow.com/a/54696878
@register.simple_tag(takes_context=True)
def render_nested(context, param, root=True):
    if type(param) is str:
        # create template from text
        tpl = template.Template(param)
        return tpl.render(context)
    elif type(param) is dict:
        res = dict([(key, render_nested(context, value, False)) for key, value in param.items()])
    elif type(param) is list:
        res = [render_nested(context, value, False) for value in param]

    if root:
       return mark_safe(json.dumps(res, cls=DjangoJSONEncoder))
    else:
       return res


