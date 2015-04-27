from django.contrib import admin

# Register your models here.

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionModelAdmin(admin.ModelAdmin):
	# 	fields = ['published_date','question_text',]

	fieldsets = [ ('Question group', { 'fields' : ['question_text'] }),
								('Date information', { 'fields' : ['published_date'], 'classes' : ['collapse']})
								]

	inlines = [ChoiceInline]

	list_display = ['question_text', 'published_date', 'was_published_recently']

	list_filter = ['published_date']

	search_fields = ['question_text']


class ChoiceModelAdmin(admin.ModelAdmin):
	list_display = ['choice_text', 'votes']


admin.site.register(Question, QuestionModelAdmin)

admin.site.register(Choice, ChoiceModelAdmin)
