from flask import Flask
from flask import current_app

app = Flask(__name__)
# 应用上下文 对象 Flask
# 请求上下文 对象 Request
# Flask AppContext
# Request RequestContext
# 离线应用、单元测试
# ctx = app.app_context()
# ctx.push
# a = current_app
# d = current_app.config["DEBUG"]
# ctx.pop()

with app.app_context():
    a = current_app
    d = current_app.config["DEBUG"]

# 实现了上下文协议的对象使用with
# 上下文管理器
# __enter__ __exit__
# 上下文表达式必须要返回一个上下文管理器

# 文件读写
# try:
#     f = open(r'D:\txt')
#     print(f.read())
# finally:
#     f.close()
#
# with  open(r'') as f:
#     print(f.read())

# 1.连接数据库
# 2.Sql
# 3.释放资源


# class A:
#     def __enter__(self):
#         a = 1
#         return a
#
#     def __exit__(self):
#         b = 2
#
# with A() as obj_a:
#     pass
#
# obj_a 不是A() 这个上下文管理器
# 而且上下文管理器类中__enter__方法返回值对象




















