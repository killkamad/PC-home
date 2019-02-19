from typing import Any, Sequence, Dict, Callable

class Bird:
    def scream(self, n: int):
        return "A" * n

class Fox:
    def scream(self)-> str:
        return "What should i say?"

lst1=[Bird(),Bird()]
lst2=[Fox(),Fox()]

# def f(s:str):
#     print(s*3)

# f(lst1[0].scream(5))
# Bird().scream(n=5)

def f(lst: Sequence[int],func:Callable[[int],int]):
    for i in lst:
        print(func(i))

def f2(a:int)-> int:
    return a*a

f([1, 2, 3, 4, 5],f2)

print(list(map(f2,[1, 2, 3, 4, 5])))