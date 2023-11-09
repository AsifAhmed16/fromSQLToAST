import re
import hashlib
import sqlparse
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import SQLToAST
from .serializers import SQLToASTSerializer


def extract_identifier_list(tokens):
    for token in tokens:
        if isinstance(token, sqlparse.sql.IdentifierList):
            return token


def extract_identifiers_from_where(tokens):
    identifiers = []
    for token in tokens:
        if isinstance(token, sqlparse.sql.Identifier):
            identifiers.append(token.get_real_name())
        elif isinstance(token, sqlparse.sql.Comparison):
            identifiers.extend(extract_identifiers_from_where(token.tokens))
    return identifiers


def hash_identifiers(identifiers):
    column_map = {}
    for identifier in identifiers:
        column_map[identifier] = hashlib.sha256(identifier.encode()).hexdigest()
    return column_map


# Function to replace substrings based on a dictionary
def replace_substrings(original, replacements):
    pattern = re.compile(r'\b(?:' + '|'.join(re.escape(k) for k in replacements.keys()) + r')\b')
    replaced_string = pattern.sub(lambda x: replacements[x.group()], original)
    return replaced_string


class SQLToASTViewSet(viewsets.ViewSet):

    def create(self, request):  # /api/sqltoast
        try:
            serializer = SQLToASTSerializer(data=request.data)
            if serializer.is_valid():
                parsed_query = sqlparse.parse(request.data["original_query"])
                instance = serializer.save()
                instance.ast = parsed_query
                identifier_list = extract_identifier_list(parsed_query[0].tokens)
                identifiers = []
                if identifier_list:
                    for each in identifier_list:
                        if str(each) not in ['', ' ', ',']:
                            identifiers.append(str(each))
                # Find the WHERE clause
                where_clause = None
                for token in parsed_query[0].tokens:
                    if isinstance(token, sqlparse.sql.Where):
                        where_clause = token
                        break
                if where_clause:
                    identifiers.extend(extract_identifiers_from_where(where_clause.tokens))

                # Replace identifiers with hashed values
                column_map = hash_identifiers(identifiers)
                # Replace substrings using the dictionary
                result_string = replace_substrings(str(parsed_query[0]), column_map)

                instance.modified_query = result_string
                instance.hashed_values = column_map
                instance.save()
                return Response(SQLToASTSerializer(instance).data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response("Please enter a valid SQL", status=status.HTTP_400_BAD_REQUEST)


class ASTToSQLViewSet(viewsets.ViewSet):
    def recreate(self, request):  # /api/asttosql
        query = SQLToAST.objects.filter(modified_query=request.data["ast_query"]).first()
        if not query:
            return Response("Please enter a valid query.", status=status.HTTP_400_BAD_REQUEST)
        serializer = SQLToASTSerializer(query)
        return Response(serializer.data.get("original_query", None))
