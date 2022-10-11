# 7. Напишите программу для. 
# проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

X = [0,1]
for i in X:
    for j in X:
        for k in X:
            A = not(i or j or k)
            B = not i and not j and not k
            F = A == B
            print(F)
