from best import check
from best import evaluate

def main():
    with open('solutions.txt') as f:
        solutions = f.read().splitlines()

    with open('words.txt') as f:
        words = f.read().splitlines()

    words += solutions
    word = "roate"

    print(len(solutions), "possible solutions")
    print("Use word:", word)
    colors = list(map(int, input("Type the resulting colors: ").split(" ")))

    while colors != [2, 2, 2, 2, 2]:
        solutions = [test for test in solutions if check(list(word), colors, list(test))]

        if len(solutions) == 1:
            print("Solution found:", solutions[0])
            break

        print(len(solutions), "possible solutions")

        word = max(words, key=lambda x: evaluate(x, solutions))
        print("Use word:", word)
        colors = list(map(int, input("Type the resulting colors: ").split(" ")))

if __name__ == "__main__":
    main()
