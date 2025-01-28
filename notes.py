# funções

## Example function 1: return the sum of two numbers.
def sum(a, b):
    return a + b

# como em JS, Py funcoes em PY sempre retornan algo, caso esse valor não seja explicito será retornado NONE (undefine no JS)

# Python Generators

## Definition of the generator to produce even numbers.
def all_even():
    n = 0
    while True:
        yield n
        n += 2

my_gen = all_even()

# ## Generate the first 5 even numbers.
for i in range(5):
    print(next(my_gen))

# ## Now go and do some other processing.
do_something = 4
do_something += 3
print(do_something, "oi")

# ## Now go back to generating more even numbers.
for i in range(10):
    print(next(my_gen))


# generators gardam na memoria uma variável(no exemplo acima n) para ser usada mesmo qdo o processo foi interronpido pelo execucao de outra funcao (no exemplo, do_something)

# generator é uma função que age como um interator (loop). Generator gera os elementos que ele mesmo itera.
# generatos podem ser pensandos como "on demand" iterable object

# tipicos interator loop over coleções de dados já existentes que ocupam espaço de memória

print(("------------------------------"))

def f():
    return 1
    return 2
    return 3

print(f())


def g():
    yield 1
    yield 2
    yield 3

print(g())
# retorna um objeto generator (precisamos loop over)

for x in g():
    print (x)
