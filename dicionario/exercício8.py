
telefones = {
    "João": "11987654321",
    "Maria": "11912345678",
    "Pedro": "11955556666",
    "Ana": "11999998888",
    "Carlos": "11977776666",
    "Juliana": "11944443333",
    "Lucas": "11922221111",
    "Fernanda": "11988887777"
}

def adicionar_contato(nome, numero):
  telefones[nome] = numero

def remover_contato(nome):
  del telefones[nome]


adicionar_contato('Neide', 11995726648)
print(telefones)
remover_contato('João')
print(telefones)