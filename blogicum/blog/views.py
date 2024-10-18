from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post, Category
from django.utils.timezone import now


class IndexListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        today = now()
        print(today)
        data = (Post.objects
                .filter(pub_date__lte=today)
                .filter(is_published=True)
                .filter(category__is_published=True)
                .order_by('-created_at')[:5])
        return data


class CategoryListView(ListView):
    model = Post
    template_name = 'blog/category.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        category = Category.objects.get(slug=category_slug)
        if category.is_published:
            data = (Post.objects
                    .filter(category__slug=category_slug)
                    .filter(is_published=True)
                    .filter(pub_date__lte=now()))
            return data
        return HttpResponseNotFound('<p>Не найдено публикаций</p>')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super().get_context_data(**kwargs)
        # Get the category based on the slug from URL
        category_slug = self.kwargs.get('category_slug')
        context['category'] = get_object_or_404(Category,
                                                slug=category_slug,
                                                is_published=True)
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        if self.kwargs['pk'] == 0:
            self.kwargs['pk'] = 1
        obj = get_object_or_404(Post,
                                pk=self.kwargs['pk'],
                                is_published=True,
                                pub_date__lte=now(),
                                category__is_published=True)

        return obj
