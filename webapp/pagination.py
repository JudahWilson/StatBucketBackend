from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'length'
    max_page_size = 1000

    def get_paginated_response(self, data):

        request = self.request
        current_url = request.build_absolute_uri()
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'current_url': current_url,
            "draw": int(request.query_params.get('draw', 0)),
            "recordsTotal": self.page.paginator.count,
            "recordsFiltered": self.page.paginator.count,
            "data": data
        })
