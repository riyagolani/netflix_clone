from django.urls import path
from core.views import Home, ProfileList, ProfileCreate, Watch, ShowMovieDetail, PlayMovie


urlpatterns = [
    path('', view=Home.as_view()),
    path('profile/', view=ProfileList.as_view(), name="profile_list"),
    path('profile/create/', view=ProfileCreate.as_view(), name="profile_create"),
    path('watch/<profile_id>/', view=Watch.as_view(), name="watch"),
    path('movie/<movie_id>', view=ShowMovieDetail.as_view(), name="show_det"),
    path('movie/play/<movie_id>', view=PlayMovie.as_view(), name='play'),
]
