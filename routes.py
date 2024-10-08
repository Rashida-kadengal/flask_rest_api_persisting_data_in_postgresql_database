from route_handlers.brand_route_handler import create_brand, delete_brand, get_all_brands, get_brand_by_id, update_brand
from route_handlers.category_route_handler import create_category, delete_category, get_all_categories, get_category_by_id, update_category
from route_handlers.product_route_handler import create_product, delete_product, get_all_products, get_product_by_id, update_product


def register_routes(app):
   app.route('/products',methods=['GET'])(get_all_products)
   app.route('/products/<int:product_id>',methods=['GET'])(get_product_by_id)
   app.route('/products',methods=['POST'])(create_product)
   app.route('/products/<int:product_id>',methods=['PUT'])(update_product)
   app.route('/products/<int:product_id>',methods=['DELETE'])(delete_product)
   app.route('/categories',methods=['GET'])(get_all_categories)
   app.route('/categories/<int:category_id>', methods=['GET'])(get_category_by_id)
   app.route('/categories',methods=['POST'])(create_category)
   app.route('/categories/<int:category_id>', methods=['PUT'])(update_category)
   app.route('/categories/<int:category_id>', methods=['DELETE'])(delete_category)
   app.route('/brands',methods=['GET'])(get_all_brands)
   app.route('/brands/<int:brand_id>',methods=['GET'])(get_brand_by_id)
   app.route('/brands',methods=['POST'])(create_brand)
   app.route('/brands/<int:brand_id>',methods=['PUT'])(update_brand)
   app.route('/brands/<int:brand_id>',methods=['DELETE'])(delete_brand)


