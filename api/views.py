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
            pointers = []
            for point in points:
                pointers.append([float(x) for x in point.split(',')])

            closest_pairs = self.calculate_closest_pairs(pointers)

            points = Points(
                points=serializer.validated_data['points'], closest_pairs=closest_pairs)
            points.save()

            response_data = {
                'closest_pairs': closest_pairs
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def calculate_closest_pairs(pointers):
        closest_pairs = []
        distances = []

        # Calculate distances between points
        for i in range(len(pointers)):
            for j in range(i+1, len(pointers)):
                distance = ((pointers[i][0] - pointers[j][0]) ** 2 +
                            (pointers[i][1] - pointers[j][1]) ** 2) ** 0.5
                distances.append((i, j, distance))

        # Sort distances in ascending order
        distances.sort(key=lambda x: x[2])

        # Get the two closest points
        closest_indices = [distances[0][0], distances[0][1]]
        closest_pairs = [
            ','.join(str(pointer) for pointer in pointers[idx]) for idx in closest_indices]

        return ';'.join(closest_pairs)
