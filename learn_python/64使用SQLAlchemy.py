from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sys,io
#改变标准输出的默认编码,windows需要加这个
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
# print('ss')
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(String(20),primary_key=True)
    name = Column(String(20))

if __name__ == '__main__':
    engine = create_engine('mysql+mysqlconnector://root:zh123456@localhost:3306/test')
    DBSession = sessionmaker(bind=engine)
    
    session = DBSession()
    new_user = User(id='5',name='Jane')
    session.add(new_user)
    session.commit()
    session.close()

    qSession = DBSession()
    result = qSession.query(User).filter(User.id=='5').one()
    print('type:',type(result))
    print('name:',result.name)
    session.close()