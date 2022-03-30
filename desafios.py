

def desafio001():
  print("olá mundo")

        
def desafio002():
  nome = input('qual é o seu nome:')
  print('é um prazer te conhecer {}!' .format(nome))

def desafio003():
  n1 = int(input('digite um valor:'))
  n2 = int(input('outro numero:'))
  s = n1 + n2
  print('a soma entre {} e {} é igual a {}!' .format(n1, n2, s))

def desafio004():
  a = input('digite algo :')
  print('o tipo dessa string foi:', type(a))



def desafio005():
  n = int (input('digite um numero:'))
  print ('analisando o valor {}, seu antecessor foi {} e o seu sucessor foi {}' .format(n, (n-1), (n+1)))

def desafio006():
  n = int(input('digite um numero: '))
  print('o dobro de {} vale {}.'.format(n, (n*2)))
  print('o triplo de {} foi {}'.format (n, (n*3)))
  
   
def desafio007():
  n1 = float(input('primeira nota do aluno:'))
  n2 = float(input('segunda nota do aluno:'))
  média = (n1 + n2) / 2
  print('a média entre {} e {} é igual a {}'.format(n1, n2, média))

def desafio008():
  medida = float(input('uma distância em metros: '))
  cm = medida * 100
  mm = medida * 1000
  print ('a medida de {}m corresponde a {}cm e {}mm'.format(medida, cm, mm))

def desafio009():
  numero = int(input('digite um numero para ver sua tabuada :'))
  print('-' * 12)
  print('{} * {:2} = {}'.format(numero, 1, numero*1))
  print('{} * {:2} = {}'.format(numero, 2, numero*2))
  print('{} * {:2} = {}'.format(numero, 3, numero*3))
  print('{} * {:2} = {}'.format(numero, 4, numero*4))
  print('{} * {:2} = {}'.format(numero, 5, numero*5))
  print('{} * {:2} = {}'.format(numero, 6, numero*6))
  print('{} * {:2} = {}'.format(numero, 7, numero*7))
  print('{} * {:2} = {}'.format(numero, 8, numero*8))
  print('{} * {:2} = {}'.format(numero, 9, numero*9))
  print('{} * {:2} = {}'.format(numero, 10, numero*10))
  print('-' * 12)

  #para quando quizer deixar                                     algum codigo bonitinho: "print('-' * 12)"


def desafio0010():
  real = float(input('quanto dinheiro você tem na carteira?r$ '))
  dolar = real/3.37
  print('com R$ {:.2f} você pode comprar US$ {:.2f}'.format(real, dolar)) 

def desafio0011():
  largura = float(input('largura da parede:'))
  alt = float(input('altura da parede:'))
  área = largura*alt
  print('sua parede tem a dimensão de {}*{} e sua área é de {}m²'.format(largura, alt, área))
  tinta = área / 2
  print('para pintar essa parede, você precisará de {}litros de tinta'.format(tinta))

def desafio0012():
  preço = float(input('qual é o preço do produto? R$'))
  novo =  preço - (preço * 5 / 100)
  print('o produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${}'.format(preço, novo))

def desafio0013():
  salário = float(input('qual é o salário do funcionário?: '))
  ns = salário + (salário * 15/100)
  print('um funcionário que ganhava R${:.2f} com 15% de aumento ficou R${}'.format(salário, ns))

def desafio0014():
  c = float(input('informe a temperatura neste momento em °C:'))
  f = 9 * c/ 5 + 32 
  print('a temperatura de {}°C corresponde a {}F'.format(c, f))


def desafio0015():
  dias = int(input('quantos dias alugados: '))
  km = float(input('quantos km rodados:'))
  pagos = (dias * 60)  +  (km * 0.15)
  print('o total a pagar é de R${}'.format(pagos))

#16
from math import trunc
def desafio0016(): 
 numero = float(input('digite um numero: '))
 print (f'o valor digitado foi:{numero}, e sua porçao inteira é {trunc(numero)}')

from math import hypot
def desafio0017():
  co = float(input('digite o valor do cateto oposto: '))
  ca = float(input('digite o valor do cateto adjacente: '))
  print(f'o valor da hypotenusa foi {hypot(co, ca):.2f}')

from math import sin, cos, tan, radians
def desafio0018():
  ang = float(input('digite um ângulo:'))
  print(f'o angulo de: {ang} tem o seno de: {sin(radians(ang)):.2f}')
  print(f'o angulo de: {ang} tem o cosseno de {cos(radians(ang)):.2f}')
  print(f'o angulo de: {ang} tem a tangente de {tan(radians(ang)):.2f}')

from random import choice
def desafio0019():
  name1 = str(input('digite o primeiro nome:'))
  name2 = str(input('digite o segundo nome:'))
  name3 = str(input('digite o terceiro nome:'))
  name4 = str(input('digite o quarto nome:'))
  lista = [name1, name2, name3, name4]
  escolhido = choice(lista)
  print(f"o aluno escolhido foi:{escolhido}")

