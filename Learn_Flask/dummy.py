from app import create_app, db
from app.models import Item  # Item 모델 임포트
from faker import Faker
import random

app = create_app()

# Faker 객체 생성
fake = Faker()


# 랜덤 데이터 생성 및 삽입
def generate_random_items(num_items):
    items = []

    for _ in range(num_items):
        name = fake.word().capitalize()  # 랜덤 단어로 아이템 이름 생성
        description = fake.sentence()  # 랜덤 문장으로 설명 생성
        item = Item(name=name, description=description)
        items.append(item)

    # 애플리케이션 컨텍스트 활성화 후 데이터베이스에 저장
    with app.app_context():  # 애플리케이션 컨텍스트 활성화
        with db.session.begin():  # 트랜잭션 시작
            db.session.add_all(items)


# 랜덤 아이템 50개 생성
generate_random_items(10)
