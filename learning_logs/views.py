from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    return render(request, 'learning_logs/index.html')


def topics(request, topic_id):
    """ Show all topics. """
    topics = Topic.objects.get('id=topic_id')
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topics.html', context)
