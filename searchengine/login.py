import os
import jwt
import datetime
import bcrypt
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .database.create_connection import get_db_connection

SECRET_KEY = os.getenv('SECRET_KEY')

@csrf_exempt
@require_POST
def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    if not username or not password:
        return JsonResponse({'error': 'Username and password are required'}, status=400)

    conn = get_db_connection()
    if not conn:
        return JsonResponse({'error': 'Database connection failed'}, status=500)

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, password, email FROM users WHERE username=%s", (username,))
        user = cursor.fetchone()
        if not user:
            return JsonResponse({'error': 'Invalid username or password'}, status=401)

        user_id, hashed_password, email = user

        if not bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
            return JsonResponse({'error': 'Invalid username or password'}, status=401)

        # Generate JWT token
        payload = {
            'username': username,
            'email': email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        # Optionally update the token in DB
        cursor.execute("UPDATE users SET Token=%s WHERE id=%s", (token, user_id))
        conn.commit()

        return JsonResponse({'message': 'Login successful', 'token': token}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    finally:
        conn.close()