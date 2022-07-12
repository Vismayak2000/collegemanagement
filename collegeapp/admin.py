from django.contrib import admin
from collegeapp.models import CourseModel,Usermember
# Register your models here.


@admin.register(CourseModel)
class CourseDetailAdmin(admin.ModelAdmin):
    list_display=('id','Course_Name','Course_Fees')

@admin.register(Usermember)
class TeacherDetailAdmin(admin.ModelAdmin):
    list_display=('id','Teacher_Address','Teacher_Age','Teacher_gender','Teacher_image')

