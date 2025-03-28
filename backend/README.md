# Backend

# 📌 Projeto: Sistema de Cadastro de Pessoas

Este projeto é uma API RESTful desenvolvida com **Django** e **Django REST Framework (DRF)**, que permite cadastrar, listar, editar, excluir e pesquisar pessoas.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Django 4.x**
- **Django REST Framework**
- **PostgreSQL (ou SQLite para desenvolvimento)**
- **Docker (Opcional)**

---

## 🚀 Como Configurar o Projeto

### **1️⃣ Clonar o Repositório**

```sh
git clone https://github.com/seu-usuario/seu-projeto.git
cd seu-projeto
```

### **2️⃣ Criar e Ativar um Ambiente Virtual**

```sh
python -m venv venv
# No Windows
venv\Scripts\activate
# No Linux/Mac
source venv/bin/activate
```

### **3️⃣ Instalar as Dependências**

```sh
pip install -r requirements.txt
```

### **4️⃣ Configurar o Banco de Dados**

> Caso esteja usando PostgreSQL, crie um banco de dados e configure o `.env`.

Crie um arquivo `.env` na raiz do projeto:

```ini
DB_ENGINE=django.db.backends.postgresql
DB_NAME=seu_banco
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
```
---

## 🔄 Rodar as Migrações do Banco

```sh
python manage.py migrate
```

---

## ▶️ Executar o Servidor

```sh
python manage.py runserver
```

A API estará disponível em [**http://127.0.0.1:8000/**](http://127.0.0.1:8000/).

---

## 📡 Endpoints da API

| Método | Rota               | Descrição                    |
| ------ | ------------------ | ---------------------------- |
| GET    | /api/pessoas/      | Lista todas as pessoas       |
| POST   | /api/pessoas/      | Cria uma nova pessoa         |
| GET    | /api/pessoas/{id}/ | Obtém detalhes de uma pessoa |
| PUT    | /api/pessoas/{id}/ | Atualiza uma pessoa          |
| DELETE | /api/pessoas/{id}/ | Remove uma pessoa            |

---

## 🐳 Rodando com Docker (Opcional)

```sh
docker-compose up --build
```

Isso criará os containers com o **Django + PostgreSQL**.

---

## 📌 Considerações Finais

Caso tenha dúvidas ou precise de suporte, entre em contato! 🚀
