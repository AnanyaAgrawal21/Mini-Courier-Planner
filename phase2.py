
# Mini-Courier Planner - Phase 2

parcels = [
    {"id": "P1", "weight": 2, "priority": 1, "value": 30},
    {"id": "P2", "weight": 4, "priority": 2, "value": 40},
    {"id": "P3", "weight": 6, "priority": 1, "value": 70},
    {"id": "P4", "weight": 3, "priority": 3, "value": 20},
    {"id": "P5", "weight": 5, "priority": 2, "value": 50}
]

capacity = 10

# 1. Sort parcels by priority
sorted_parcels = sorted(
    parcels, key=lambda p: (p["priority"], p["id"])
)

print("SORTED PARCELS")
for p in sorted_parcels:
    print(p)

# 2. Knapsack Dynamic Programming
n = len(parcels)
dp = [[0] * (capacity + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    weight = parcels[i - 1]["weight"]
    value = parcels[i - 1]["value"]

    for w in range(capacity + 1):
        dp[i][w] = dp[i - 1][w]

        if weight <= w:
            dp[i][w] = max(
                dp[i][w],
                value + dp[i - 1][w - weight]
            )

# 3. Find selected parcels
selected = []
w = capacity

for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        p = parcels[i - 1]
        selected.append(p)
        w -= p["weight"]

selected.reverse()

# 4. Display packing plan
print("\nOPTIMAL PACKING PLAN")

for p in selected:
    print(p["id"], "Weight:", p["weight"], "kg",
          "Value:", p["value"])

total_weight = sum(p["weight"] for p in selected)
total_value = sum(p["value"] for p in selected)

print("Total weight:", total_weight, "kg")
print("Capacity:", capacity, "kg")
print("Total value:", total_value)

# 5. Display DP table
print("\nDP TABLE")
print("Items/Capacity", *range(capacity + 1), sep="\t")

for i, row in enumerate(dp):
    print(i, *row, sep="\t")

print("\nTime Complexity: O(n * capacity)")
print("Space Complexity: O(n * capacity)")
