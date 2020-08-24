
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import * #PostViewSet, TestCaseViewSet, TagViewSet, showLog, executeSuite, getFileTreeList, saveSuiteFile
app_name = 'blog'
router = DefaultRouter()
router.register(r'show_books', PostViewSet)
router.register(r'show_testcases', TestCaseViewSet)
router.register(r'show_tags', TagViewSet)
urlpatterns = [
    #path('', views.index, name='index'),
    #path('show_books', views.getAllBooks, name='showBooks')
    path(r'api/', include(router.urls)),
    path(r'api/show_log/', showLog, name='test'),
    path(r'api/execute_suite/', executeSuite, name='execute'),
    path(r'api/getFileTreeList/', getFileTreeList, name='getFileTreeList'),
    path(r'api/getFileContent/', getFileContent, name='getFileContent'),
    path(r'api/saveSuiteFile/', saveSuiteFile, name='saveSuiteFile'),
    path(r'api/saveRawFile/', saveRawFile, name='saveRawFile')
]
