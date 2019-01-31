from rest_framework import routers
from .viewsets import *

router = routers.DefaultRouter()
router.register("tags", TagViewset)
router.register("bloglist", BlogListViewset, "bloglist")
router.register("blogs", BlogViewset)
router.register("comments", CommentViewset)
