import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django
django.setup()

from MainApp.models import Topic, Entry

topics = Topic.objects.all()

for topic in topics:
    print(topic.id)
    #don't need .text cause we have __str__ object in models.py that 
    # returns text of topic
    print(topic)
    print(topic.date_added)

t = Topic.objects.get(id=1)
print(t)

#set all gets all entries for t object
entries = t.entry_set.all()

#prints entry text of t topic (chess cause id 1)
for e in entries:
    print(e)