import os
from datetime import datetime
import sqlalchemy as sql
from sqlalchemy.orm import relationship, backref, Session, sessionmaker
import sqlalchemy.ext.declarative as declarative
from sqlalchemy import select, update


BASE_DIR = os.path.dirname(__file__)
data = datetime.now().strftime('%H:%M %d/%m/%Y')

engine = sql.create_engine(f'sqlite:///{BASE_DIR}/database.db', echo=True)
Base = declarative.declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

# use direct


class User(Base):
    __tablename__ = "users"

    id = sql.Column(sql.Integer, index=True, primary_key=True)
    id_na_cloud = sql.Column(sql.Integer, index=True, primary_key=True)
    nome_empresa = sql.Column(sql.String, index=True)
    email = sql.Column(sql.String, index=True)
    whatsapp = sql.Column(sql.String, index=True)
    senha = sql.Column(sql.String, index=True)
    licenca = sql.Column(sql.String, index=True, default="Gratuita")
    max_pesagens = sql.Column(sql.String, index=True, default="30")


class PesagemAvulsa(Base):
    __tablename__ = "avulsas"

    id = sql.Column(sql.Integer, index=True, primary_key=True)
    user_id = sql.Column(sql.Integer, sql.ForeignKey("users.id"))
    user = relationship(
        "User", backref=backref("avulsa", uselist=False))
    motorista = sql.Column(sql.String, index=True)
    produto = sql.Column(sql.String, index=True)
    cliente = sql.Column(sql.String, index=True)
    peso_bruto = sql.Column(sql.String, index=True)
    data = sql.Column(sql.String, index=True, default=data)
    placa = sql.Column(sql.String, index=True)
    obs = sql.Column(sql.String, index=True)


class PesagemEntrada(Base):
    __tablename__ = "entradas"

    id = sql.Column(sql.Integer, index=True, primary_key=True)
    user_id = sql.Column(sql.Integer, sql.ForeignKey("users.id"))
    user = relationship(
        "User", backref=backref("entrada", uselist=False))
    motorista = sql.Column(sql.String, index=True)
    produto = sql.Column(sql.String, index=True)
    cliente = sql.Column(sql.String, index=True)
    peso_entrada = sql.Column(sql.String, index=True)
    data_entrada = sql.Column(sql.String, index=True, default=data)
    placa = sql.Column(sql.String, index=True)


class PesagemSaida(Base):
    __tablename__ = "saidas"

    id = sql.Column(sql.Integer, index=True, primary_key=True)
    user_id = sql.Column(sql.Integer, sql.ForeignKey("users.id"))
    user = relationship(
        "User", backref=backref("saida", uselist=False))
    pesagem_entrada_id = sql.Column(sql.Integer, sql.ForeignKey("entradas.id"))
    entrada = relationship(
        "PesagemEntrada", backref=backref("entrada_2", uselist=False))
    peso_saida = sql.Column(sql.String, index=True)
    data_saida = sql.Column(sql.String, index=True, default=data)
    peso_liquido = sql.Column(sql.String, index=True)


class Cliente(Base):
    __tablename__ = "clientes"

    id = sql.Column(sql.Integer, index=True, primary_key=True)
    user_id = sql.Column(sql.Integer, sql.ForeignKey("users.id"))
    user = relationship(
        "User", backref=backref("cliente", uselist=False))
    nome = sql.Column(sql.String, index=True)
    cpf_cnpj = sql.Column(sql.String, index=True, default=data)
    rg = sql.Column(sql.String, index=True)
    telefone = sql.Column(sql.String, index=True)
    uf = sql.Column(sql.String, index=True)
    cidade = sql.Column(sql.String, index=True)
    endereço = sql.Column(sql.String, index=True)


class Carga(Base):
    __tablename__ = "carga"

    id = sql.Column(sql.Integer, index=True, primary_key=True)
    user_id = sql.Column(sql.Integer, sql.ForeignKey("users.id"))
    user = relationship(
        "User", backref=backref("carga", uselist=False))
    nome = sql.Column(sql.String, index=True)
    preco = sql.Column(sql.String, index=True)
    densidade = sql.Column(sql.String, index=True)
    embalagem = sql.Column(sql.String, index=True)
    desconto = sql.Column(sql.String, index=True)


class Veiculo(Base):
    __tablename__ = "veiculo"

    id = sql.Column(sql.Integer, index=True, primary_key=True)
    user_id = sql.Column(sql.Integer, sql.ForeignKey("users.id"))
    user = relationship(
        "User", backref=backref("veiculo", uselist=False))
    proprietario = sql.Column(sql.String, index=True)
    nome = sql.Column(sql.String, index=True)
    placa = sql.Column(sql.String, index=True)
    carga_id = sql.Column(sql.Integer, sql.ForeignKey("carga.id"))
    carga = relationship(
        "Carga", backref=backref("carga", uselist=False))

#ADD and READ
def add_tables():
    Base.metadata.create_all(bind=engine)


def add_user(id_cloud, nome, email, telefone, senha, licenca, pesagens):
    # user = User(nome_empresa=nome, email=email, whatsapp=telefone,
    #             senha=senha, licenca=licenca, max_pesagens=pesagens)
    # session.add(user)
    session.query(User).filter(User.id == 1).update(
        {
            'id_na_cloud': id_cloud,
            'nome_empresa': nome, 'email': email,
            'whatsapp': telefone, 'senha': senha,
            'licenca': licenca, 'max_pesagens': pesagens
        }
    )

    session.commit()
    session.flush()


def get_all_users():
    users = []
    with engine.begin() as conn:
        for c in conn.execute(sql.text('select * from users')):
            users.append(c)

    return users

