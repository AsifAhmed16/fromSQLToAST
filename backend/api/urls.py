from django.urls import path

from .views import ASTToSQLViewSet, SQLToASTViewSet

app_name = 'api'

urlpatterns = [
    path('sqltoast/', SQLToASTViewSet.as_view({
        'post': 'create'
    })),
    path('asttosql/', ASTToSQLViewSet.as_view({
        'post': 'recreate'
    })),
]
