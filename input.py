
"""
Example 1
"""
def calculate_heterogeneity(text, keyboard_mapping):
    heterogeneity = 0
    K = len(text)

    for i in range(1, K):
        char1 = text[i - 1]
        char2 = text[i]

        key1, row1 = keyboard_mapping[char1]
        key2, row2 = keyboard_mapping[char2]

        if row1 != row2:
            heterogeneity += 1

    return heterogeneity


def generate_permutations(arr, l, r, all_permutations, curr_permutation):
    if l == r:
        all_permutations.append(curr_permutation[:])
    else:
        for i in range(l, r + 1):
            arr[l], arr[i] = arr[i], arr[l]
            curr_permutation[l], curr_permutation[i] = curr_permutation[i], curr_permutation[l]
            generate_permutations(arr, l + 1, r, all_permutations, curr_permutation)
            arr[l], arr[i] = arr[i], arr[l]
            curr_permutation[l], curr_permutation[i] = curr_permutation[i], curr_permutation[l]


def find_optimal_keyboard(N, ci, ri, K, sj):
    keyboard_mapping = {}

    for i in range(N):
        keyboard_mapping[ci[i]] = (i, ri[i])

    max_diversity = float('-inf')
    optimal_keyboard = None
    all_rows_combinations = []
    generate_permutations(list(range(N)), 0, N - 1, all_rows_combinations, list(range(N)))

    for rows_combination in all_rows_combinations:
        permuted_ci = [ci[i] for i in rows_combination]
        keyboard_mapping = {permuted_ci[i]: (i, ri[i]) for i in range(N)}
        diversity = calculate_heterogeneity(sj, keyboard_mapping)

        if diversity > max_diversity:
            max_diversity = diversity
            optimal_keyboard = rows_combination

    rows_in_optimal_layout = max(ri[i] for i in optimal_keyboard)

    return rows_in_optimal_layout


N = int(input())
ci = list(map(int, input().split()))
ri = list(map(int, input().split()))
K = int(input())
sj = list(map(int, input().split()))
rows_in_optimal_layout = find_optimal_keyboard(N, ci, ri, K, sj)
print(rows_in_optimal_layout)


"""
Example 2
____________________________________________________________________________________________
"""


def calculate_heterogeneity(text, keyboard_mapping):
    heterogeneity = 0
    K = len(text)

    for i in range(1, K):
        char1 = text[i - 1]
        char2 = text[i]

        key1, row1 = keyboard_mapping[char1]
        key2, row2 = keyboard_mapping[char2]

        if row1 != row2:
            heterogeneity += 1

    return heterogeneity


def generate_permutations(arr, l, r, all_permutations, curr_permutation):
    if l == r:
        all_permutations.append(curr_permutation[:])
    else:
        for i in range(l, r + 1):
            arr[l], arr[i] = arr[i], arr[l]
            curr_permutation[l], curr_permutation[i] = curr_permutation[i], curr_permutation[l]
            generate_permutations(arr, l + 1, r, all_permutations, curr_permutation)
            arr[l], arr[i] = arr[i], arr[l]
            curr_permutation[l], curr_permutation[i] = curr_permutation[i], curr_permutation[l]


def find_optimal_keyboard(N, ci, ri, K, sj):
    keyboard_mapping = {}

    for i in range(N):
        keyboard_mapping[ci[i]] = (i, ri[i])

    max_diversity = float('-inf')
    optimal_keyboard = None
    all_rows_combinations = []
    generate_permutations(list(range(N)), 0, N - 1, all_rows_combinations, list(range(N)))

    for rows_combination in all_rows_combinations:
        permuted_ci = [ci[i] for i in rows_combination]
        keyboard_mapping = {permuted_ci[i]: (i, ri[i]) for i in range(N)}
        diversity = calculate_heterogeneity(sj, keyboard_mapping)

        if diversity > max_diversity:
            max_diversity = diversity
            optimal_keyboard = rows_combination

    rows_in_optimal_layout = len(set(ri[i] for i in optimal_keyboard))

    return rows_in_optimal_layout


N = 3
ci = [42, 3, 14]
ri = [1, 3, 3]
K = 4
sj = [3, 14, 14, 3]

rows_in_optimal_layout = find_optimal_keyboard(N, ci, ri, K, sj)
print(rows_in_optimal_layout)


def max_ideal_sculptures(N, sculptures, X, T):
    sculptures.sort()
    max_ideals = 0

    for sculpture in sculptures:
        if T <= 0:
            break

        difference = abs(X - sculpture)

        if T >= difference:
            max_ideals += 1
            T -= difference

    return max_ideals


if __name__ == '__main__':
    N, X, T = map(int, input().split())
    sculptures = list(map(int, input().split()))

    result = max_ideal_sculptures(N, sculptures, X, T)
    print(result)


def max_ideal_sculptures(N, sculptures, X, T):
    sculptures.sort()
    max_ideals = 0

    for sculpture in sculptures:
        if T <= 0:
            break

        difference = abs(X - sculpture)

        if T >= difference:
            max_ideals += 1
            T -= difference

    return max_ideals

