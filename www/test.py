import orm
import asyncio
from models import User,Blog,Comment

def test():
    yield from orm.create_pool(None,user='test',password='123456',db='awesome')

    u=User(name='Test',email='test@163.com',password='123456',image='about:blank')
    yield from u.save()

test()
   