# 使用数据库连接池提高程序运行效率
# Improve the efficiency by using connection pool

# References:
#   https://developer.aliyun.com/article/1276445
#   https://blog.csdn.net/CrankZ/article/details/82874158

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_poll(wk_database, pool_size, max_overflow):
    try:
        engine = create_engine(wk_database, echo=False, pool_size=pool_size, max_overflow=max_overflow)
        Session = sessionmaker(bind=engine)
        return Session()
    except Exception as e:
        print(f'Error occurs when creating a session of database: {e}')
        return None

# An example:
# if __name__ == '__main__':
#    session = create_poll('sqlite:///example.db', 5, 10)
#    if session:
#        results = session.execute('SELECT * FROM TABLE_1').fetchall()
#    print(results)
#        session.close()
