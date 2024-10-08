from flask import jsonify, request
from repositories.brands_repository import BrandRepository


def get_all_brands():
    try:
        repository=BrandRepository()
        data=repository.fetch_all_brands()
        if data:
            return jsonify(data)
        return jsonify({"error": "No brands found"}), 404 
    except Exception as e:
        print(e)
        

def get_brand_by_id(brand_id):
    try:
        repository=BrandRepository()
        data=repository.fetch_brand_by_id(brand_id)
        if data:
            return jsonify(data)
        else:
            return jsonify({'message':'brand not found'}),404
    except Exception as e:
        print(e)



def create_brand():
    try:
        repository=BrandRepository()
        new_brand=request.json
        data=repository.add_brand(new_brand["name"])
        if data:
            return jsonify(data)
        return jsonify({"category can't be created"}), 404
    except Exception as e:
        print(e)



def update_brand(brand_id):
    repository=BrandRepository()
    brand=request.json
    data=repository.update_brand_data(brand_id,brand["name"])
    return jsonify(data)



def delete_brand(brand_id):
    repository=BrandRepository()
    data=repository.delete_brand_data(brand_id)
    return jsonify(data)
