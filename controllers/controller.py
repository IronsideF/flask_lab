from flask import render_template
from app import app
from models.all_orders import order_list

@app.route('/orders')
def index():
    return render_template('index.html', title='All Orders', all_orders=enumerate(order_list))

@app.route('/orders/<int:index>')
def single_order(index):
    return render_template('order.html', order=order_list[index])
