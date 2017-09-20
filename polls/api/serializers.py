from rest_framework import serializers
from polls.models import Question,Choice

class Questionserializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		fields = [
			'question_text',
			'pub_date',
		]


class Choiceserializer(serializers.ModelSerializer):
	class Meta:
		model = Choice
		fields = [
			'choice_text',
			'votes',
		]
