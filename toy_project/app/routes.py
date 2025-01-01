from flask import Blueprint, request, jsonify
from .models import Item
from .db import db

api_bp = Blueprint('api', __name__)

@api_bp.route('/items', methods=['POST'])
def create_item():
    data = request.json
    if not data.get('name'):
        return jsonify({'message': '아이템 이름은 필수입니다.'}), 400

    new_item = Item(name=data['name'], description=data.get('description', ''))
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'message': '아이템이 성공적으로 추가되었습니다.'}), 201

@api_bp.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([{'id': item.id, 'name': item.name, 'description': item.description} for item in items])

@api_bp.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    # 아이템을 'id'로 조회
    item = Item.query.get(item_id)  # 'get' 메서드로 primary key를 기준으로 조회

    if not item:
        return jsonify({'message': 'Item not found'}), 404  # 아이템이 없으면 404 응답

    # 아이템이 존재하면 정보 반환
    return jsonify({
        'id': item.id,
        'name': item.name,
        'description': item.description
    })

@api_bp.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.json
    item = Item.query.get(item_id)
    if not item:
        return jsonify({'message': 'Item not found'}), 404

    item.name = data['name']
    item.description = data['description']
    db.session.commit()
    return jsonify({'message': 'Item updated'})

@api_bp.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({'message': 'Item not found'}), 404

    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Item deleted'})
