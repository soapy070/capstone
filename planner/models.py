from django.db import models
from django.contrib.auth.models import Group


class Location(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Team(models.Model):
    name = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='teams_managed_by')
    manager = models.ForeignKey('Manager', on_delete=models.CASCADE, related_name='teams', null=True)

    def __str__(self):
        return f"{self.name}"


class Member(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255, default='Member')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='members')
    start_date = models.DateField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members', null=True)
    manager = models.ForeignKey('Manager', on_delete=models.CASCADE, related_name='members', null=True)
    groups = models.ManyToManyField(Group, blank=True)

    def __str__(self):
        return f"{self.name}"


class Manager(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255, default='Manager')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='managers')
    start_date = models.DateField()
    groups = models.ManyToManyField(Group, blank=True)

    def __str__(self):
        return f"{self.name}"