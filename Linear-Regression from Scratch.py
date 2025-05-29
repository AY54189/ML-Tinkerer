X = [1, 2, 3, 4, 5]
Y = [27, 51, 81, 105, 140]

m = 0  # Slope
c = 0  # Intercept
L = 0.005  # Learning rate
iteration = 10000  # Cycles
n = len(X)

m_values = []
c_values = []
mse_values = []

for step in range(iteration):
    y_pred = [m * x + c for x in X]

    dm = (-2 / n) * sum([x * (y - y_pred[i]) for i, (x, y) in enumerate(zip(X, Y))])
    dc = (-2 / n) * sum([(y - y_pred[i]) for i, y in enumerate(Y)])

    m -= L * dm
    c -= L * dc

    mse = sum([(y - y_pred[i])**2 for i, y in enumerate(Y)]) / n
    m_values.append(m)
    c_values.append(c)
    mse_values.append(mse)

    if step % 100 == 0:
        print(f"Step {step}: m={m:.4f}, c={c:.4f}, MSE={mse:.4f}")

print(f"\nFinal equation: y = {m:.2f}x + {c:.2f}")

#"Feel free to play around with the m, c, L, and iteration variables.
