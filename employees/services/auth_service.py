import requests

class AuthService:
    BASE_URL = 'http://your-backend-url/api'  # Replace with your backend URL

    @staticmethod
    def signup_user(username, email, password):
        try:
            response = requests.post(
                f'{AuthService.BASE_URL}/signup/',
                json={
                    'username': username,
                    'email': email,
                    'password': password
                }
            )
            return response.json()
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}

    @staticmethod
    def signin_user(username, password):
        try:
            response = requests.post(
                f'{AuthService.BASE_URL}/login/',
                json={
                    'username': username,
                    'password': password
                }
            )
            return response.json()
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}