import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, UpdateView, DeleteView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from ads.models import Category
from ads.permissions.permissions import CategoryCreatePermission
from ads.serializers.category import CategoryCreateSerializer


class CategoriesListView(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        object_list = self.object_list.order_by("name")

        response = []
        for item in object_list:
            response.append({
                "id": item.id,
                "name": item.name,
            })

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def category_detail_views(request, pk):
    category = Category.objects.get(pk=pk)

    return JsonResponse({
        "id": category.id,
        "name": category.name
    }, json_dumps_params={"ensure_ascii": False})


class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer
    permission_classes = [IsAuthenticated, CategoryCreatePermission]


@method_decorator(csrf_exempt, name="dispatch")
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ["name"]

    def patch(self, reguest, *args, **kwargs):
        super().post(reguest, *args, **kwargs)
        category_data = json.loads(reguest.body)

        self.object.name = category_data["name"]

        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name
        }, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)
