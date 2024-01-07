from flask import jsonify, request, render_template
from app import app, db
from app.models import Outlet

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/outlets', methods=['GET'])
def get_outlets():
    outlets = Outlet.query.all()
    return jsonify([{
        'id': outlet.id,
        'name': outlet.name,
        'address': outlet.address,
        'latitude': outlet.latitude,
        'longitude': outlet.longitude
    } for outlet in outlets])

@app.route('/outlet', methods=['POST'])
def add_outlet():
    data = request.json
    new_outlet = Outlet(name=data['name'], address=data['address'])
    db.session.add(new_outlet)
    db.session.commit()
    return jsonify({'message': 'New outlet added!', 'id': new_outlet.id}), 201

@app.route('/outlet/<int:outlet_id>', methods=['GET'])
def get_outlet(outlet_id):
    outlet = Outlet.query.get_or_404(outlet_id)
    return jsonify({
        'id': outlet.id,
        'name': outlet.name,
        'address': outlet.address,
        'latitude': outlet.latitude,
        'longitude': outlet.longitude
    })
