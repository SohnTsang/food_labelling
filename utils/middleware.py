from django.utils import translation

class AdminLocaleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if current path is for the Django admin
        if request.path.startswith('/admin/'):
            # Set language to English for admin
            translation.activate('en')
            request.LANGUAGE_CODE = 'en'
        response = self.get_response(request)
        return response


class CreateLabelMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if current path is for the Django admin
        if request.path.startswith('/label-management/create-label/'):
            # Set language to English for admin
            translation.activate('ja')
            request.LANGUAGE_CODE = 'ja'
        response = self.get_response(request)
        return response