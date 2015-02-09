from ratelimitbackend import admin

from .models import CourseStructure


class CourseStructureAdmin(admin.ModelAdmin):
    search_fields = ('course_id', 'version')
    list_display = ('course_id', 'version', 'modified')
    ordering = ('course_id', 'version', '-modified')


admin.site.register(CourseStructure, CourseStructureAdmin)
