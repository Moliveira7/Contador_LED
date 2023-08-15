from pyfirmata import Arduino, util
import time

Uno = Arduino('COM3')
it = util.Iterator(Uno)
it.start()

valD13 = Uno.get_pin('d:13:i')
valD12 = Uno.get_pin('d:12:i')
valD11 = Uno.get_pin('d:11:i')


estadoBt1Ant = True
estadoBt2Ant = True
estadoBt3Ant = True

contador = 0

while True:
    time.sleep(0.15)

    estadoBotao1 = valD11.read()
    estadoBotao2 = valD12.read()
    estadoBotao3 = valD13 .read()

    if estadoBotao1 == 0 and estadoBt1Ant :
        contador += 1
        print(contador)

    if estadoBotao2 == False and estadoBt2Ant :
        contador -= 1
        print(contador)

    if not estadoBotao3 and estadoBt3Ant :
        contador = 0
        print(contador)

    if contador >= 5 :
        Uno.digital[5].write(1)
    else:
        Uno.digital[5].write(0)

    if contador >= 10 :
        Uno.digital[6].write(1)
    else:
        Uno.digital[6].write(0)

    if contador >= 15 :
        Uno.digital[7].write(1)
    else:
        Uno.digital[7].write(0)


    estadoBt1Ant = estadoBotao1
    estadoBt2Ant = estadoBotao2
    estadoBt3Ant = estadoBotao3
        
