from app.libs.helper import get_isbn


# 表示单本书籍的模型
class BookViewModel:
    def __init__(self, data):
        # if not isinstance(data, dict):V
        #     author = data.author
        #     data = data.__dict__
        #     data['author'] = author
        self.title = data['title']
        self.author = '、'.join(data['author'])
        self.binding = data['binding']
        self.publisher = data['publisher']
        self.image = data['image']
        self.price = '￥' + data['price'] if data['price'] else data['price']
        self.isbn = get_isbn(data)
        self.pubdate = data['pubdate']
        self.summary = data['summary']
        self.pages = data['pages']

    @property
    def intro(self):
        intros = filter(lambda x: True if x else False,
                        [self.author, self.publisher, self.price])
        return ' / '.join(intros)

# 书本集合处理模型
class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = None

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.books = [BookViewModel(book) for book in yushu_book.books]
        self.keyword = keyword


class BookViewModelOld:
    @classmethod
    def from_api(cls, keyword, data):
        '''
            为什么不在spider里做成viewmodel？
            从豆瓣获取的数据可能是单本，也可能是多本集合
            data 有三种情况：
            1. 单本
            2. 空对象
            3. 多对象
        '''
        # if not data:

        yushu_books = data.get('books', 'null')
        if yushu_books == 'null':
            total = 1
            temp_books = [data]
        else:
            if len(yushu_books) > 0:
                total = data['total']
                temp_books = yushu_books
            else:
                total = 0
                temp_books = []

        books = []
        for book in temp_books:
            book = cls.get_detail(book, 'from_api')
            books.append(book)
        # douban_books = result['books'] if result.get('books') else [result]
        view_model = {
            'total': total,
            'keyword': keyword,
            'books': books
        }
        return view_model

    @classmethod
    def single_book_from_mysql(cls, keyword, data):
        count = 1
        if not data:
            count = 0
        returned = {
            'total': count,
            'keyword': keyword,
            'books': [cls.get_detail(data)]
        }
        return returned

    @classmethod
    def get_detail(cls, data, from_where='from_mysql'):
        if from_where == 'from_api':
            book = {
                'title': data['title'],
                'author': '、'.join(data['author']),
                'binding': data['binding'],
                'publisher': data['publisher'],
                'image': data['images']['large'],
                'price': data['price'],
                'isbn': data['isbn'],
                'pubdate': data['pubdate'],
                'summary': data['summary'],
                'pages': data['pages']
            }
        else:
            book = {
                'title': data['title'],
                'author': '、'.join(data['author']),
                'binding': data['binding'],
                'publisher': data['publisher'],
                'image': data.image,
                'price': data['price'],
                'isbn': data.isbn,
                'pubdate': data['pubdate'],
                'summary': data['summary'],
                'pages': data['pages']
            }
        return book

        # @classmethod
        # def get_isbn(cls, book):
        #     isbn13 = book.get('isbn13', None)
        #     isbn10 = book.get('isbn10', None)
        #     return isbn13 if isbn13 else (isbn10 if isbn10 else '')


# 根本没用到python面向对象。简单的堆叠一些函数 面向过程编程
# 类包括
# 描述特征 (类变量、实例变量)
# 行为 (方法)
class _BookViewModel:
    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = 1
            returned['books'] = [cls._cut_book_data(data)]
        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = data['total']
            returned['books'] = [cls._cut_book_data(book) for book in data['books']]
        return returned

    @classmethod
    def _cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'] or '',
            'author': '、'.join(['author']),
            'price': data['price'],
            'summary': data['summary'] or '',
            'image': data['image']
        }
        return book

    @classmethod
    def _cut_books_data(cls, data):
        books = []
        for book in data['books']:
            r = {
                'title': book['title'],
                'publisher': book['publisher'],
                'pages': book['pages'],
                'author': '、'.join(book['author']),
                'price': book['price'],
                'summary': book['summary'],
                'image': book['image']
            }
            books.append(r)
        return books
