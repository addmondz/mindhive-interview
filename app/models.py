from app import db

class Outlet(db.Model):
    __tablename__ = 'outlets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    latitude = db.Column(db.String(100), nullable=True)
    longitude = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f'<Outlet {self.name}>'
