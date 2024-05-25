import random

def simulate_dice_rolls(n):

    sum_counts = [0] * 11

    for _ in range(n):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        sum = roll1 + roll2
        sum_counts[sum - 2] += 1

    probabilities = [count / n for count in sum_counts]
    return probabilities

def main():
    n = 10000

    probabilities = simulate_dice_rolls(n)

    print("Ймовірності сум при киданні двох кубиків (метод Монте-Карло):")
    for i in range(2, 13):
        print(f"{i}: {probabilities[i - 2]:.2f}%")

if __name__ == "__main__":
    main()