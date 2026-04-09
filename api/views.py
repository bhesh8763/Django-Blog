from django.shortcuts import render
from django.http import JsonResponse

from home.models import Article
from .serializers import ArticleSerializer
import json
# Create your views here.
def index(request):
    
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    message = {
        'message': 'Welcome to the API',
        'status': 'success',
        'code': 200,
        'articles': serializer.data
    }
    return JsonResponse(message, safe=False)

from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_POST



@csrf_exempt
@require_POST
# def create(request):
#     try:
#         data = json.loads(request.body)  # ✅ Parse raw JSON body
#     except json.JSONDecodeError:
#         return JsonResponse({'message': 'Invalid JSON', 'status': 'error', 'code': 400}, status=400)

#     article = Article.objects.create(
#         title=data.get('title'),
#         content=data.get('content')
#     )
#     serializer = ArticleSerializer(article)
#     return JsonResponse({
#         'message': 'Article created successfully',
#         'status': 'success',
#         'code': 201,
#         'data': serializer.data
#     }, status=201)
def create(request):
    if request.method == 'POST':
        data = request.POST
        article = Article.objects.create(
            title=data.get('title'), 
            content=data.get('content'))
        serializer = ArticleSerializer(article)
        message = {
            'message': 'Article created successfully',
            'status': 'success',
            'code': 201,
            'data': serializer.data
        }
        return JsonResponse(message, safe=False)

    

def detail(request, slug):
    objects = Article.objects.filter(slug=slug).first()
    serializer = ArticleSerializer(objects)

    return JsonResponse(serializer.data, safe=False)

def delete(request, slug):
    return JsonResponse({"message": f"Delete endpoint for {slug}"})