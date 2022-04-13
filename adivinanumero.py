from random import randint

def adivina_numero():
    numero_secreto = randint(0, 10)
    ganador = False
    
    for intento in range(0,3):
        numero_pensado = int(input("En que numero estoy pensando? "))

        if numero_pensado == numero_secreto:
           ganador = True
           print("Felicidades, el numero secreto es correcto ")
           break

        elif numero_pensado > numero_secreto:
          print("Mas Bajo")

        else:
         print("Mas Alto")
   
    print('Gracias por jugar')
    
adivina_numero()