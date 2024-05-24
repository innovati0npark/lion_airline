from django.core.paginator import Paginator
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from app.models import Flights



@api_view(["GET"])
def get_flights(request):
    page = request.GET.get('page', 1)
    limit = request.GET.get('limit', 10)

    flights = Flights.objects.all()
    paginator = Paginator(flights, limit)
    page_obj = paginator.get_page(page)

    response = {
        "totalItems": paginator.count,
        "totalPages": paginator.num_pages,
        "currentPage": page,
        "flights": list(page_obj.object_list.values(
            "id", "departure", "departure_airport", "departure_airport_code", 
            "destination", "destination_airport", "destination_airport_code", 
            "departure_date", "destination_date", "departure_time", 
            "destination_time", "duration", "airline", "flightClass", "price"
        ))
    }

    return JsonResponse(response)