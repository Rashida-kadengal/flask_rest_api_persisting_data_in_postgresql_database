from flask import jsonify, request
from repositories.categories_repository import CategoryRepository

def get_all_categories():
    try:
        repository=CategoryRepository()
        data =repository.fetch_all_categories()  # Ensure this function is called correctly
        if data:  # Check if data 
            return jsonify(data)  # Return the data if everything is okay
        return jsonify({"error": "No categories found"}), 404  # Return a 404 response if no data
    except Exception as e:
        print(e)


def get_category_by_id(category_id):
    try:
        repository=CategoryRepository()
        data=repository.fetch_category_by_id(category_id)
        if data:  # Check if data 
            return jsonify(data)  # Return the data if everything is okay
        return jsonify({"error": "No categories found"}), 404
    except Exception as e:
        print(e)


def create_category():
    try:
        repository=CategoryRepository()
        new_category=request.json
        data=repository.add_category(new_category["name"])
        if data:
            return jsonify(data)
        return jsonify({"category can't be created"}), 404
    except Exception as e:
        print(e)


def update_category(category_id):
    try:
        repository=CategoryRepository()
        category=request.json
        data=repository.update_category_data(category_id,category["name"])
        return jsonify(data)
    except Exception as e:
        print(e)


def delete_category(category_id):
    try:
        repository=CategoryRepository()
        data=repository.delete_category_data(category_id)
        return jsonify(data)
    except Exception as e:
            print(e)