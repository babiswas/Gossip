from django.urls import path
from .views import TopicView, TopicList, CommentView, CommentList

app_name = 'Topic'

urlpatterns = [
    path('create_topic/', TopicView.as_view(), name='addTopic'),
    path('topic_list/', TopicList.as_view(), name='topics'),
    path('<int:topic_id>/comment', CommentView.as_view(), name='addComment'),
    path('<int:topic_id>/comments', CommentList.as_view(), name='comments'),
]
