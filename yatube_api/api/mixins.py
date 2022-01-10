from rest_framework import mixins, viewsets


class CreateListViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    """Собираем ViewSet для Follow."""
    pass
