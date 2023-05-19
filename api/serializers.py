from rest_framework import serializers


class PointsSerializer(serializers.Serializer):
    points = serializers.CharField(max_length=200)

    def validate_points(self, value):
        points = value.split(';')
        if len(points) < 2:
            raise serializers.ValidationError("At least 2 points are required.")
        for point in points:
            pointers = point.split(',')
            if len(pointers) != 2:
                raise serializers.ValidationError("Invalid pointer format!.")
            try:
                float(pointers[0])
                float(pointers[1])
            except ValueError:
                raise serializers.ValidationError("Invalid pointer value!.")
        return value
