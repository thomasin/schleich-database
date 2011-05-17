import re
from django.template.defaultfilters import stringfilter, slugify
from django import template
from schleich.catalogue.models import Animal

register = template.Library()

names = dict([(a.name, a.slug) for a in Animal.objects.all()])
slugs = dict([(value, key) for key, value in names.items()])

def animal_url(value):
    value = value.group()
    prefix = str(value).split('#')[0]
    name = str(value).split('#')[1]
    slug = slugify(name)
    try:
        return '%s<a href="/catalogue/%s" class="%s">%s</a>'%(prefix, names[name], slug, name)
    except KeyError:
        try:
            return '%s<a href="/catalogue/%s" class="%s">%s</a>'%(prefix, name, slug, slugs[name])
        except KeyError:
            return value


@register.filter
@stringfilter
def hashtags(value):
    return re.sub('#[\w-]+', animal_url, value)

