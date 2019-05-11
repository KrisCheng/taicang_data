
from sqlalchemy import Column, String, Integer, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

class Case(Base):
    __tablename__ = 'case_info'
    id = Column(Integer, primary_key=True)
    case_id = Column(String(64))
    name = Column(String(64))
    phone_number = Column(String(64))
    title = Column(String(1024))
    content = Column(String(4096))
    remark = Column(String(4096))
    status = Column(String(64))
    ctype = Column(String(64))
    address = Column(String(1024))
    case_status = Column(String(64))

    def __init__(self, case_id, name, phone_number, title, content, remark, status, ctype, address, case_status):
        self.case_id = case_id
        self.name = name
        self.phone_number = phone_number
        self.title = title
        self.content = content
        self.remark = remark
        self.status = status
        self.ctype = ctype
        self.address = address
        self.case_status = case_status
