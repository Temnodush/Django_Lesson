from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView, TemplateView

from blogs.models import BlogPost


# Create your views here.



class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'content', 'preview', 'is_published']
    template_name = 'blogs/blogpost_form.html'
    success_url = reverse_lazy('blogs:blogpost_list')

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blogs/blogpost_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save(update_fields=['views_count'])
        return obj

class BlogPostDraftListView(ListView):
    model = BlogPost
    template_name = 'blogs/blogpost_draft_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=False)

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'content', 'preview', 'is_published']
    template_name = 'blogs/blogpost_form.html'
    success_url = None

    def get_success_url(self):
        return reverse('blogs:blogpost_detail', kwargs={'pk': self.object.pk})


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blogs/blogpost_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)

class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blogs/blogpost_confirm_delete.html'
    success_url = reverse_lazy('blogs:blogpost_list')

class BlogPostPublishView(UpdateView):
    model = BlogPost
    fields = []
    success_url = reverse_lazy('blogs:blogpost_draft_list')

    def form_valid(self, form):
        self.object.is_published = True
        self.object.save()
        return super().form_valid(form)
