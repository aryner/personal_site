from django import template

register = template.Library()

@register.inclusion_tag('blog/replies.html')
def show_replies(comment, logged_in, post_slug):
  replies = comment.children.all()
  return {'replies':replies,'logged_in':logged_in,'post_slug':post_slug}

