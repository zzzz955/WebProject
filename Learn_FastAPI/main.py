from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from models import SessionLocal, Item
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# FastAPI 앱 초기화
app = FastAPI()

# CORS 설정 추가
origins = ["*"]  # 모든 도메인 허용

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 허용할 오리진 (프론트엔드 주소)
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 헤더 허용
)

# Pydantic 모델 정의
class ItemCreate(BaseModel):
    name: str
    description: str

class ItemUpdate(BaseModel):
    name: str
    description: str

class ItemResponse(BaseModel):
    id: int
    name: str
    description: str

# 데이터베이스 세션을 만드는 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1. 모든 항목 조회
@app.get("/items", response_model=list[ItemResponse])
def read_items(db: Session = Depends(get_db)):
    items = db.query(Item).all()
    return items

# 2. 특정 id 조회
@app.get("/items/{item_id}", response_model=ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# 3. 아이템 생성
@app.post("/items", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# 4. 아이템 수정
@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: ItemUpdate, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    db_item.name = item.name
    db_item.description = item.description
    db.commit()
    db.refresh(db_item)
    return db_item

# 5. 아이템 삭제
@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(db_item)
    db.commit()
    return {"message": f"Item with id {item_id} deleted"}
