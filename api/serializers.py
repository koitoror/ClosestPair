from rest_framework import serializers


class PointsSerializer(serializers.Serializer):
    points = serializers.CharField(max_length=200)

    def validate_points(self, value):
        point_pairs = value.split(';')
        if len(point_pairs) < 2:
            raise serializers.ValidationError("At least a pair of point_pairs is required.")  # noqa
        for point_pair in point_pairs:
            point_pair_list = point_pair.split(',')
            if len(point_pair_list) != 2:
                raise serializers.ValidationError("Invalid point_pair format!")
            try:
                int(point_pair_list[0])
                int(point_pair_list[1])
                # x, y = point_pair_list
                # x, y = int(x), int(y)
            except ValueError:
                raise serializers.ValidationError("Invalid point_pair values!")
        return value
