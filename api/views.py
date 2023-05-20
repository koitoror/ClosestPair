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
            point_pairs = []
            for point in points:
                point_pairs.append([float(x) for x in point.split(',')])

            closest_pair = self.calculate_closest_pair(point_pairs)

            points = Points(
                points=serializer.validated_data['points'], closest_pair=closest_pair)  # noqa
            points.save()

            response_data = {
                'closest_pair': closest_pair
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # noqa

    @staticmethod
    def calculate_closest_pair(point_pairs):
        closest_pair = []
        manhattan_distances = []

        # Calculate manhattan_distances between all pairs
        for i in range(len(point_pairs)):
            for j in range(i+1, len(point_pairs)):
                distance = ((point_pairs[i][0] - point_pairs[j][0]) ** 2 +
                            (point_pairs[i][1] - point_pairs[j][1]) ** 2) ** 0.5
                manhattan_distances.append((i, j, distance))

        # Sort manhattan_distances in ascending order
        manhattan_distances.sort(key=lambda x: x[2])

        # Get the closest pair
        closest_indices = [manhattan_distances[0]
                           [0], manhattan_distances[0][1]]
        closest_pair = [
            ','.join(str(point_pair) for point_pair in point_pairs[idx]) for idx in closest_indices]

        return ';'.join(closest_pair)
