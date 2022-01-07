from rest_framework import generics, status, views, response
from .models import Campus, Institute, Courses
from .serializers import CampusSerialize, InstituteSerialize, CoursesSeralizer


class CampusList(generics.ListAPIView):
    serializer_class = CampusSerialize

    def get(self, request):
        send_data = CampusSerialize(Campus.objects.all(), many=True).data
        return response.Response({'status': 'OK', 'result': send_data})


class InstituteList(generics.ListAPIView):
    serializer_class = InstituteSerialize

    def get(self, request):
        send_data = InstituteSerialize(Institute.objects.all(), many=True).data
        return response.Response({'status': 'OK', 'result': send_data})


class CoursesList(generics.ListAPIView):
    serializer_class = CoursesSeralizer

    def get(self, requst):
        send_data = CoursesSeralizer(Courses.objects.all(), many=True).data
        return response.Response({'status': 'OK', 'result': send_data})
