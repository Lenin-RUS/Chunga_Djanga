from django.test import Client
from django.test import TestCase
from faker import Faker
from my_user_app.models import MyUser, Place_of_job


class OpenViewsTest(TestCase):

    def setUp(self):
        self.client=Client()
        self.fake=Faker()

    def test_statuses(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/send_mail/',
                            {'name': self.fake.name(), 'message': self.fake.text(),
                             'email': self.fake.email(), 'phone': self.fake.phone_number()})
        self.assertEqual(response.status_code, 302)


    def test_login_required(self):
        job=Place_of_job.objects.create(name='Gascade')
        MyUser.objects.create_user(username='Lenin_user', email='test@test.com', password='Slanin742', job=job, is_superuser=1)

        # Он не вошел
        response = self.client.get('/new_point/')
        self.assertEqual(response.status_code, 302)

        # Логинимся
        self.client.login(username='Lenin_user', password='Slanin742')
        response = self.client.get('/new_point/')
        print('Answer:  ',response.status_code)
        self.assertEqual(response.status_code, 200)
