from django import template

register = template.Library()


@register.filter(name='cactive')
def only_active_comments(comments):
    return comments.filter(active=True)
