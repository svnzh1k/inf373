from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Subject, Lecture, Practice, Subscriber
from .serializers import SubjectSerializer, LectureSerializer, PracticeSerializer, SubscriberSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache

from .tasks import notify_subscribers_new_subject

class SubjectListView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(responses={200: SubjectSerializer(many=True)})
    def get(self, request):
        cache_key = 'subject_list'
        cached_data = cache.get(cache_key)
        if cached_data is not None:
            return Response(cached_data)

        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        cache.set(cache_key, serializer.data, timeout=60 * 5)
        return Response(serializer.data)


class SubjectCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(request=SubjectSerializer, responses={201: SubjectSerializer})
    def post(self, request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            subject = serializer.save()
            # notify_subscribers_new_subject.delay(subject.subject_name)  # 🚀
            notify_subscribers_new_subject.apply_async(
                args=[subject.subject_name],
                countdown=100
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class SubjectUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Subject, pk=pk)

    @extend_schema(request=SubjectSerializer, responses={200: SubjectSerializer})
    def patch(self, request, pk):
        subject = self.get_object(pk)
        serializer = SubjectSerializer(subject, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SubjectDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Subject, pk=pk)

    @extend_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        subject = self.get_object(pk)
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class LectureListView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(responses={200: LectureSerializer(many=True)})
    def get(self, request):
        cache_key = 'lecture_list'
        cached_data = cache.get(cache_key)
        if cached_data is not None:
            return Response(cached_data)

        lectures = Lecture.objects.all()
        serializer = LectureSerializer(lectures, many=True)
        cache.set(cache_key, serializer.data, timeout=60 * 5)
        return Response(serializer.data)



class LectureCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(request=LectureSerializer, responses={201: LectureSerializer})
    def post(self, request):
        serializer = LectureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LectureUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Lecture, pk=pk)

    @extend_schema(request=LectureSerializer, responses={200: LectureSerializer})
    def patch(self, request, pk):
        lecture = self.get_object(pk)
        serializer = LectureSerializer(lecture, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LectureDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Lecture, pk=pk)

    @extend_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        lecture = self.get_object(pk)
        lecture.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class PracticeListView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(responses={200: PracticeSerializer(many=True)})
    def get(self, request):
        cache_key = 'practice_list'
        cached_data = cache.get(cache_key)
        if cached_data is not None:
            return Response(cached_data)

        practices = Practice.objects.all()
        serializer = PracticeSerializer(practices, many=True)
        cache.set(cache_key, serializer.data, timeout=60 * 5)
        return Response(serializer.data)



class PracticeCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(request=PracticeSerializer, responses={201: PracticeSerializer})
    def post(self, request):
        serializer = PracticeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PracticeUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Practice, pk=pk)

    @extend_schema(request=PracticeSerializer, responses={200: PracticeSerializer})
    def patch(self, request, pk):
        practice = self.get_object(pk)
        serializer = PracticeSerializer(practice, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PracticeDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Practice, pk=pk)

    @extend_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        practice = self.get_object(pk)
        practice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



class SubscriberCreateView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(request=SubscriberSerializer, responses={201: SubscriberSerializer})
    def post(self, request):
        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class SubscriberListView(APIView):
    permission_classes = [IsAuthenticated]  # например, только админы

    @extend_schema(responses={200: SubscriberSerializer(many=True)})
    def get(self, request):
        subscribers = Subscriber.objects.all()
        serializer = SubscriberSerializer(subscribers, many=True)
        return Response(serializer.data)
