import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django
django.setup()

from MainApp.models import Pizza

pizzas = Pizza.objects.all()

for p in pizzas:
    print(p.id, ' ', p.text)

p = Pizza.objects.get(id=1)

print('Pizza: ', p.text)
#print(p.date_added)


toppings = p.toppings_set.all()

for t in toppings:
    print('Toppings: ', t.text)

