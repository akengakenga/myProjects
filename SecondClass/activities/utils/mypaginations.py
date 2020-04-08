from rest_framework.pagination import PageNumberPagination


class MyNumberPagination(PageNumberPagination):
    page_size = 6  #每页数量
    page_query_param = 'page'  #页码
    page_size_query_param = 'size'  # 修改每页数量
    max_page_size = 6  #最大每页数量