from django.db import models


class SQLToAST(models.Model):
    original_query = models.CharField(max_length=10000)
    ast = models.CharField(max_length=10000, null=True, blank=True)
    modified_query = models.CharField(max_length=10000, null=True, blank=True)
    hashed_values = models.CharField(max_length=10000, null=True, blank=True)

    def __str__(self):
        return self.original_query

    class Meta:
        db_table = 'API_SQLToAST'
