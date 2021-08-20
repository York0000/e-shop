from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from posts.forms import CommentModelForm
from posts.models import PostModel, PostTagModel


class PostsListView(ListView):
    template_name = 'blog.html'
    paginate_by = 3

    def get_queryset(self):
        qs = PostModel.objects.order_by('-pk')
        s = self.request.GET.get('s')
        tag = self.request.GET.get('tag')

        if tag:
            qs = qs.filter(tags__title=tag)

        if s:
            qs = qs.filter(title__icontains=s)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        context['tags'] = PostTagModel.objects.all()

        context['recent_posts'] = PostModel.objects.order_by('-pk')[:3]

        return context


class PostDetailView(DetailView):
    template_name = 'blog-details.html'
    model = PostModel


class CommentCreateView(CreateView):
    form_class = CommentModelForm

    def form_valid(self, form):
        form.instance.post = get_object_or_404(PostModel, pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('posts:detail', kwargs={'pk': self.kwargs.get('pk')})
