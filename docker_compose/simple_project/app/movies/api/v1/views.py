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

    def get_queryset(self):
        """
        Возвращает аннотированный набор данных о фильмах.
        Агрегирует жанры и участников по ролям (актеры, режиссеры, сценаристы).
        """
        genres = ArrayAgg(
            'genres__name',
            distinct=True
        )
        actors = ArrayAgg(
            'persons__full_name',
            distinct=True,
            filter=Q(personfilmwork__role='actor')
        )
        directors = ArrayAgg(
            'persons__full_name',
            distinct=True,
            filter=Q(personfilmwork__role='director')
        )
        writers = ArrayAgg(
            'persons__full_name',
            distinct=True,
            filter=Q(personfilmwork__role='writer')
        )

        return self.queryset.annotate(
            genres=genres,
            actors=actors,
            directors=directors,
            writers=writers
        )

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)


class MoviesListApi(MoviesApiMixin, BaseListView):
    model = FilmWork

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {
            'results': list(self.get_queryset()),
        }
        return context


class MoviesDetailApi(MoviesApiMixin, BaseDetailView):
    def get_context_data(self, **kwargs):
        return  # Словарь с данными объекта
