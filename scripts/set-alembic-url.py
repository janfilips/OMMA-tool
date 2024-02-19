import os

with open("alembic.ini", "r") as file:
    content = file.read()

user = os.environ["POSTGRES_USER"]
password = os.environ["POSTGRES_PASSWORD"]
host = os.environ["POSTGRES_HOST"]
port = os.environ["POSTGRES_PORT"]
db = os.environ["POSTGRES_DB"]

url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
content = content.replace('%POSTGRES_USER%', user).replace('%POSTGRES_PASSWORD%', password).replace('%POSTGRES_HOST%', host).replace('%POSTGRES_PORT%', port).replace('%POSTGRES_DB%', db)

with open("alembic.ini", "w") as file:
    file.write(content)
