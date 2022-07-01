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
    id_na_cloud = sql.Column(sql.Integer, index=True)
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

    def __repr__(self):
        return f'({self.id}) {self.motorista}'


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
    cep = sql.Column(sql.String, index=True)
    endereço = sql.Column(sql.String, index=True)

    def __repr__(self):
        return f'({self.id}) {self.nome}'


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

    def __repr__(self):
        return f"({self.id}) {self.nome}"


class Veiculo(Base):

    __tablename__ = "veiculo"

    id = sql.Column(sql.Integer, index=True, primary_key=True)
    user_id = sql.Column(sql.Integer, sql.ForeignKey("users.id"))
    user = relationship("User", backref=backref("veiculo", uselist=False))
    proprietario = sql.Column(sql.String, index=True)
    nome = sql.Column(sql.String, index=True)
    placa = sql.Column(sql.String, index=True)
    carga_id = sql.Column(sql.Integer, sql.ForeignKey("carga.id"))
    carga = relationship(
        "Carga", backref=backref("carga", uselist=False))

    def __repr__(self):
        return f'({self.id}) {self.nome}'


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


def add_veiculo(id_user_local, proprietario, modelo, placa, produto):
    dados = Veiculo(
        user_id=id_user_local,
        proprietario=proprietario,
        nome=modelo,
        placa=placa,
        carga_id=produto,
    )
    session.add(dados)
    session.commit()
    session.flush()


def list_veiculos():
    query = session.query(Veiculo).all()
    session.commit()

    return query


def add_carga(id_user_local, nome, preco, densidade, embalagem, desconto):
    dados = Carga(
        user_id=id_user_local,
        nome=nome,
        preco=preco,
        densidade=densidade,
        embalagem=embalagem,
        desconto=desconto)

    session.add(dados)
    session.commit()
    session.flush()


def list_cargas(carga=False):
    if carga:
        carga_id = carga.split(')')[0].replace('(', '')
        query = carga_id
    else:
        query = session.query(Carga).all()

    session.commit()

    return query


def add_cliente(id_user_local, nome, cpf_cnpj, rg, telefone, cep, endereço):
    dados = Cliente(
        user_id=id_user_local,
        nome=nome,
        cpf_cnpj=cpf_cnpj,
        rg=rg,
        telefone=telefone,
        cep=cep,
        endereço=endereço)

    session.add(dados)
    session.commit()
    session.flush()


def list_clientes():
    query = session.query(Cliente).all()
    session.commit()

    return query


def get_all_users():
    users = []
    with engine.begin() as conn:
        for c in conn.execute(sql.text('select * from users')):
            users.append(c)

    return users


def att_user_nome(nome):
    query = session.query(User).first()
    query.nome_empresa = nome
    session.commit()
    return True


def att_user_telefone(telefone):
    query = session.query(User).first()
    query.whatsapp = telefone
    session.commit()


def att_user_senha(senha_atual, senha_1, senha_2):
    query = session.query(User).first()
    if senha_atual == query.senha:
        if senha_1 == senha_2:
            query.senha = senha_1
            session.commit()
            return True
        else:
            return None
    else:
        return False


def excluir_conta(senha):
    query = session.query(User).first()
    if query.senha == senha:
        # Deletar conta
        pass
        


if __name__ == '__main__':
    att_user_senha()
