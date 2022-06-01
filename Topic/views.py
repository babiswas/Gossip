from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from .models import Topic, Comment
from .forms import TopicForm, CommentForm
from django.urls import reverse_lazy


# Create your views here.


class TopicList(ListView):
    model = Topic

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CommentList(ListView):
    model = Comment
    template_name = 'Topic/comment_list.html'
    paginate_by = 20

    def get_queryset(self):
        topic = Topic.objects.get(pk=self.kwargs.get('topic_id', None))
        queryset = Comment.objects.filter(topic=topic)
        return queryset


class TopicView(FormView):
    template_name = 'Topic/topic_form.html'
    form_class = TopicForm
    success_url = '/topic/topic_list/'

    def form_valid(self, form):
        if form.is_valid():
            form.save(self.request.user)
        return super().form_valid(form)


class CommentView(FormView):
    template_name = 'Topic/comment_form.html'
    form_class = CommentForm

    def get_success_url(self, **kwargs):
        return reverse_lazy('Topic:comments', kwargs={'topic_id': self.kwargs.get('topic_id')})

    def form_valid(self, form):
        message_id = self.kwargs['topic_id']
        if form.is_valid():
            form.save(self.request.user, message_id)
        return super().form_valid(form)
