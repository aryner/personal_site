from django import template

register = template.Library()

@register.inclusion_tag('blog/replies.html')
def show_replies(comment):
  replies = comment.children.all()
  return {'replies':replies}

