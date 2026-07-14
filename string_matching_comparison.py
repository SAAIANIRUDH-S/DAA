import random


# ---------------- Naive String Matching ----------------
def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)

    matches = []
    comparisons = 0

    for i in range(n - m + 1):
        j = 0

        while j < m:
            comparisons += 1

            if text[i + j] != pattern[j]:
                break

            j += 1

        if j == m:
            matches.append(i)

    return matches, comparisons


# ---------------- KMP Algorithm ----------------
def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m

    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1

        elif length != 0:
            length = lps[length - 1]

        else:
            lps[i] = 0
            i += 1

    return lps


def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)

    lps = compute_lps(pattern)

    matches = []
    comparisons = 0

    i = 0
    j = 0

    while i < n:
        comparisons += 1

        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == m:
                matches.append(i - j)
                j = lps[j - 1]

        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches, comparisons


# ---------------- Rabin-Karp Algorithm ----------------
def rabin_karp(text, pattern, q=101):
    n = len(text)
    m = len(pattern)

    d = 256
    h = pow(d, m - 1, q)

    pattern_hash = 0
    text_hash = 0

    matches = []
    comparisons = 0

    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % q
        text_hash = (d * text_hash + ord(text[i])) % q

    for s in range(n - m + 1):

        if pattern_hash == text_hash:

            for j in range(m):
                comparisons += 1

                if text[s + j] != pattern[j]:
                    break
            else:
                matches.append(s)

        if s < n - m:
            text_hash = (
                d * (text_hash - ord(text[s]) * h)
                + ord(text[s + m])
            ) % q

    return matches, comparisons


# ---------------- Main Program ----------------
text = "AABAACAADAABAABA"
pattern = "AABA"

print("========== SMALL EXAMPLE ==========")
print("Text    :", text)
print("Pattern :", pattern)

naive_matches, naive_comp = naive_search(text, pattern)
kmp_matches, kmp_comp = kmp_search(text, pattern)
rk_matches, rk_comp = rabin_karp(text, pattern)

print("\nNaive")
print("Matches      :", naive_matches)
print("Comparisons  :", naive_comp)

print("\nKMP")
print("Matches      :", kmp_matches)
print("Comparisons  :", kmp_comp)

print("\nRabin-Karp")
print("Matches      :", rk_matches)
print("Comparisons  :", rk_comp)


# ---------------- Performance Comparison ----------------
print("\n========== PERFORMANCE COMPARISON ==========")

random.seed(10)

text_large = "".join(random.choices("ABCD", k=10000))

pattern_lengths = [5, 10, 20, 50]

print(f'{"Pattern Length":<18}{"Naive":<12}{"KMP":<12}{"Rabin-Karp":<12}')
print("-" * 54)

for length in pattern_lengths:

    pattern = text_large[100:100 + length]

    _, c1 = naive_search(text_large, pattern)
    _, c2 = kmp_search(text_large, pattern)
    _, c3 = rabin_karp(text_large, pattern)

    print(f"{length:<18}{c1:<12}{c2:<12}{c3:<12}")