import sys
from time import sleep
import time 

def lyrics():
    lines = [
        ("Amou daquela vez como se fosse máquina", 0.08, False), 
        ("Beijou sua mulher como se fosse lógico", 0.08, False),
        ("Ergueu no patamar quatro paredes flácidas", 0.07, False),
        ("Sentou pra descansar como se fosse um pássaro", 0.08, False),
        ("E flutuou no ar como se fosse um príncipe", 0.09, False),
        ("E se acabou no chão feito um pacote bêbado", 0.08, False),

        ("Morreu na contramão atrapalhando o sábado.", 0.1, True),
    ]
 
    delays = [0.1, 0.3, 0.08, 0.07, 0.09] * len(lines)
    for i, (line, char_delay, is_colored) in enumerate(lines):
        if is_colored:
            print("\033[91m", end='')  

        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)

        if is_colored:
            print("\033[0m", end='')  

        time.sleep(delays[i])
        print('') 

        if i == 1:
            time.sleep(0.2   )  
        else:
            time.sleep(delays[i])

        if i == 3:
            time.sleep(0.2)  
        else:
            time.sleep(delays[i])

        if i == 5:
            time.sleep(3.2)  
        else:
            time.sleep(delays[i])

lyrics()