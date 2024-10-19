from flask import Blueprint, render_template, request, redirect

product_routes = Blueprint('product_routes', __name__)

# In memory list of products
products = [
    {
        'name': 'laptop',
        'price': 1000
    },
    {
        'name': 'phone',
        'price': 500
    }

]

@product_routes.route('/products')
def index():
    return render_template('products/index.html', products=products)

@product_routes.route('/products/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        new_product = {
            'name': request.form['name'],
            'price': request.form['price']
        }
        if new_product:
            products.append(new_product)
            return redirect('/products')
            
    return render_template('products/create.html')


@product_routes.route('/products/update/<int:product_id>', methods=['GET', 'POST'])
def update(product_id):
    product = products[product_id - 1] 

    if request.method == 'POST':
        product['name'] = request.form['name']
        product['price'] = request.form['price']
        return redirect('/products')

    return render_template('products/update.html', product=product, product_id=product_id)


#to delete the product
@product_routes.route('/products/delete/<int:product_id>')
def delete(product_id):
    products.pop(product_id - 1)
    return redirect('/products')

