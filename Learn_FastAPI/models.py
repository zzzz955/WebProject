from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 데이터베이스 연결 URL (PostgreSQL에 연결)
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@localhost/exampledb"

# SQLAlchemy 기본 설정
Base = declarative_base()

# 세션 만들기
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# 테이블 모델 정의
class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(80), nullable=False)
    description = Column(String(200), nullable=False)


# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)
