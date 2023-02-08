def func( a, b = 5, c = 10):
    print('a equal', a, ', b equal to', b, ', c equal to', c)

func(3, 7)
func(24, c = 24)
func(c=50, a=100)
                                #Если имеется некоторая функция с большим числом параметров, и при её вызове тре-
                                #буется указать только некоторые из них, значения этих параметров могут задаваться по
                                #их имени – это называется ключевые параметры. В этом случае для передачи аргументов
                                #функции используется имя (ключ) вместо позиции (как было до сих пор).
                                
                                #Есть два преимущества такого подхода: во-первых, использование функции становится
                                #легче, поскольку нет необходимости отслеживать порядок аргументов; во-вторых, можно
                                #задавать значения только некоторым избранным аргументам, при условии, что осталь-
                                #ные параметры имеют значения аргумента по умолчанию.'''