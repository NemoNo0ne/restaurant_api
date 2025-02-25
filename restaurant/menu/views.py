from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import models
from .models import FoodCategory, Food
from .serializers import FoodListSerializer
from rest_framework.exceptions import NotFound

class FoodCategoryListView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            categories = FoodCategory.objects.prefetch_related(
                models.Prefetch("food", queryset=Food.objects.filter(is_publish=True))
            ).filter(food__is_publish=True).distinct()

            if not categories:
                raise NotFound("Категории не найдены.")

            serializer = FoodListSerializer(categories, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
