from django.contrib import admin
from analyzer.models import Feedback

# Register your models here.
class FeedbackModelAdmin(admin.ModelAdmin):
    model = Feedback
    list_display = ['name','age','q1s','q2s','q3s','q4s']


admin.site.register(Feedback,FeedbackModelAdmin)