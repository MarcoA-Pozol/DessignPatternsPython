import random

# Step 1: Component Interface
class Handler():
    def handle(self):
        pass

# Step 2: Concrete Component
class Request(Handler):
    def handle(self):
        methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']
        method = random.choice(methods)
        print(f'Sending HTTP Request [{method}] ᯓ➤')
        return {'method': method, 'data': 'Example response data'} 

# Step 3: Decorator (abstract)
class HandlerDecorator(Handler):
    def __init__(self, handler:Handler):
        self.handler = handler
    
    def handle(self):
        self.handler.handle()

# Step 4: Concrete Decorators
class HttpErrorHandler(HandlerDecorator):
    def handle(self):
        try:
            response = self.handler.handle()
            print('Executed request ✅')
            return response
        except Exception as e:
            print(f'Failed request ({e}) ❌')

class CacheResponseDataHandler(HandlerDecorator):
    def handle(self):
        response = self.handler.handle()
        print('Stored response data in cache 💾')
        return response

# Step 5: Client Code
if __name__ == '__main__':
    request = Request()
    cache_response_data = CacheResponseDataHandler(request)
    manage_http_errors = HttpErrorHandler(cache_response_data)
    print(manage_http_errors.handle())