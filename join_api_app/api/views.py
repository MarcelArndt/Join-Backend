
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from .serializer import ContactSerializer, TasksSerializer, SummaryDetailsSerializer, FindContactByEmailSerializer
from join_api_app.models import Contact, Tasks, SummaryDetails


#_________________________     Contact     _________________________
class ContactViewSet(generics.CreateAPIView, generics.RetrieveAPIView, generics.UpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get(self, request, *args, **kwargs):
        serializer = ContactSerializer(Contact.objects.all(), many=True, context={'request': request})    
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data, many=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response("data saved", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data, many=True, context={'request': request})
        if serializer.is_valid():
            Contact.objects.all().delete()
            serializer.save()
            return Response("Contacts saved", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        Contact.objects.all().delete()
        return Response('All Contacts are deleted', status=status.HTTP_204_NO_CONTENT)


class FindContactByEmailView(APIView):
    def post(self, request):
        serializer = FindContactByEmailSerializer(data = request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            return Response(data)
        return Response(serializer.errors)

#_________________________     Task     _________________________
class TaskOverViewSet(generics.CreateAPIView, generics.RetrieveAPIView, generics.UpdateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer

    def get(self, request, *args, **kwargs):
        serializer = TasksSerializer(Tasks.objects.all(), many=True, context={'request': request})    
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = TasksSerializer(data=request.data, many=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response("Tasks saved", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, *args, **kwargs):
        serializer = TasksSerializer(data=request.data, many=True, context={'request': request})
        if serializer.is_valid():
            Tasks.objects.all().delete()
            serializer.save()
            return Response("data saved", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        Tasks.objects.all().delete()
        return Response('All Tasks are deleted', status=status.HTTP_204_NO_CONTENT)

#_________________________     SummaryDetails    _________________________

class SummaryDetailViewSet(generics.CreateAPIView, generics.RetrieveAPIView, generics.UpdateAPIView):
    queryset = SummaryDetails.objects.all()
    serializer_class = SummaryDetailsSerializer

    def get(self, request, *args, **kwargs):
        if not self.queryset.exists():
            SummaryDetails.objects.create(taskInBoard=0, taskInToDo=0, taskInDone=0, taskInProgress=0, taskInFeedback=0, urgendTaskUpcoming=[])
        summary_details = self.queryset.first()
        serializer = self.get_serializer(summary_details, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

