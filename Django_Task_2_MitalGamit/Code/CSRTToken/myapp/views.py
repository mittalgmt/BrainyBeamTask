from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from myapp.models import MyData

@csrf_exempt
def save_data(request):
    token = request.headers.get('Authorization')
    if not token or token != settings.MY_SECRET_TOKEN:
        return JsonResponse({'error': 'Unauthorized'}, status=401)

    if request.method == 'POST':
        data = request.POST.get('data')
        if data:
            MyData.objects.create(data=data)
            return JsonResponse({'message': 'Data saved successfully'}, status=201)
        else:
            return JsonResponse({'error': 'No data provided'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
