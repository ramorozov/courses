from tastypie.authentication import ApiKeyAuthentication

'''Измененный класс авторизации. Допускает GET запрос без аутентификации'''
class CustomAuthentication(ApiKeyAuthentication):
    def is_authenticated(self, request, **kwargs):
        if request.method == 'GET':
            return True
               
        return super().is_authenticated(request, **kwargs)
