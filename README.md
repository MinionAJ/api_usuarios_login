# 🔐 API de Usuários com Autenticação

Projeto backend desenvolvido com Python e FastAPI com foco em aprendizado de APIs REST, autenticação de usuários e boas práticas de desenvolvimento backend.

---

## 🚀 Funcionalidades

* ✅ Cadastro de usuários
* ✅ Listagem de usuários
* ✅ Login de usuários
* ✅ Criptografia de senha com bcrypt
* ✅ Integração com banco de dados SQLite

---

## 🛠️ Tecnologias Utilizadas

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Passlib (bcrypt)
* Uvicorn

---

## 📁 Estrutura do Projeto

```id="j5u3fz"
projeto_api/
│
└── src/
    ├── main.py
    ├── database.py
    ├── models.py
    ├── schemas.py
    ├── security.py
    └── __init__.py
```

---

## 🔒 Autenticação

As senhas dos usuários são armazenadas de forma segura utilizando criptografia com bcrypt através da biblioteca Passlib.

Fluxo implementado:

1. Usuário realiza cadastro
2. Senha é criptografada antes de salvar
3. Login valida email e senha criptografada

---

## ▶️ Como Executar

### 1. Instalar dependências

```bash id="pph6h0"
pip install fastapi uvicorn sqlalchemy passlib[bcrypt]
```

---

### 2. Executar aplicação

```bash id="h4fgm6"
uvicorn src.main:app --reload
```

---

## 🌐 Documentação Interativa

Após iniciar o servidor:

```id="huwz57"
http://127.0.0.1:8000/docs
```

---

## 📌 Endpoints

### Criar usuário

```http id="s9a4wo"
POST /usuarios
```

### Listar usuários

```http id="bg1k7x"
GET /usuarios
```

### Login

```http id="0ykb0g"
POST /login
```

---

## 📚 Conceitos Aplicados

* APIs REST
* CRUD
* Autenticação
* Criptografia de senha
* Estruturação backend
* ORM com SQLAlchemy

---

## 🚀 Próximas Melhorias

* JWT Authentication
* Rotas protegidas
* PostgreSQL
* Deploy da API
* Integração com frontend Flutter

---

## 👨‍💻 Objetivo do Projeto

Projeto criado para desenvolvimento de habilidades práticas em backend utilizando Python e FastAPI, com foco em evolução profissional na área de tecnologia.