from random import shuffle
def desafio0020():
  name01 = input('digite o primeiro nome:')
  name02 = input('digite o segundo nome:')
  name03 = input('digite o terceiro nome:')
  name04 = input('digite o quarto nome:')
  lista = [name01, name02, name03, name04]
  shuffle(lista)
  print(f'a ordem será:')
  print(lista)


 #desafio0021(fiz no pygame aqui não dar pra fazer )
  

def desafio0022():
  name = str(input('digite seu nome completo:')).strip()
  print('analisando seu nome...')
  print(f'seu nome em maiusculas fica:{name.upper()}')
  print(f'seu nome em minusculas fica: {name.lower()}')
  print(f'seu nome tem ao todo {len(name) - name.count(" ")} letras')
  print(f'seu primeiro nome tem:{name.find(" ")} letras')


def desafio0023():
  num = int(input('informe um número:'))
  u = num // 1 % 10
  d = num // 10 % 10
  c = num // 100 % 10
  m = num // 1000 % 10
  print(f'analizando o número:{num}')
  print(f'unidade:{u}')
  print(f'dezena:{d}')
  print(f'centena:{c}')
  print(f'milhar:{m}')

def desafio0024():
 cid = (input('em que cidade você nasceu?:')).strip()
 print(cid[:5].upper() == 'SANTO')

def desafio0025():
  name = input('digite seu nome completo:')
  print(f'seu nome tem silva?{"silva" in name.lower()}')

def desafio0026():
  f = str(input('digite uma frase:')).upper().strip()
  print(f'a letra A aparece {f.count ("A")} vez(es)')
  print(f'a primeira letra A apareceu na posição {f.find("A")+1}')
  print(f'a última letra A apareceu na {f.rfind("A")+ 1}')

def desafio0027():
  name = str(input('digite seu nome completo:')).strip()
  nome = name.split()
  print(f'muito prazer em te conhecer!{name}')
  print(f'seu primeiro nome é {nome[0]}')
  print(f'seu último nome é {nome[len(nome)-1]}')

from random import randint
from time import sleep
def desafio0028():
  computador = randint(0, 5)
  print('-*-' * 18)
  print('vou pensar em um número entre 0 e 5 tente adivinhar...')
  print('_*_' * 18)
  gamer = int(input('tente adivinhar em qual número o computador irá pensar:'))
  print('PROCESSANDO...')
  sleep(3)
  if gamer == computador:
    print(f'pensei no número:{computador}, acertou miseraavi*_*')
  else:
    print('pensei no numero:{} errou em cheio@_@'.format(computador))
  

def desafio0029():
 velocidade = int(input('qual a velocidade do carro?:'))  
 multa = (velocidade - 80) * 7
 if velocidade > 80:
   print(f'MUTADO! você passou do limite de velocidade de 80km/h para {velocidade}')
   print(f'você deve pagar:R$ {multa} de multa')
 print('tenha um bom dia dirija com segurança^_^')

def desafio0030():
  n1 = float(input('me diga um número qualquer:'))
  resultado = n1 % 2
  if resultado == 0:
   print('o número é par')
  else:
   print('o número é ímpar')
   
def desafio0031():
  distância = float(input('qual a distância da sua viagem?:'))
  print(f'você estar prestes a começar uma viagem de {distância} km')
  if distância <= 200:
    preço = distância * 0.50
  else:
    preço = distância * 0.45
  print(f'sua passagem custará: {preço} reais')



def desafio0032():
  from datetime import date
  ano = int(input('que ano quer analisar?digite 0 para analisar o ano atual:'))
  if ano == 0:
   ano = date.today().year
  if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
   print(f'o ano de {ano} é BISSEXTO!')
  else:
   print(f'o ano de {ano} NÃO é BISSEXTO')

def desafio0033():
  a = float(input('primeiro valor:'))
  b = float(input('segundo valor:'))
  c = float(input('terceiro valor:'))
  menor = a
  if b<a and b<c:
    menor = b
  if c<a and c<b:
    menor = c
  maior = a
  if b>a and b>c:
    maior = b
  if c>b and c>a:
    maior = c
  print(f'o menor número digitado foi: {menor}')
  print(f'o maior valor digitado foi: {maior}')


def desafio0034():
  salário = float(input('digite o salário do funcionário:'))
  if salário <= 1250:
    novo = salário + (salário * 15 / 100 )
    print(f'o novo salário de quem ganhava menos ou igual R$ 1250 passa a ser:R$ {novo}')
  else:
    novo = salário + (salário * 10 / 100)
    print(f'o novo salário de quem ganhava mais que 1250 passa a ser: {novo}')

def desafio0035():
  print('=+='* 8)
  print('analisador de triângulos')
  print('=+='* 8)
  t1 = float(input('primeiro seguimento:'))
  t2 = float(input('segundo seguimento:'))
  t3 = float(input('terceiro seguimento:'))
  if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print('os seguimentos a cima PODEM formar um triângulo!')
  else:
    print('os seguimentos NÃO PODEM formar um triângulo!')
    