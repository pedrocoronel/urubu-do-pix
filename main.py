import time
import os

# logo
# menu
# tabela + valor q eu vou colocar

logo = '''
  _   _ ____  _   _ ____  _   _
 | | | |  _ \| | | |  _ \| | | |
 | | | | |_) | | | | |_) | | | |
 | |_| |  _  < |_| | |__)| |_| |
 |_____|_| \_|_____|_____/_____|
  ____  _____    ____  _ _    _
 |  _ \|  _  |  |  _ \| | \  / /
 | | | | | | |  | |_) | |\ \/ /
 | |_| | |_| |  |  __/| |/ /\ \ 
 |____/|_____|  |_|   |_|_/  \_\ v1.0

'''

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def inicio():
	print(logo)
	time.sleep(1)

espaco = " "

def info():
	print(espaco * 12,"[X] Seguro")
	print(espaco * 12,"[X] Rapido")
	print(espaco * 12,"[X] Facil")
	print("\n")
	print(espaco * 12,"iniciando...")
	print("\n")
	time.sleep(4)
	clear()

def menu():
	inicio()
	print("Tabela Trading")
	print("$200 Retorno 2000")
	print("$250 Retorno 2500")
	print("$300 Retorno 3000")
	print("$350 Retorno 3500")
	print("$400 Retorno 4000")
	print("$500 Retorno 5000")
	valor = input("Valor: ")
	return valor

def main():
	while True:
		clear()
		inicio()
		info()
		menu()

if __name__ == "__main__":
	main()
