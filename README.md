# TypeInferSemantics
Project made for the course of Semantics, of Universidade Federal do Rio Grande do SUl

Exemplo execução de um teste do arquivo test_tlet.py:

python3 -m Tests.test_tlet


Observações:
Na hora de definir uma função que é chamada pela main_function e que por sua vez também chama a main_function, colocar: from mainFunction import main_function dentro da definição da função!!

E não esquecer de acrescentar um import no arquivo mainFunction, como por exemplo:

from Functions.Tletrec import *

Para rodar:

python3 mainFunction

Pra rodar outro arquivo que não esteja no mesmo nível da mainFunction:

python3 -m Pasta.arquivo
