from django.test import TestCase
from django.urls import reverse, resolve
from rest_framework import status, serializers
from rest_framework.test import APIClient

from .models import Points
from .views import PointsAPIView
from .serializers import PointsSerializer


class PointsAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('points-api')
        self.valid_points = {
            "points": "2,2;-1,30;20,11;4,5"
        }
        self.invalid_points_values = {
            "points": "2,2;a,b;-1,30",
        }
        self.invalid_points_format = {
            "points": "2,2;30",
        }
        self.invalid_points_single_pair = {
            "points": "2,2",
        }
        self.invalid_points_blank = {
            "points": "",
        }

    def test_add_points(self):
        data = {'points': '2,2;-1,30;20,11;4,5'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Points.objects.count(), 1)
        points = Points.objects.first()
        self.assertEqual(points.points, '2,2;-1,30;20,11;4,5')
        self.assertEqual(points.closest_pair, '2,2;4,5')

    def test_add_points_invalid_input(self):
        data = {'points': '2,2'}
        response = self.client.post(self.url, data, format='json')
        print('response *** → ', response)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Points.objects.count(), 0)

    def test_get_points_views(self):
        print(resolve(self.url).func)

        self.assertEqual(resolve(self.url).func.view_class, PointsAPIView)

    def test_get_points_model(self):
        points = Points.objects.create(
            points='2,2;-1,30;20,11;4,5', closest_pair='2,2;4,5')
        self.assertEqual(str(points), "2,2;4,5")

    def test_points_serializer_validates_invalid_points_values(self):
        """
        Test if the serializer validated points values
        """
        serializer = PointsSerializer(data=self.invalid_points_values)
        self.assertRaises(
            serializers.ValidationError,
            serializer.is_valid,
            raise_exception=True)
        self.assertIn('Invalid point_pair values!',
                      serializer.errors['points'][0])

    def test_points_serializer_validates_invalid_points_format(self):
        """
        Test if the serializer validated points
        """
        serializer = PointsSerializer(data=self.invalid_points_format)
        self.assertRaises(
            serializers.ValidationError,
            serializer.is_valid,
            raise_exception=True)
        self.assertIn('Invalid point_pair format!',
                      serializer.errors['points'][0])

    def test_points_serializer_validates_invalid_points_single_pair(self):
        serializer = PointsSerializer(data=self.invalid_points_single_pair)
        self.assertRaises(
            serializers.ValidationError,
            serializer.is_valid,
            raise_exception=True)
        self.assertIn('At least a pair of point_pairs is required.',
                      serializer.errors['points'][0])

    def test_points_serializer_validates_invalid_points_blank(self):
        serializer = PointsSerializer(data=self.invalid_points_blank)
        self.assertFalse(serializer.is_valid())
        self.assertRaises(
            serializers.ValidationError,
            serializer.is_valid,
            raise_exception=True)
        self.assertIn(serializer.errors['points']
                      [0], 'This field may not be blank.')

    def test_points_serializer_validates_valid_points(self):
        serializer = PointsSerializer(data=self.valid_points)
        serializer.is_valid()
        self.assertEqual(self.valid_points, serializer.data)
