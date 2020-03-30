from django.test import TestCase
from .models import Point, Sinonim
from mixer.backend.django import mixer

# Create your tests here.

class PointTestCase(TestCase):

    def setUp(self):
        self.point_str = mixer.blend(Point, pointLabel='Липецк', pointType__name='Virtual')

    def test_str(self):
        self.assertEqual(str(self.point_str), 'Липецк')


class SinonimTestCase(TestCase):

    def setUp(self):
        self.sinonim_str = mixer.blend(Sinonim, name='Lipetsk')

    def test_str(self):
        self.assertEqual(str(self.sinonim_str), 'Lipetsk')