from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """User model for storing user details."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mpesa_transactions = db.relationship('MpesaTransaction', backref='user', lazy=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return f'<User {self.username}>'

class MpesaTransaction(db.Model):
    """Model for storing M-Pesa transaction details."""
    id = db.Column(db.Integer, primary_key=True)
    transaction_id = db.Column(db.String(100), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    reference = db.Column(db.String(100), nullable=True)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)  # Optional: link to User

    def __init__(self, transaction_id, phone_number, amount, status, description=None, reference=None, user_id=None):
        self.transaction_id = transaction_id
        self.phone_number = phone_number
        self.amount = amount
        self.status = status
        self.description = description
        self.reference = reference
        self.user_id = user_id

    def __repr__(self):
        return f'<MpesaTransaction {self.transaction_id}>'