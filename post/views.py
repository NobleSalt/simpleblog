from django.shortcuts import render
from django.views.generic import View, ListView
from django.utils import timezone
from post.models import (
    Post,
    Category,
)
# Create your views here.


class CategoryView(View):
    template_name = 'post/home.html'

    def get(self, request, *args, **kwargs):
        catg = Category.objects.all()
        pop = Post.objects.filter(published=True).order_by('-views')
        context = {
            'cat': catg,
            'pop': pops
        }
        return render(request, self.template_name, context)


class PostListView(ListView):
    template_name = 'post/home.html'
    context_object_name = 'postlist'
    paginate_by = 5
    queryset = Post.objects.filter(
            date_published__lte=timezone.now(), published=True
            ).order_by('-date_published')
