from typing import List
from ninja import Router
from ninja.orm import create_schema
from .models import Location

router = Router(tags=['maps'])

@router.get('locations', response=List[create_schema(Location)])
def location_list(request):
    return Location.objects.all()