import os
import django

# Configuração do Django (se necessário)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nome_do_projeto.settings')
django.setup()

from myapp.models import Fotografia  # Certifique-se de importar o modelo corretamente

# Inserindo dados diretamente no Django ORM
fotografia1 = Fotografia(nome="Fotografia 1", legenda="Legenda 1", descricao="Descrição da fotografia 1", foto="foto1.jpg")
fotografia1.save()  # Salva a fotografia no banco de dados

# Para inserir múltiplos registros de uma vez
fotografias = [
    Fotografia(nome="Fotografia 2", legenda="Legenda 2", descricao="Descrição da fotografia 2", foto="foto2.jpg"),
    Fotografia(nome="Fotografia 3", legenda="Legenda 3", descricao="Descrição da fotografia 3", foto="foto3.jpg"),
    Fotografia(nome="Fotografia 4", legenda="Legenda 4", descricao="Descrição da fotografia 4", foto="foto4.jpg"),
]

Fotografia.objects.bulk_create(fotografias)  # Insere várias fotografias de uma vez

# Consultando as fotografias inseridas
fotografias_salvas = Fotografia.objects.all()

# Exibindo as fotografias salvas
for foto in fotografias_salvas:
    print(f"Nome: {foto.nome}, Legenda: {foto.legenda}, Descrição: {foto.descricao}, Foto: {foto.foto}")
