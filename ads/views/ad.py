from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from ads.models import Ad
from ads.permissions.permissions import AdUpdatePermission
from ads.serializers.ad import AdListSerializer, AdDetailSerializer, AdCreateSerializer, AdUpdateSerializer, \
    AdDestroySerializer


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


class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdUpdateSerializer
    permission_classes = [IsAuthenticated, AdUpdatePermission]


class AdDeleteView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDestroySerializer
    permission_classes = [IsAuthenticated, AdUpdatePermission]


@api_view(["POST"])
@permission_classes([IsAuthenticated, AdUpdatePermission])
def ad_upload_image_view(request, pk):
    obj = Ad.objects.get(pk=pk)
    obj.image = request.FILES.get("image", None)
    obj.save()

    return JsonResponse({
        "id": obj.id,
        "name": obj.name,
        "author_id": obj.author_id,
        "author": obj.author.first_name,
        "price": obj.price,
        "description": obj.description,
        "is_published": obj.is_published,
        "category_id": obj.category_id,
        "image": obj.image.url if obj.image else None
    })
