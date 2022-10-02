from peewee import *
import os
arq = "Frente_CaixaBD.db"
db = SqliteDatabase(arq)

class BaseModel(Model):

    class Meta:
        database = db

class Operador(BaseModel):

    def __init__(self, nome, turno, qtd_dias_rapido, folga):
        self.nome = nome
        self.turno = turno
        self.qtd_dias_rapidos = 0
        self.folga = folga

if __name__ == "__main__":

    if os.path.exists(arq):
        os.remove(arq)
    db.connect()
    db.create_tables([Operador])

operador = ('Talis','T',0,1)
operador = ('Matheus','M',0,2)