import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','capstone_project.settings')

import django
django.setup()

import random
from faker import Faker
from capstone_app.models import User

fakegen = Faker()
def populate(num = 5):
    for entry in range(num):
        fake_name = fakegen.name().split()
        fake_email = fakegen.ascii_company_email()

        first_name = fake_name[0]
        last_name = fake_name[1]

        user = User.objects.get_or_create(first_name = first_name, last_name = last_name, email = fake_email)[0]

if __name__ == '__main__':

    print("populating")
    populate(20)
    print("populating complete")
