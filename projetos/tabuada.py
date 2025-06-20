while True:
    def tabuada():
        print("\nTabuada")
        op = input("Escolha a operação:\n+\n-\n÷\nx\n ou então exit para sair: ")
        if op == 'exit':
            return False
        elif op == '+':
            soma()
        elif op == '-':
            sub()
        elif op == '÷':
            div()
        elif op == 'x':
            mult()
        else:
            print("Operação inválida!")
        return True

    def soma():
        print(f"\n1+1={1+1}\n2+2={2+2}\n3+3={3+3}\n4+4={4+4}\n5+5={5+5}\n6+6={6+6}\n7+7={7+7}\n8+8={8+8}\n9+9={9+9}\n10+10={10+10}")

    def sub():
        print(f"\n1-1={1-1}\n2-2={2-2}\n3-3={3-3}\n4-4={4-4}\n5-5={5-5}\n6-6={6-6}\n7-7={7-7}\n8-8={8-8}\n9-9={9-9}\n10-10={10-10}")

    def div():
        print(f"\n1/1={1/1}\n2/2={2/2}\n3/3={3/3}\n4/4={4/4}\n5/5={5/5}\n6/6={6/6}\n7/7={7/7}\n8/8={8/8}\n9/9={9/9}\n10/10={10/10}")

    def mult():
        print(f"\n1*1={1*1}\n2*2={2*2}\n3*3={3*3}\n4*4={4*4}\n5*5={5*5}\n6*6={6*6}\n7*7={7*7}\n8*8={8*8}\n9*9={9*9}\n10*10={10*10}")

    if not tabuada():
        break
