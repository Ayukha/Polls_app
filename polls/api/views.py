from rest_framework.generics import ListAPIView

from polls.models import Question , Choice
from .serializers import Questionserializer , Choiceserializer




class QuestionListAPIView(ListAPIView):
	queryset = Question.objects.all()
	serializer_class = Questionserializer


class ChoiceListAPIView(ListAPIView):
	queryset = Choice.objects.all()
	serializer_class = Choiceserializer