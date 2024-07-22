from django.shortcuts import render
from django.utils import timezone
from .models import Post,Item
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ItemSerializer,PostSerializer

@api_view(['GET'])
def getData(request):
    person={'message':'Hello'}
    return Response(person)

@api_view(['POST'])
def addData(request):
    data=request.data
    serializer=ItemSerializer(data=data)
    print(data)
    if serializer.is_valid():
        serializer.save()
    return Response(data)

@api_view(['POST'])
def add_Blog(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)  # Status code 201 indicates creation success
    return Response(serializer.errors, status=400)  

@api_view(['GET'])
def get_Blog(request):
    posts = Post.objects.all().order_by('published_date')  # Retrieve all posts ordered by published_date
    serializer = PostSerializer(posts, many=True)  # Serialize the queryset
    return Response(serializer.data)  # Return the serialized data

def post_list(request):
    # Retrieve all Post objects, ordered by published_date
    posts = Post.objects.all().order_by('published_date')
    
    # Debug print statement for checking the retrieved posts
    print("Number of posts retrieved:", posts.count())
    for post in posts:
        print(post.title, post.published_date)
        
    # Pass the posts to the template
    return render(request, 'index.html', {'posts': posts})
