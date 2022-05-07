import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django
django.setup()

from MainApp.models import Pizza

toppings = Pizza.objects.all()

for t in toppings:
    print(t.id, ' ', t)