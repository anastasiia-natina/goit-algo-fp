def greedy_algorithm(items, budget):

    sorted_items = sorted(items.items(), key=lambda item: item[1]["calories"] / item[1]["cost"], reverse=True)

    selected_items = []
    current_cost = 0
    for item_name, item_data in sorted_items:
        if current_cost + item_data["cost"] <= budget:
            selected_items.append(item_name)
            current_cost += item_data["cost"]

    total_calories = 0
    for item_name in selected_items:
        total_calories += items[item_name]["calories"]

    return selected_items, total_calories

def dynamic_programming(items, budget):
    dp = [[0 for _ in range(budget + 1)] for _ in range(len(items) + 1)]

    for i in range(len(items) + 1):
        for j in range(budget + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            else:
                item_name = list(items.keys())[i - 1]
                item_cost = items[item_name]["cost"]
                item_calories = items[item_name]["calories"]

                if item_cost > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - item_cost] + item_calories)

    selected_items = []
    current_cost = budget
    i = len(items)
    while i > 0 and current_cost > 0:
        if dp[i][current_cost] != dp[i - 1][current_cost]:
            selected_items.append(list(items.keys())[i - 1])
            current_cost -= items[list(items.keys())[i - 1]]["cost"]
        i -= 1

    total_calories = 0
    for item_name in selected_items:
        total_calories += items[item_name]["calories"]

    return selected_items, total_calories

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 75

selected_items, total_calories = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print(f"Вибрані страви: {selected_items}")
print(f"Загальна калорійність: {total_calories}")

selected_items, total_calories = dynamic_programming(items, budget)
print("\nАлгоритм динамічного програмування:")
print(f"Вибрані страви: {selected_items}")
print(f"Загальна калорійність: {total_calories}")