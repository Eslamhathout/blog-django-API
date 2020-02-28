from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from myblog.models import Article
from myblog.api.serializers import articleSerializer, UserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework import generics, viewsets
from django.contrib.auth.models import User
from rest_framework import permissions
from myblog.api.permissions import IsOwnerOrReadOnly

#Root View
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user_list', request=request, format=format),
        'articles': reverse('article_list', request=request, format=format)
    })

#Using viewsets
#It provide the read only and can replace both UserList, and UserDetail.
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = articleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # The create() method of our serializer will now be passed an additional 'owner' field, along with the validated data from the request.
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  


# #Using generic class based views
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class ArticleList(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = articleSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

#     # The create() method of our serializer will now be passed an additional 'owner' field, along with the validated data from the request.
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)


# class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = articleSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


# #Solution using regular function based views
# @csrf_exempt
# def article_list(request):
#     if request.method == "GET":
#         #Bring all the objects
#         articles = Article.objects.all()
#         #serialize the objects
#         serializer = articleSerializer(articles, many=True)
#         #return the serialized object
#         return JsonResponse(serializer.data, safe=False)

    
#     elif request.method == "POST":
#         #read the serialized data and convert it to JSON
#         data = JSONParser().parse(request)
#         #Convert JSON data to articleSerializer 
#         serializer = articleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# @csrf_exempt
# def article_detail(request, pk):
#     try: 
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return HttpResponse(reason="Sorry we can't find your article!!",status=404)

#     if request.method=="GET":
#         serializer = articleSerializer(article)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method=="DELETE":
#         article.delete()
#         return HttpResponse(status=204)
    
#     elif request.method=="PUT":
#         data = JSONParser().parse(request)
#         serializer = articleSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)





#2-Second solution using function based views, api-views decorators, built-in Response-Request-Status
# @api_view(['GET', 'POST'])
# def article_list(request):
#     if request.method == "GET":
#         #Bring all the objects
#         articles = Article.objects.all()
#         #serialize the objects
#         serializer = articleSerializer(articles, many=True)
#         #return the serialized object
#         return Response(serializer.data)

    
#     elif request.method == "POST":
#         #Convert JSON data to articleSerializer 
#         serializer = articleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def article_detail(request, pk):
#     try: 
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return Response(reason="Sorry we can't find your article!!",status=404)

#     if request.method=="GET":
#         serializer = articleSerializer(article)
#         return Response(serializer.data)

#     elif request.method=="DELETE":
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
#     elif request.method=="PUT":
#         serializer = articleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)