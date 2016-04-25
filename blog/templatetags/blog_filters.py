from django import template

register = template.Library()

def preview(value):
  result = value[:value.index('</p>')]
  print(result)
  return result

register.filter('preview',preview)

