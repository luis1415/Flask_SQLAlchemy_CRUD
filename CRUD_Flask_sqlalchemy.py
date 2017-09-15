from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@127.0.0.1/MAPA'
db = SQLAlchemy(app)


class Ejemplo(db.Model):
    __tablename__ = 'FAlchemy'
    id = db.Column('id', db.Integer, primary_key=True)
    data = db.Column('data', db.Unicode)

    def __init__(self, id_, data):
        self.id = id_
        self.data = data


if __name__ == '__main__':
    app.run()
