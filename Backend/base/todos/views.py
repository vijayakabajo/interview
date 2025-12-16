from django.shortcuts import render
from todos.models import Todos
from rest_framework.views import APIView
from django.http import JsonResponse

class TodosView(APIView):
    def get(self, request):
        response = {
            'status': True,
            'message': 'success',
            'data': []
        }
        todos_id = request.GET.get('todo_id')
        if not todos_id:
            response['status'] = False
            response['message'] = 'todo_id is required'
            return JsonResponse(response)
        
        todos = Todos.objects.filter(id=todos_id).first()

        if todos:
            response['data'].append({
                'id': todos.id,
                'title': todos.title,
                'content': todos.content,
                'is_done': todos.is_done
            })

        return JsonResponse(response)
    
    def post(self, request):
        response = {
            'status': True,
            'message': 'success'
        }
        user_id = request.data.get('user_id')
        title = request.data.get('title')
        content = request.data.get('content')

        if not title or not content:
            response['status'] = False
            response['message'] = 'title and content are required'
            return JsonResponse(response)

        Todos.objects.create(
            user_id=user_id,
            title=title,
            content=content
        )

        return JsonResponse(response)
    
    def patch(self, request):
        response = {
            'status': True,
            'message': 'success'
        }

        todo_id = request.data.get('todo_id')
        is_done = request.data.get('is_done')
        title = request.data.get('title')
        content = request.data.get('content')

        if not todo_id:
            response['status'] = False
            response['message'] = 'todo_id required'
            return JsonResponse(response)
        
        if title:
            Todos.objects.filter(id=todo_id).update(title=title)
        
        if content:
            Todos.objects.filter(id=todo_id).update(content=content)

        Todos.objects.filter(id=todo_id).update(is_done=is_done)

        return JsonResponse(response)
    
    def delete(self, request):
        response = {
            'status': True,
            'message': 'success'
        }

        todo_id = request.data.get('todo_id')

        if not todo_id:
            response['status'] = False
            response['message'] = 'todo_id required'
            return JsonResponse(response)
        
        Todos.objects.filter(id=todo_id).delete()

        return JsonResponse(response)
    
class todosListView(APIView):
    permission_classes = []

    def get(self, request):
        response = {
            'status': True,
            'message': 'success',
            'data': []
        }

        todos = Todos.objects.all()

        for todo in todos:
            response['data'].append({
                'id': todo.id,
                'title': todo.title,
                'content': todo.content,
                'is_done': todo.is_done
            })

        return JsonResponse(response)
    

        
