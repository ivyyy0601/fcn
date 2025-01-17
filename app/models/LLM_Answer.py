from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base

class Answer(Base):
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True)
    LLM_AnsID = Column(Integer, nullable=False)
    LLM_Name = Column(String(50), nullable=False)
    LLM_AnswerImg = Column(String(255))  # 这里存储图片文件路径
    LLM_Score = Column(Integer, nullable=False)
    Comments = Column(String(255))

    def __init__(self, LLM_AnsID, LLM_Name, LLM_AnswerImg, LLM_Score, Comments):
        self.LLM_AnsID = LLM_AnsID
        self.LLM_Name = LLM_Name
        self.LLM_AnswerImg = LLM_AnswerImg
        self.LLM_Score = LLM_Score
        self.Comments = Comments
