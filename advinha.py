import random
import time
x = random.randint(1,100)
print("Advinhe o número de 1 a 110, você tem 5 tentaivas")
c = 5
for i in range(5):
    time.sleep(14)
    num = int(input('Digite o Número: '))
    if x == num:
        print("VOCÊ ACERTOU!!!")
        break
    else:
        time.sleep(1)
        c -=1
        print('você errou :), mas ainda tem {} tentativas'.format(c))
        time.sleep(2)
        print("Você tem uma dica:")
        time.sleep(2)
        if i == 0:
            if x >= 50:
                print('O numero é maior ou igual a 50')
            else:
                print('O numero é menor que 50')
        if i == 1:
            if x % 2 == 0:
                print('O numero é par')
            else:
                print('O numero é impar')
        
        if i == 2:
            if (x % 3 == 0) and (x % 5 != 0):
                print('O numero é divisvel por 3, mas não por 5')
            elif (x % 3 == 0) and (x % 5 == 0):
                print('O numero é divisivel por 3 e 5')
            elif (x % 3 != 0) and (x % 5 == 0):
                print('O numero é divisivel por 5, mas não por 3')
            else:
                print('O numero não é divisivel por 3 e 5')
        if i == 3:
            y = x % 10
            z = (x - y)
            z = z / 10
            z = z % 10
            m = 1
            while True:
                if z > 10:
                    print('O numero está entre 1 a 9')
                    break
                if z == m:
                    print('O numero é da dezena {}0'.format(m))
                    break
                m +=1
        if i == 4:
            if x > num:
                print('O numero é maior que {}'.format(num))
            else:
                print('O numero é menor que {}'.format(num))
            num = int(input())
            if x == num:
                print('VOCÊ GANHOUUU!!!!!')
            else:
                print('você perdeu:), o numero era {}'.format(x))