# Test Example 1
N1, X1, T1 = 3, 5, 2
sculptures1 = [4, 2, 5]
result1 = max_ideal_sculptures(N1, sculptures1, X1, T1)
print(result1)  # Output: 2

# Test Example 2
N2, X2, T2 = 5, 19, 32
sculptures2 = [36, 10, 72, 9, 50]
result2 = max_ideal_sculptures(N2, sculptures2, X2, T2)
print(result2)  # Output: 2

# Test Example 3
N3, X3, T3 = 4, 25, 10
sculptures3 = [1, 10, 42, 9]
result3 = max_ideal_sculptures(N3, sculptures3, X3, T3)
print(result3)  # Output: 0

def max_profit_with_transactions(N, prices):
    # Initialize variables to track the maximum profit and the days of buying and selling shares
    dp = [[0] * 5 for _ in range(N)]
    transactions = [[(0, 0)] * 5 for _ in range(N)]

    for t in range(1, 5):
        max_diff = -prices[0]

        for i in range(1, N):
            # Calculate the maximum profit after t-th transaction on the i-th day
            dp[i][t] = max(dp[i-1][t], prices[i] + max_diff)

            # Update the days of buying and selling shares for the current transaction
            if prices[i] + max_diff > dp[i-1][t]:
                transactions[i][t] = (transactions[i-1][t-1][0], i)
            else:
                transactions[i][t] = transactions[i-1][t]

            # Update the maximum difference considering the previous transaction
            max_diff = max(max_diff, dp[i][t-1] - prices[i])

    # Find the best transaction days by backtracking
    best_transactions = []
    i, t = N - 1, 4
    while t > 0:
        buy_day, sell_day = transactions[i][t]
        if buy_day == 0:
            break
        best_transactions.append((buy_day, sell_day))
        i, t = buy_day - 1, t - 1

    best_transactions.reverse()

    return len(best_transactions), best_transactions

# Test Example 1
N1 = 5
prices1 = [3, 5, 2, 7, 1]
K1, transactions1 = max_profit_with_transactions(N1, prices1)
print(K1)  # Output: 2
for buy_day, sell_day in transactions1:
    print(buy_day, sell_day)

# Test Example 2
N2 = 5
prices2 = [5, 7, 3, 4, 2]
K2, transactions2 = max_profit_with_transactions(N2, prices2)
print(K2)  # Output: 1
for buy_day, sell_day in transactions2:
    print(buy_day, sell_day)

# Test Example 3
N3 = 3
prices3 = [3, 3, 3]
K3, transactions3 = max_profit_with_transactions(N3, prices3)
print(K3)  # Output: 0


def find_countries(classmates_info, countries_info):
    results = {}

    for classmate in classmates_info:
        eligible_countries = []

        for country in countries_info:
            income_req = country['income']
            education_req = country['education']
            parent_citizenship_req = country['parent_citizenship']

            if (classmate['income'] >= income_req and
                    (not education_req or classmate['education']) and
                    (parent_citizenship_req == 0 or parent_citizenship_req == classmate['parent_citizenship'])):
                eligible_countries.append(country['name'])

        eligible_countries.sort()
        results[classmate['name']] = eligible_countries

    return results


# Example usage:
if __name__ == '__main__':
    N = 3
    income = [25000, 22000, 30000]
    education = [1, 1, 1]
    parent_citizenship = [1, 1, 0]

    countries_info = []
    for i in range(N):
        country = {
            'name': i + 1,
            'income': income[i],
            'education': education[i],
            'parent_citizenship': parent_citizenship[i]
        }
        countries_info.append(country)

    Q = 2
    classmates_income = [20000, 30000]
    classmates_education = [1, 0]
    classmates_parent_citizenship = [1, 0]

    classmates_info = []
    for j in range(Q):
        classmate = {
            'name': j + 1,
            'income': classmates_income[j],
            'education': classmates_education[j],
            'parent_citizenship': classmates_parent_citizenship[j]
        }
        classmates_info.append(classmate)

    results = find_countries(classmates_info, countries_info)
    for classmate, countries in results.items():
        if countries:
            print(countries[0], end=' ')
        else:
            print(0, end=' ')


def spell_strength(s, m, d):
    strength = 0
    character_counts = [0] * 26

    for i in range(len(s)):
        k = ord(s[i]) - ord('a')
        m_i = m[i]

        if m_i == 0:
            character_counts[k] += 1
        else:
            new_k = (k + (m_i - 1) * d[i]) % 26
            character_counts[new_k] += 1

    for count in character_counts:
        if count > 0:
            strength += 1

    return strength

if __name__ == '__main__':
    N, K = map(int, input().split())
    S = input().strip()
    p = list(map(int, input().split()))
    d = list(map(int, input().split()))

    total_strength = 0
    for k in range(1, K + 1):
        for i in range(1, N + 1):
            current_i = i
            spell = S[current_i - 1]

            for j in range(k - 1):
                current_i = p[current_i - 1]
                spell += S[current_i - 1]

            strength = spell_strength(spell, [0] * len(spell), d)
            total_strength += strength

    print(total_strength)
