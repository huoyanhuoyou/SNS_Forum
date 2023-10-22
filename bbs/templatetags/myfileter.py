from django import template
import markdown

register = template.Library()

@register.filter()
def mdToHtml(x):
    return markdown.markdown(x)