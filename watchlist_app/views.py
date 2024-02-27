# from django.shortcuts import render
# from .models import Movie
# from django.http import JsonResponse
# # Create your views here.


# def movie_list(request):
#     movies=Movie.objects.all()
#     data= {
#         'movie':list(movies.values())
#     }
#     return JsonResponse(data)

# def movie_detail(request,movie_id):
    
#     movie=Movie.objects.get(pk=movie_id)
    
#     data= {
#        'movie':movie.name,
#        'description':movie.description,
#        'active':movie.active,
#     }
#     return JsonResponse(data)