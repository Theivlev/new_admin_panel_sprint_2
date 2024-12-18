from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView

from movies.models import FilmWork


class MoviesApiMixin:
    
    model = FilmWork
    http_method_names = ['get']

    @property
    def queryset(self):
        """
        Базовый набор данных о фильмах.
        Возвращает только необходимые поля из FilmWork с предзагрузкой связанных данных.
        """
        return FilmWork.objects.prefetch_related('genres', 'persons').values(
            'id',
            'title',
            'description',
            'rating',
            'type',
            'creation_date'
        )

    def get_persons_by_role(self, role):
        """
        Получает список полных имен участников по заданной роли.
        """
        return ArrayAgg(
            'persons__full_name',
            distinct=True,
            filter=Q(personfilmwork__role=role)
        )

    def get_queryset(self):
        """
        Возвращает аннотированный набор данных о фильмах.
        Агрегирует жанры и участников по ролям (актеры, режиссеры, сценаристы).
        """
        genres = ArrayAgg(
            'genres__name',
            distinct=True
        )
        roles = ['actor', 'director', 'writer']
        annotations = {role: self.get_persons_by_role(role) for role in roles}

        return self.queryset.annotate(
            genres=genres,
            **annotations
        )

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)


class MoviesListApi(MoviesApiMixin, BaseListView):
    model = FilmWork

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', 50)

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = self.get_queryset()
        paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, self.get_paginate_by(queryset))
        context = {
            'count': paginator.count,
            'total_pages': paginator.num_pages,
            'prev': page.previous_page_number() if page.has_previous() else None,
            'next': page.next_page_number() if page.has_next() else None,
            'results': list(queryset),
        }
        return context


class MoviesDetailApi(MoviesApiMixin, BaseDetailView):
     def get_context_data(self, **kwargs):
        return kwargs['object']
