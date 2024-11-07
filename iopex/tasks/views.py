
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tasks.serializers import TaskSerializer
from tasks.models import Tasks

# Create your views here.


class TasksView(APIView):
    """Creates user for specified email and name
    """
    def post(self, request):
        """Creation of tasks
        """
        try:
            serializer = TaskSerializer(data=request.data)
            return self.serializer_validations(serializer)
        except Exception as e:
            print(f"{e=}")
            return Response(data= {}, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        """Fetches single task
        """
        try:
            task = Tasks.objects.get(id=request.data['id'])
            serializer = TaskSerializer(data=task)
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data= {}, status=status.HTTP_400_BAD_REQUEST)
        
    
    def put(self, request):
        try:
            serializer = TaskSerializer(data=request.data)
            return self.serializer_validations(serializer)
        except Exception as e:
            return Response(data= {}, status=status.HTTP_400_BAD_REQUEST)
        
    
    def patch(self, request):
        try:
            serializer = TaskSerializer(data=request.data, partial=True)
            return self.serializer_validations(serializer)
        except Exception as e:
            return Response(data= {}, status=status.HTTP_400_BAD_REQUEST)
        
        
    def list(self, request):
        """Fetches all tasks
        """
        try:
            task = Tasks.objects.all()
            serializer = TaskSerializer(data=task)
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data= {}, status=status.HTTP_400_BAD_REQUEST)
    def serializer_validations(self, serializer):
        """Gathered repeated code in one place
        """
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)