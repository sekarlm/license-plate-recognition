from app import db
from sqlalchemy.dialects.postgresql import JSON

class Plate(db.Model):
    __tablename__ = 'plate_numbers'

    id_user = db.Column(db.Integer)
    id_transaction = db.Column(db.Integer, primary_key=True)
    plate_number = db.Column(db.String(8), unique=True)
    place = db.Column(db.String(64))
    time_enter = db.Column(db.DateTime(timezone=True))
    time_out = db.Column(db.DateTime(timezone=True))
    price = db.Column(db.Numeric())

    def __init__(self, id_user, id_transaction, plate_number, place):
        self.id_user = id_user
        self.id_transaction = id_transaction
        self.plate_number = plate_number
        self.place = place

    def __repr__(self) -> str:
        return '<id_transaction {}>'.format(self.id_transaction)

    def serialize(self):
        return {
            'id_user': self.id_user,
            'id_transaction': self.id_transaction,
            'plate_number': self.plate_number,
            'place': self.place,
            'time_enter': self.time_enter,
            'time_out': self.time_out,
            'price': self.price
        }