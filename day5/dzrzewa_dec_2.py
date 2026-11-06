# pip install -U scikit-learn
# Cechy: [wiek w latach, roczne zarobki w tys. zł]
X = np.array([
    [22, 24],
    [32, 28],
    [45, 32],
    [58, 36],
    [24, 44],
    [29, 48],
    [36, 44],
    [44, 52],
    [53, 48],
    [61, 56],
    [25, 72],
    [34, 76],
    [47, 84],
    [60, 92],
])

# 1 = przyznana, 0 = odrzucona
y = np.array([
    0, 0, 0, 0,
    0, 0, 1, 1, 1, 1,
    1, 1, 1, 1,
])
