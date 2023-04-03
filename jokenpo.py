import random
    
def game():
    jokenpo_cpu = random.randint(1,3) 
    print('[1] - Pedra \n[2] - Papel\n[3] - Tesoura')
    choice_player = int(input('Digite sua jogada no JoKenPo:'))
    
    if choice_player == 1:
        print('Você jogou Pedra')
        if jokenpo_cpu != 1:
            if jokenpo_cpu == 2:
                print('O computador escolheu Papel')
            if jokenpo_cpu == 3:
                print('O computador escolheu Tesoura')
            print('Resultado: Você venceu')
        if jokenpo_cpu == 1:
            print('O computador escolheu Pedra\nResultado: Empate')
     
    if choice_player == 2:
            print('Você jogou Papel')
        if jokenpo_cpu != 2:
            if jokenpo_cpu == 1:
                print('O computador escolheu Pedra')
            if jokenpo_cpu == 3:
                    print('O computador escolheu Tesoura')
        print('Resultado: Você venceu')
        if jokenpo_cpu == 2:
            print('O computador escolheu Papel\nResultado: Empate')
            
    if choice_player == 3:
            print('Você jogou Pedra')
        if jokenpo_cpu != 3:
            if jokenpo_cpu == 1:
                print('O computador escolheu Pedra')
            if jokenpo_cpu == 2:
                print('O computador escolheu Papel')
            print('Resultado: Você venceu')
        if jokenpo_cpu == 3:
                print('O computador escolheu Tesoura\nResultado: Empate')

def main():
    game()
main()
