from rest_framework import serializers


class PointsSerializer(serializers.Serializer):
    points = serializers.CharField(max_length=200)

    def validate_points(self, value):
        points = value.split(';')
        if len(points) < 2:
            raise serializers.ValidationError("At least 2 points are required.")
        for point in points:
            coordinates = point.split(',')
            if len(coordinates) != 2:
                raise serializers.ValidationError("Invalid coordinate format!.")
            try:
                float(coordinates[0])
                float(coordinates[1])
            except ValueError:
                raise serializers.ValidationError("Invalid coordinate value!.")
        return value
