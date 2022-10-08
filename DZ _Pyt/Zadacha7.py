# 7. Напишите программу для. 
# проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

X = 1
Y = 1
Z = 1
A = not(X or Y or Z)
B = not X and not Y and not Z
F = A == B
print(F)
