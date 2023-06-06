import datetime
class Categoria():
    def __init__(self, titulo):
        self.titulo = titulo
        
        
class Evento():
    def __init__(self, titulo,data,categoria,data_criacao):
        self.titulo = titulo
        self.data = data
        self.categoria = categoria
        self.data_criacao = data_criacao.strftime('%Y-%m-%d %H:%M:%S')
        
def exibir_categorias(categorias):
    print("Categorias Disponiveis:")
    for i,categoria in enumerate(categorias):
        print(f"{i+1} - {categoria.titulo}")
    categoria = input("Digite a categoria do evento: ")
    return categoria
    
def criar_evento(evento):
    with open("eventos.txt", "a") as arquivo:
        arquivo.write(f"Titulo: {evento.titulo}\n")
        arquivo.write(f"Data: {evento.data}\n")
        arquivo.write(f"Categoria: {evento.categoria.titulo}\n")
        arquivo.write(f"Data de criacao: {evento.data_criacao}\n")
        arquivo.write("\n")


categoria1 = Categoria("Trabalho")
categoria2 = Categoria("Estudo")
categoria3 = Categoria("Lazer")

categorias = [categoria1, categoria2, categoria3]




titulo = input("Digite o título do evento: ")
data = input("Digite a data do evento: ")
while data < '0' or data >'31':
    print("Data inválida. Digite novamente.")
    data = input("Digite a data do evento: ")


categoria_escolhida = exibir_categorias(categorias)


if not categoria_escolhida.isdigit():
    print("Categoria inválida. Digite novamente.")
    categoria_escolhida = input("Digite a categoria do evento: ")

if int(categoria_escolhida) > len(categorias):
    print("Categoria inválida. Digite novamente.")
    categoria_escolhida = input("Digite a categoria do evento: ")

categoria_escolhida = categorias[int(categoria_escolhida)-1].titulo    
    
categoria_evento = ''

for categoria in categorias:
    if categoria.titulo == categoria_escolhida:
        categoria_evento = categoria
        break

if categoria_evento:
    evento = Evento(titulo, data, categoria_evento,datetime.datetime.now())
    criar_evento(evento)
    print("Evento criado com sucesso!")
else:
    print("Categoria não encontrada!")