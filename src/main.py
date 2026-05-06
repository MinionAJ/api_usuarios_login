from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src import models, database, schemas
from src.security import gerar_hash, verificar_senha

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/usuarios")
def criar_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    senha_hash = gerar_hash(usuario.senha)

    novo_usuario = models.Usuario(
        nome= usuario.nome,
        email= usuario.email,
        senha= senha_hash
    )
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return novo_usuario

@app.post("/login")
def login(dados: schemas.Login, db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.email == dados.email).first()

    if not usuario:
        return {"erro": "Usuário não encontrado"}

    if not verificar_senha(dados.senha, usuario.senha):
        return {"erro": "Senha inválida"}

    return {"mensagem": "Login realizado com sucesso"}

@app.get("/usuario")
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(models.Usuario).all()