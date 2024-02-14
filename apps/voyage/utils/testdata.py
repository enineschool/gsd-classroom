import random

from django.contrib.auth import get_user_model
from django.db import IntegrityError

from ..models import (
    Faculty,
    Student,
    Program,
    Course,
    Content,
    Assignment,
    StudentAssignment,
)
from ..sandbox.randgen import random_userdata


def create_random_users(count=100):
    result = [create_random_user() for _ in range(count)]
    return result


def create_random_user():
    obj_exists = False
    usermodel = get_user_model()
    obj = None
    while not obj_exists:
        random_data = random_userdata()
        obj_exists = usermodel.objects.filter(username=random_data["username"]).exists()
        if not obj_exists:
            obj = usermodel.objects.create_user(**random_data)
            obj_exists = True if obj else False

    return obj


def create_random_data():
    usermodel = get_user_model()
    create_random_users()

    appmodels = {
        Faculty: 20,
        Program: 4,
        Course: 4,
        Content: 8,
        Assignment: 4,
        Student: 40,
        StudentAssignment: 40,
    }
    for appmodel, item_count in appmodels.items():
        for _ in range(item_count):
            obj = appmodel()
            obj.randomize()

            if hasattr(obj, "user_id"):
                if appmodel == Faculty:
                    available_users = usermodel.objects.filter(faculty=None)
                elif appmodel == Student:
                    available_users = usermodel.objects.filter(student=None)
                else:
                    available_users = usermodel.objects.none()
                user = random.choice(available_users)
                setattr(obj, "user_id", user.id)

            try:
                obj.save()
            except IntegrityError:
                print(f"{appmodel}: IntegrityError")


if __name__ == "__main__":
    create_random_data()
