
class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("--------------------------------------------------------------------------")
        print(f"| Request URL: {request.path} - User: {request.user} - Method: {request.method} - MIDDLEWARE POSTEOS |")
        response = self.get_response(request) # en este punto comienza la respuesta de la vista
        print(f"|     Response: {response}|")
        print("--------------------------------------------------------------------------")
        return response
         