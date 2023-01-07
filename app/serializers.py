from rest_framework import serializers
from .models import  *


#teacher model serializers
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = (
            "id", 
            "tName",
            "profession",
        )
        # depth= 1 
        depth= 0

    def save(self):
        teacher = Teacher(
            tName=self.validated_data["tName"],
            profession=self.validated_data["profession"]

        )
        teacher.save()
        return teacher

#student model serializer
class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        
    def save(self):
        student = Student(
            sName=self.validated_data["sName"],
            age=self.validated_data["age"],
            # foreign key field
            teacherName=self.instance 
        )
        student.save()
        return student

#Coordinators model serializer
class CoordinatorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinators
        fields = "__all__"
        
    def save(self):
        coordinator = Coordinators(
            cName=self.validated_data["cName"],
            workPlace=self.validated_data["workPlace"],
    
        )
        coordinator.save()
        return coordinator


        