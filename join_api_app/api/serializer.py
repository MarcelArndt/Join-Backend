from rest_framework import serializers
from join_api_app.models import Contact,  Users, Tasks
from datetime import datetime, date



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ["id"]


class FindContactByEmailSerializer(serializers.Serializer):
    email = serializers.CharField(write_only=True)
    def validate(self, data):
        email = data.get("email")
        print(email)
        contact = Contact.objects.filter(email=email).first()
        print(contact)
        if contact:
            return {
                "isContact": True,
                "color": contact.color,
                "name" : contact.name,
                "email" : contact.email,
                "phone" : contact.phone,
                "initials" : contact.initials
            }
        return {"isContact":False}
        

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        exclude = ["id"]

class SummaryDetailsSerializer(serializers.Serializer):

    taskInBoard = serializers.SerializerMethodField()
    taskInToDo = serializers.SerializerMethodField()
    taskInDone = serializers.SerializerMethodField()
    taskInProgress = serializers.SerializerMethodField()
    taskInFeedback = serializers.SerializerMethodField()
    urgendTaskUpcoming = serializers.SerializerMethodField()

    def get_taskInToDo(self, obj):
        return Tasks.objects.filter(currentProgress=0).count()
    
    def get_taskInProgress(self, obj):
        return Tasks.objects.filter(currentProgress=1).count()
    
    def get_taskInFeedback(self, obj):
        return Tasks.objects.filter(currentProgress=2).count()
    
    def get_taskInDone(self, obj):
        return Tasks.objects.filter(currentProgress=3).count()
    
    def get_taskInBoard(self, obj):
        return Tasks.objects.all().count()
    
    def get_urgendTaskUpcoming(self, obj):
        today = datetime.today().date()
        tasks = Tasks.objects.exclude(dueDate__isnull=True)
        upcomingUrgentsTasksCounter = 0
        urgent_task_due_date = 0
        UrgentsTasksId = None
        earliestDate = date.min
        for task in tasks:
            currentDate = datetime.strptime(task.dueDate, "%Y-%m-%d")
            if task.priority == "urgent":
                upcomingUrgentsTasksCounter += 1
            if task.currentProgress < 3 and currentDate.date():
               if earliestDate > currentDate.date() or earliestDate == 0:
                    earliestDate = currentDate.date()
                    urgent_task_due_date = task.dueDate 
                    UrgentsTasksId = task.taskID
        return {"taskId": UrgentsTasksId, "amount": upcomingUrgentsTasksCounter, "dueDate": urgent_task_due_date } 
