from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tutorial.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#definicion del modelo 
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    
    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}')>"
    
#funcion para inicialiazr la base de datos
def init_db():
    with app.app_context():
        db.create_all()
        print("Base de datos inicializada")
        
#operaciones CRUD

def insert_users():
    with app.app_context():
        user1 = User(name="Bruno Diaz", email="brunodiaz@gmail.com")
        user2 = User(name="Ricardo Tapia", email="rycky@mail.com")
        user3 = User(name="Zacarias Flores", email="zaca@mail.com")
        user4 = User(name="Santiago Tapia", email="santi@mail.com")
        user5 = User(name="Armando Carpas", email="armi@mail.com")
        # adicion de objetos  (registros en la tabla)
        db.session.add(user1)
        db.session.add(user2)
        db.session.add(user3)
        db.session.add(user4)
        db.session.add(user5)
        #consolida los cambios en la base de datos
        db.session.commit()
        print("Usuarios creados")
        
#consulta a la base de datos

def query_users():
    with app.app_context():
        #cosnsultar todos los registro de una tabla
        print("Listado de los usuarios")
        users = User.query.all() # muestra todos los registros de una bd
        for item in users:
            print(item)
        
        #consulta de un registro especifico que cumplen cierta condicion
        print("\nRegistros filtrados por Usuario con id 2")
        filtrados = User.query.filter(User.id >= 2).all()
        for item in filtrados:
            print(item)
            
        #consulta de un solo usuario
        print("\nobtener un solo registro")
        user = User.query.filter_by(id=2).first()
        if user:
            print(user)
        else:
            print("No se encontro el usuario")
            
# def update_user():
#     with app.app_context():
#         print("\nActualizar un usuario")
#         user = User.query.filter_by(id=1).first()
#         if user:
#             user.name = "Benjamin Cadillo"
#             user.email = "bencadillo@mail"
#             #consolida los cambios
#             db.session.commit()
#             print("Usuario actualizado", user)
#         else:
#             print("No se encontro el usuario")


#actualiza mas
def update_users():
    with app.app_context():
        print("\nActualizar múltiples usuarios")
        users = User.query.filter(User.id.in_([1, 2])).all()
        
        if users:
            for user in users:
                if user.id == 1:
                    user.name = "Benjamin Cadillo"
                    user.email = "bencadillo@mail"
                elif user.id == 2:
                    user.name = "Ricardo Pérez"
                    user.email = "ricardo.perez@mail"
            
            db.session.commit()
            print("Usuarios actualizados:")
            for user in users:
                print(user)
        else:
            print("No se encontraron los usuarios")



#eliminar usuario
# def delete_user():
#     with app.app_context():
#         print("\nEliminar un usuario")
#         user = User.query.filter_by(id=3).first()
#         if user:
#             db.session.delete(user)
#             db.session.commit()
#             print("Usuario eliminado", user)
#         else:
#             print("No se encontro el usuario")
            

#eliminar mas

def delete_users():
    with app.app_context():
        print("\nEliminar múltiples usuarios")
        users_to_delete = User.query.filter(User.id.in_([2, 3])).all()

        if users_to_delete:
            for user in users_to_delete:
                db.session.delete(user)
            db.session.commit()
            print("Usuarios eliminados:")
            for user in users_to_delete:
                print(user)
        else:
            print("No se encontraron los usuarios a eliminar")


if __name__ == '__main__':
    init_db()
    insert_users()
    query_users()
    update_users()
    delete_users()