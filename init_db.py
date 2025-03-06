from app import app, db

with app.app_context():
    db.create_all()  # This will create all tables based on your model
    print("Database initialized!")

