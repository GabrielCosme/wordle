def check(word, colors, solution):
    for pos, color in enumerate(colors):
        if color == 2:
            if word[pos] != solution[pos]:
                return False
            solution[pos] = '_'

    for pos, color in enumerate(colors):
        if color == 1:
            if word[pos] not in solution:
                return False
            solution[solution.index(word[pos])] = '_'

    for pos, color in enumerate(colors):
        if color == 0:
            if word[pos] in solution:
                return False

    return True

def evaluate(word, solutions):
    value = 0

    for solution in solutions:
        aux = list(word)
        solution = list(solution)
        colors = [0, 0, 0, 0, 0]

        for pos, letter in enumerate(aux):
            if letter == solution[pos]:
                solution[pos] = '_'
                aux[pos] = '_'
                colors[pos] = 2

        for pos, letter in enumerate(aux):
            if letter == '_':
                continue
            if letter in solution:
                solution[solution.index(letter)] = '_'
                colors[pos] = 1

        temp = [test for test in solutions if check(list(word), colors, list(test))]
        value += 1 - len(temp) / len(solutions)

    return value / len(solutions)

def main():
    with open('solutions.txt') as f:
        solutions = f.read().splitlines()

    with open('words.txt') as f:
        words = f.read().splitlines()

    words += solutions

    best = [(word, evaluate(word, solutions)) for word in words]
    best.sort(key=lambda x: x[1], reverse=True)

    for word, value in best:
        print(word, value)

if __name__ == "__main__":
    main()
