# 2)

num = int(input("Informe um número: "))

fibonacci = [0, 1]

while fibonacci[-1] < num:
    next_fibonacci = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next_fibonacci)

if num in fibonacci:
    print(f"{num} pertence à sequência de Fibonacci.")
else:
    print(f"{num} não pertence à sequência de Fibonacci.")

# 5)

string = input("Informe uma string: ")

inverted_string = ""

for i in range(len(string) - 1, -1, -1):
    inverted_string += string[i]

print(inverted_string)