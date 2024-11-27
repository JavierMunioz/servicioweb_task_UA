from flask import Flask, request, jsonify

app = Flask(__name__)

items = [
    {"id": 1, "name": "Chevrilet", "description": "One car"},
    {"id": 2, "name": "Camaro", "description": "Two car"},
]


@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items), 200

@app.route('/', methods=['GET'])
def home():
    return jsonify({"Welcome":"Service with Flask"}), 200

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item), 200
    return jsonify({"error": "Item not found"}), 404

@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.json
    if "name" not in new_item or "description" not in new_item:
        return jsonify({"error": "Invalid data"}), 400

    new_item["id"] = items[-1]["id"] + 1 if items else 1  
    items.append(new_item)
    return jsonify(new_item), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    updated_data = request.json
    item.update(updated_data)
    return jsonify(item), 200

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({"message": "Item deleted"}), 200

if __name__ == '__main__':
    app.run(debug=False)
