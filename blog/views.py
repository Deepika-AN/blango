from django.shortcuts import render
from django.utils import timezone
from blog.models import Post
from django import template

register = template.Library()

# Create your views here.
def index(request):
  posts = Post.objects.filter(published_at=timezone.now())
  return render(request, "index.html", {"posts": posts})

@register.filter
def author_details(author):
    if not isinstance(author, user_model):
        # return empty string as safe default
        return ""

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"

    if author.email:
        prefix = format_html('<a href="mailto:{}">', author.email)
        suffix = format_html("</a>")
    else:
        prefix = ""
        suffix = ""

    return format_html('{}{}{}', prefix, name, suffix)