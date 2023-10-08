from django.contrib import admin
from About_Us.models import Teachers
# Register your models here.

class TeachersAdmin(admin.ModelAdmin):
    list_display = ('id', 'teacher_id', 'teacher_name', 'teacher_email')


admin.site.register(Teachers, TeachersAdmin)



