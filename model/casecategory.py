
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

class CaseCategory(Base):
    __tablename__ = 'case_category'
    id = Column(Integer, primary_key=True)
    category = Column(String(1024))
    categorycode = Column(String(64))
    remark = Column(String(4096))

    def __init__(self, category, categorycode, remark):
        self.category = category
        self.categorycode = categorycode
        self.remark = remark