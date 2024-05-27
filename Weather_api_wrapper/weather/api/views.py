<<<<<<< HEAD
import requests
from django.http import JsonResponse
from django.conf import settings
from django.core.cache import cache_page


@cache_page(60 * 15)
def get_weather(request):
    

    # Retrieve API key from environment variable
    api_key = settings.VISUAL_CROSSING_API_KEY
    city = request.GET.get('city')

    # Make request to Visual Crossing API with the provided city
    api_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=us&key={api_key}&contentType=json"
    #api_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Herndon,VA?unitGroup=us&key={api_key}&include=days&elements=datetime,moonphase,sunrise,sunset,moonrise,moonset"
    response = requests.get(api_url)

    # Check if request was successful
    if response.status_code == 200:
        # Parse JSON response
        data = response.json()

        # Extract weather information from response
        weather_info = {
            'city': city,
            'weather': data['days'][0]['conditions']
        }
        return JsonResponse(weather_info)
    else:
        # Handle error if request fails
        return JsonResponse({'error': 'Failed to retrieve weather information'}, status=500)
=======
from django.shortcuts import render
from django
# Create your views here.
>>>>>>> ada43e41de69b6c16be1a789b1872d6f90731e68
