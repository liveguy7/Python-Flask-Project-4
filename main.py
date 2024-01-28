from project import create_app, _db
from project.models import User
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager

app = create_app()



if __name__ == '__main__':
  #with app.app_context():
   # _db.create_all()
  app.run(host='0.0.0.0', port=81)

