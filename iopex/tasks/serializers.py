from rest_framework import serializers
from tasks.models import Tasks, TASK_STATUS

class TaskSerializer(serializers.ModelSerializer):
    """Serializes task object
    """

    class Meta:
        model = Tasks
        fields = "__all__"
        
    def create(self, validated_data):
        return Tasks.objects.create(
            title=validated_data['title'],
            description=validated_data.get('description',""),
            due_date=validated_data.get('due_date'),
            status=validated_data['status'],
            user=validated_data['user'],
        )