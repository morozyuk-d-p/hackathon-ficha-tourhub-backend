from ninja import NinjaAPI
from maps.api import router as MapsRouter

api = NinjaAPI(title='TourHub')

api.add_router(prefix='maps', router=MapsRouter)