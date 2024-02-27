from rest_framework.response import Response
from ..models import Movie
from .serializers import MovieSerializers
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

class MovieListAV(APIView):
    def get(self,request):
        movies = Movie.objects.all()
        serializer = MovieSerializers(movies,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self,request):
        serializer = MovieSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class MovieDetailAV(APIView):
    def get(self,request,pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({"message": "Movie not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = MovieSerializers(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self,request,pk):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializers(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response({"message": "Movie deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    

# @api_view(['GET','POST',])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializers(movies,many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer =MovieSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
    
#         return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)  
# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):
#     try:
#         movie = Movie.objects.get(pk=pk)
#     except Movie.DoesNotExist:
#         return Response({"message": "Movie not found."}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = MovieSerializers(movie)
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response({"message": "Movie deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
#     elif request.method == 'PUT':
#         serializer = MovieSerializers(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)