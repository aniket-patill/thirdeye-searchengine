import os
import jwt
import datetime
import bcrypt 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .database.create_connection import get_db_connection

SECRET_KEY = os.getenv('SECRET_KEY')  # Load from .env

@csrf_exempt
@require_POST
def register_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')

    if not username or not password or not email:
        return JsonResponse({'error': 'All fields are required'}, status=400)

    conn = get_db_connection()
    if not conn:
        return JsonResponse({'error': 'Database connection failed'}, status=500)

    try:
        cursor = conn.cursor()
        # Check if user exists
        cursor.execute("SELECT id FROM users WHERE username=%s OR email=%s", (username, email))
        if cursor.fetchone():
            return JsonResponse({'error': 'Username or email already exists'}, status=409)
        
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        # Generate JWT token
        payload = {
            'username': username,
            'email': email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        # Insert new user with token
        cursor.execute(
            "INSERT INTO users (username, password, email, Token) VALUES (%s, %s, %s, %s)",
            (username, hashed_password, email, token)
        )
        conn.commit()

        return JsonResponse({'message': 'User registered successfully', 'token': token}, status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    finally:
        conn.close()