# 导入所需要的模块和类
from app.models.human import Human
from sqlalchemy import Column, String, Integer, orm



class Admin(Human):
    
    id = Column(Integer, primary_key = True, autoincrement = True)

    def __init__(self, email, password):
        super(Admin,self).__init__(email, password)
