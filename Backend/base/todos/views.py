from django.utils import timezone
from django.shortcuts import render
from todos.models import Todos
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from accounts.authentication import CustomJWTAuthentication
from accounts.permissions import IsCustomAuthenticated
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework import generics
from django.db.models import Q


# Create your views here.
class TodosView(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsCustomAuthenticated]

    def get(self, request):

        # print("user_id:",request.user.id)
        user_id = request.user.id

        response = {
            'status': True,
            'message': 'success',
            'data': None,
            'error': None
        }
        todos_id = request.GET.get('todo_id')
        if not todos_id:
            response['status'] = False
            response['message'] = 'todo_id is required'
            return JsonResponse(response)
        
        todos = Todos.objects.filter(
            id=todos_id,
            user_id=user_id,
            is_active=True
        ).first()

        if todos:
            response['data'] = {
                'id': todos.id,
                'title': todos.title,
                'content': todos.content,
                'is_done': todos.is_done
            }
        else:
            response['status'] = False
            response['message'] = 'todo not found'

        return JsonResponse(response)
    
    def post(self, request):
        response = {
            'status': True,
            'message': 'success',
            'data': None,
            'error': None
        }
        user_id = request.user.id
        title = request.data.get('title')
        content = request.data.get('content')

        if not title or not content:
            response['status'] = False
            response['message'] = 'title and content are required'
            return JsonResponse(response)

        Todos.objects.create(
            user_id=user_id,
            title=title,
            content=content,
            is_done=False,
            is_active=True
        )

        return JsonResponse(response)
    
    def patch(self, request):
        response = {
            'status': True,
            'message': 'success',
            'data': None,
            'error': None
        }
        user_id = request.user.id
        todo_id = request.data.get('todo_id')
        is_done = request.data.get('is_done')
        title = request.data.get('title')
        content = request.data.get('content')


        if not todo_id:
            response['status'] = False
            response['message'] = 'todo_id required'
            return JsonResponse(response)
        
        qs = Todos.objects.filter(
            id=todo_id,
            user_id=user_id,
            is_active=True,
            deleted_at__isnull=True
        )

        if title is not None:
            qs.update(title=title)
        
        if content is not None:
            qs.update(content=content)

        if is_done is not None:
            qs.update(is_done=is_done)

        return JsonResponse(response)
    
    def delete(self, request):
        response = {
            'status': True,
            'message': 'success',
            'data': None,
            'error': None
        }

        # delete_type = request.data.get('type') #soft or hard

        todo_id = request.GET.get('todo_id')

        if not todo_id:
            response['status'] = False
            response['message'] = 'todo_id required'
            return JsonResponse(response)
        try:
            todo_to_del = Todos.objects.filter(
                id=todo_id,
                user_id=request.user.id
            )
            todo_to_del.update(
                is_active=False,
                deleted_at=timezone.now()
            )
            response['message'] = 'todo deleted successfully'
        except Exception as e:
            response['status'] = False
            response['message'] = 'error deleting todo'
            response['error'] = str(e)

        return JsonResponse(response)


#LIST----------------------------------------------

class TodosListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todos
        fields = ['id', 'title', 'content', 'is_done']

class TodosPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50


class TodosListView(generics.ListAPIView):
    serializer_class = TodosListSerializer
    pagination_class = TodosPagination
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsCustomAuthenticated]

    def get_queryset(self):
        
        user_id = self.request.user.id

        qs = Todos.objects.filter(
            user_id=user_id,
            is_active=True,
            deleted_at__isnull=True
        ).only(
            "id", "title", "content", "is_done", "created_at"
        ).order_by("-created_at")

        qp = self.request.query_params

        is_done = qp.get("is_done")
        if is_done is not None:
            is_done = str(is_done).lower() in ("true", "1")
            qs = qs.filter(is_done=is_done)

        search = qp.get("search")
        if search is not None:
            qs = qs.filter(
                Q(title__icontains=search) |
                Q(content__icontains=search)
            )

        return qs
