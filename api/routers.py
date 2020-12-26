from rest_framework import routers
from api.views import CategoryApiView,ProductApiview, LinkMapperApiview, LinkStatsApiview

router = routers.DefaultRouter()
router.register('catergory', CategoryApiView)
router.register('link', LinkMapperApiview)
router.register('product', ProductApiview)
router.register('linkstats', LinkStatsApiview)

