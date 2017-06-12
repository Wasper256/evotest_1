"""Here is DB models."""
from extentions import db


class Names(db.Model):
    """Name table db model."""

    __tablename__ = "names"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True, nullable=False)

    def __init__(self, name):
        """initialization."""
        self.name = name
