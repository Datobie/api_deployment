from rest_framework import serializers
from .models import Student, Course, Instructor
from django.contrib.auth.models import User


class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(max_length=100)
    about_course = serializers.CharField()
    duration = serializers.CharField(max_length=50)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    start_date = serializers.DateField()
    end_date = serializers.DateField()


    def validate(self, attrs):
        if attrs['duration'] != "3 months":
            raise serializers.ValidationError("please duration must be up to 3 month")
        return super().validate(attrs)
    
    # def validate_price(self, value):
    #     if not isinstance(value, [float]):
    #         raise serializers.ValidationError("only decimals are allowed")
    
    def create(self, validated_data):
        return Course.objects.create(**validated_data)
        # return super().create(validated_data)
    
    def update(self, instance, validated_data): 
        instance.title=validated_data.get('title', instance.title)
        instance.about_course=validated_data.get('about_course', instance.about_course)
        instance.duration=validated_data.get('duration', instance.duration)
        instance.price=validated_data.get('price', instance.price)
        instance.start_date=validated_data.get('start_date', instance.start_date)
        instance.end_date=validated_data.get('end_date', instance.end_date)
        instance.save()
        return instance
        # return super().update(instance, validated_data)



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["name", "course", "gender", "age", "email"]


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ["name", "course", "gender", "age", "email"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]