#自定义分页
import math
class PageHelper():
    def __init__(self,url,query_list,current_page,index_num=9,per_page_num=4):
        """
        初始化
        :param url: 请求地址
        :param query_list: 查询结果集
        :param current_page: 跳转页码
        :param index_num: 显示页数
        :param per_page_num: 每页显示结果条数
        """
        self.url = url
        self.query_list = query_list
        self.total_count = len(query_list)
        self.current_page = current_page
        self.per_page_num = per_page_num
        self.index_num = index_num
    @property
    def getQueryList(self):
        start = (int(self.current_page)-1) * int(self.per_page_num)
        if math.ceil(self.total_count/self.per_page_num) == self.current_page:
            end = self.total_count + 1
            return self.query_list[start:end]
        else:
            return self.query_list[start:start+self.per_page_num]
    @property
    def getAumout(self):
        return self.total_count
    @property
    def getPage(self):
        v,a = divmod(self.total_count,self.per_page_num)
        if a != 0:
            v += 1
        if v <= self.index_num:
            start_page = 1
            end_page = v
        else:
            if self.current_page < math.floor(self.index_num/2):
                start_page = 1
                end_page = self.index_num
            else:
                start_page = self.current_page-math.floor(self.per_page_num/2)
                end_page = self.current_page + math.floor(self.per_page_num/2)
                if end_page > v:
                    start_page = v-self.per_page_num
                    end_page = v
        page_list = []
        if int(self.current_page) == 1:
            page_list.append('<a href="javascript:void(0);">上一页</a>')
        else:
            page_list.append('<a href="%s?pageno=%s" >上一页</a>'%(self.url,int(self.current_page) - 1))
        for i in range(start_page,end_page+1):
            if i == int(self.current_page):
                page_list.append('<a class="current" href="%s?pageno=%d" >%a</a>'%(self.url,i,i))
            else:
                page_list.append('<a href="%s?pageno=%d" >%a</a>'%(self.url,i,i))
        if int(self.current_page) == v:
            print(111)
            print('页数：',v,'当前页码：',self.current_page)
            page_list.append('<a href="javascript:void(0);">下一页</a>')
        else:
            print(222)
            print('页数：', v, '当前页码：', self.current_page)
            page_list.append('<a href="%s?pageno=%s" >下一页</a>' % (self.url, int(self.current_page) + 1))
        pages = ' '.join(page_list)
        return pages