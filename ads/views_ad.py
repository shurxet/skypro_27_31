import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView, DeleteView

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from ads.models import Ad, Category

from ads.serializers import AdListSerializer, AdDetailSerializer, AdCreateSerializer
from authentication.models import User


def root_domain(request):
    return JsonResponse({"status": "ok"})




class AdsListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer

    def get(self, request, *args, **kwargs):
        ad_cat = request.GET.get('cat', None)
        if ad_cat:
            self.queryset = self.queryset.filter(category__id__in=ad_cat)
        ad_text = request.GET.get('text', None)
        if ad_text:
            self.queryset = self.queryset.filter(name__icontains=ad_text)
        ad_location = request.GET.get('location', None)
        if ad_location:
            self.queryset = self.queryset.filter(author__location__name__icontains=ad_location)

        price_from = request.GET.get('price_from', None)
        price_to = request.GET.get('price_to', None)
        if price_from:
            self.queryset = self.queryset.filter(price__gte=int(price_from))
        if price_to:
            self.queryset = self.queryset.filter(price__lte=int(price_to))

        return super().get(self, request, *args, **kwargs)


class AdDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer
    permission_classes = [IsAuthenticated]


class AdCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerializer
    permission_classes = [IsAuthenticated]


@method_decorator(csrf_exempt, name="dispatch")
class AdUpdateView(UpdateView):
    model = Ad
    fields = ["name", "author", "price", "description", "is_published", "category"]

    def patch(self, reguest, *args, **kwargs):
        super().post(reguest, *args, **kwargs)
        ad_data = json.loads(reguest.body)

        self.object.name = ad_data["name"]
        self.object.price = ad_data["price"]
        self.object.description = ad_data["description"]
        self.object.is_published = ad_data["is_published"]
        self.object.author = get_object_or_404(User, pk=ad_data["author_id"])
        self.object.category = get_object_or_404(Category, pk=ad_data["category_id"])

        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author_id": self.object.author_id,
            "author": self.object.author.first_name,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "category_id": self.object.category_id,
            "image": self.object.image.url if self.object.image else None
        })


@method_decorator(csrf_exempt, name="dispatch")
class AdDeleteView(DeleteView):
    model = Ad
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class AdUploadImageView(UpdateView):
    model = Ad
    fields = ("image",)

    def ad_upload_image_view(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.image = request.FILES.get("image", None)
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author_id": self.object.author_id,
            "author": self.object.author.first_name,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "category_id": self.object.category_id,
            "image": self.object.image.url if self.object.image else None
        })
