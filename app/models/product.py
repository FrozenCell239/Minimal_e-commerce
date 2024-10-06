from app.extensions import db
from sqlalchemy.sql import func

class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False, unique = True)
    description = db.Column(db.Text, nullable = False)
    price = db.Column(db.Float, nullable = False)
    stock = db.Column(db.Integer, nullable = False)
    created_at = db.Column(
        db.DateTime(timezone = True),
        nullable = False,
        server_default = func.current_timestamp()
    )

    def __init__(self, name: str, description: str, price: float, stock: int) -> None :
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

    def __repr__(self) -> str : return f'<Product "{self.username}">'

    # Creation date getter
    def getCreatedAt(self) -> dict[str, str] :
        return {
            'date' : str(self.created_at)[:10],
            'time' : str(self.created_at)[10:-13],
            'timezone' : str(self.created_at)[-6:]
        }