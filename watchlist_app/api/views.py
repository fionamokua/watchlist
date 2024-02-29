from rest_framework.response import Response
from ..models import WatchList,StreamingPlartform
from .serializers import WatchListSerializers,StreamingPlatformSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
class StreamingPlartformAV(APIView):
    def get(self,request):
        platform=StreamingPlartform.objects.all()
        serializer = StreamingPlatformSerializer(platform,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self,request):
        serializer = StreamingPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class StreamingPlartformDetailAV(APIView):
    def get(self,request,pk):
        try:
            platform = StreamingPlartform.objects.get(pk=pk)
        except StreamingPlartform.DoesNotExist:
            return Response({"message": "Movie not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamingPlatformSerializer(platform)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self,request,pk):
        platform = StreamingPlartform.objects.get(pk=pk)
        serializer = StreamingPlatformSerializer(platform,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    def delete(self,request,pk):
        platform = StreamingPlartform.objects.get(pk=pk)
        platform.delete()
        return Response({"message": "Movie deleted successfully."}, status=status.HTTP_204_NO_CONTENT) 
        
        
        
class WatchListAV(APIView):
    def get(self,request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializers(movies,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self,request):
        serializer = WatchListSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class WatchDetailAV(APIView):
    def get(self,request,pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({"message": "Movie not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = WatchListSerializers(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self,request,pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchList(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        movie = WatchList.objects.get(pk=pk)
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