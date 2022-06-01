from django.forms import ModelForm
from .models import Topic
from .models import Comment


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['topic', ]

    def save(self, user=None):
        topic = super(TopicForm, self).save(commit=False)
        if topic:
            topic.published_by = user
        topic.save()
        return topic


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', ]

    def save(self, user=None, topic_id=None):
        comment = super(CommentForm, self).save(commit=False)
        if comment:
            comment.commented_by = user
            if topic_id:
                topic = Topic.objects.get(id=topic_id)
                comment.topic = topic
        comment.save()
        return comment
