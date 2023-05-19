from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PointsSerializer
from .models import Points


class PointsAPIView(APIView):
    def post(self, request):
        serializer = PointsSerializer(data=request.data)
        if serializer.is_valid():
            points = serializer.validated_data['points'].split(';')
            coordinates = []
            for point in points:
                coordinates.append([float(x) for x in point.split(',')])

            closest_points = self.find_closest_points(coordinates)

            point_set = Points(
                points=serializer.validated_data['points'], closest_points=closest_points)
            point_set.save()

            response_data = {
                'closest_points': closest_points
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def find_closest_points(coordinates):
        closest_points = []
        distances = []

        # Calculate distances between points
        for i in range(len(coordinates)):
            for j in range(i+1, len(coordinates)):
                distance = ((coordinates[i][0] - coordinates[j][0]) ** 2 +
                            (coordinates[i][1] - coordinates[j][1]) ** 2) ** 0.5
                distances.append((i, j, distance))

        # Sort distances in ascending order
        distances.sort(key=lambda x: x[2])

        # Get the two closest points
        closest_indices = [distances[0][0], distances[0][1]]
        closest_points = [
            ','.join(str(coord) for coord in coordinates[idx]) for idx in closest_indices]

        return ';'.join(closest_points)
