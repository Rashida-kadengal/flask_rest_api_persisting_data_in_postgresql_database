from flask import jsonify, request

from repositories.products_repository import ProductRepository


def get_all_products():
    try:
        repository=ProductRepository()
        data=repository.fetch_all_products()
        if data:
            return jsonify(data)
        else:
            return jsonify({'message': 'No products found'}), 404
    except Exception as e:
        print(e)


def get_product_by_id(product_id):
    try:
        repository=ProductRepository()
        data=repository.fetch_product_by_id(product_id)
        if data:
            return jsonify(data)
        else:
            return jsonify({'message': 'No product found'}), 404
    except Exception as e:
        print(e)


def create_product():
    try:
        repository=ProductRepository()
        new_product=request.json
        data=repository.add_product(new_product["name"])
        if data:
            return jsonify(data)
        else :
            return jsonify({'product cannot be created'}),404
    except Exception as e:
        print(e)
        

        
def update_product(product_id):
    try:
        repository=ProductRepository()
        product=request.json
        data=repository.update_product_data(product_id,product["name"])
        return jsonify(data)
    except Exception as e:
        print(e)



def delete_product(product_id):
    try:
        repository=ProductRepository()
        data=repository.delete_product_data(product_id)
        if data:
            return jsonify(data)
        else:
            return jsonify({'products not found'}),404
    except Exception as e:
        print(e)