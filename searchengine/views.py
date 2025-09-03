
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
# @csrf_exempt
# def register(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         email = request.POST.get('email')

#         print(f"Received registration data: username={username}, email={email}")

#         return JsonResponse({'message': 'User registered successfully'}, status=201)
#     else:
#         return JsonResponse({'error': 'Invalid request method'}, status=405)
