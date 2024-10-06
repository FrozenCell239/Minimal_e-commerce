from app.extensions import db
from sqlalchemy.sql import func

class Order(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    customer_mail = db.Column(db.String(100), nullable = False)
    content = db.Column(db.Text, nullable = False) # The content of the order will be stored as a JSON string
    created_at = db.Column(
        db.DateTime(timezone = True),
        nullable = False,
        server_default = func.current_timestamp()
    )

    def __init__(self, customer_mail: str, content: str) -> None :
        self.customer_mail = customer_mail
        self.content = content

    def __repr__(self) -> str : return f'<Product "{self.username}">'

    # Creation date getter
    def getCreatedAt(self) -> dict[str, str] :
        return {
            'date' : str(self.created_at)[:10],
            'time' : str(self.created_at)[10:-13],
            'timezone' : str(self.created_at)[-6:]
        }