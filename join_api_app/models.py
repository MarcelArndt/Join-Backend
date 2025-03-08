from django.db import models

class Contact(models.Model):
    contactID = models.CharField(max_length=30, blank=True)
    name = models.CharField(max_length=120, blank=True)
    email = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    color = models.CharField(max_length=7)
    initials = models.CharField(max_length=5, blank=True, default="")

    def __str__(self):
        return self.name

class Tasks(models.Model):
    taskID = models.CharField(max_length=30, blank=True)
    title = models.CharField(max_length=255, blank=True)
    CATEGORY_CHOICES = [
        ("technicalTask", "Technical Task"),
        ("userStory", "User Story"),
        ("bug", "Bug"),
        ("feature", "Feature"),
        ("refactor", "Refactor"),
        ("documentation", "Documentation"),
        ("Testing", "Testing QA"),
        ("Analysis", "Analysis/Research"),
        ("design", "Design"),
        ("noCategory", "No Category"),
    ]
    category = models.CharField(max_length=33, choices=CATEGORY_CHOICES, default="technicalTask")
    currentProgress = models.IntegerField(default=0)
    description = models.TextField()
    dueDate = models.CharField(max_length=30, blank=True)
    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("urgent", "Urgent"),
    ]
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default="medium")
    color = models.CharField(max_length=7, default="#000000")
    assignedTo = models.JSONField(default=list)
    subtasks = models.JSONField(default=list)

    def __str__(self):
        return f"{self.title} {self.category} {self.priority}"


class Users(models.Model):
    userId = models.CharField(max_length=30, blank=True)


class SummaryDetails(models.Model):
    taskInBoard = models.IntegerField(default=0)
    taskInToDo = models.IntegerField(default=0)
    taskInDone = models.IntegerField(default=0)
    taskInProgress = models.IntegerField(default=0)
    taskInFeedback = models.IntegerField(default=0)
    urgendTaskUpcoming = models.JSONField(default=list)