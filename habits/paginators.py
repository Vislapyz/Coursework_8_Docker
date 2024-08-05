from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    """
    Количество сущностей, которое будет выведено на 1 странице
    """

    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 10
