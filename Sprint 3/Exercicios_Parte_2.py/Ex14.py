def imprimir(*args, **kwargs):
 
    for arg in args:
        print(arg)

    for valor  in kwargs.values():
        print(f"{valor}")

imprimir(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)