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

# Новый тест. Проверяет создание синонима при создании новой точки
class test_save_point_add_sinomim(TestCase):
    def setUp(self):
        self.point_sin = mixer.blend(Point, pointLabel='Липецк', pointType__name='Virtual')
    def test_save(self):
        print(self.point_sin)
        self.assertEqual(Sinonim.objects.filter(root_point=self.point_sin).exists(), True)
