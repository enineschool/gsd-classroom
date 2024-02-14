from django.contrib import admin
from django.shortcuts import reverse
from django.utils.html import format_html

from .models import (
    Faculty,
    Content,
    Program,
    Course,
    Student,
    Assignment,
    StudentAssignment,
)


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    fields = (
        "id",
        "user",
        "github",
        "is_active",
    )
    readonly_fields = ("id",)
    list_display = fields + ("_courses", "_programs", "_graded")

    @admin.display(description="Courses")
    def _courses(self, obj):
        courses = obj.courses()

        html = (
            "<div>"
            f'<a href="#" data-bs-toggle="dropdown">'
            f"{courses.count()}"
            f'<ul class="dropdown-menu">'
        )
        for course in courses:
            html += (
                f'<li class="dropdown-item">'
                f'<a href="'
                f'{reverse("admin:voyage_course_change", args=[course.id])}'
                f'">{course.name}</li>'
            )
            print(html)
        return format_html(html)

    @admin.display(description="Programs")
    def _programs(self, obj):
        programs = obj.programs()
        program_idstr = [x.id for x in programs]
        if program_idstr:
            program_idstr = ",".join([str(x) for x in program_idstr])
        print(program_idstr)
        # print(program_ids)

        html = "<div>" f"<a href=" f'{reverse("admin:voyage_program_changelist")}'
        if program_idstr:
            html += f"?id__in={program_idstr}"
        html += f">{obj.programs().count()}</a>"
        return format_html(html)

    @admin.display(description="Graded")
    def _graded(self, obj):
        return obj.assignments_graded().count()


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    pass


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    pass


@admin.register(StudentAssignment)
class StudentAssignmentAdmin(admin.ModelAdmin):
    pass
