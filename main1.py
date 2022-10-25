import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
celsius = [[-67.0], [-34.0], [0], [34.0], [54.0], [67.0], [100]]
fahrenheit = [[-88.0], [-29.0], [32.0], [93.2], [129.2], [129.2], [152.6]]
plt.figure(figsize=(15, 8), dpi=50)

plt.scatter(celsius, fahrenheit, label='входные значения', color='green', marker='$f$',)
plt.xlabel('celsius')
plt.ylabel('fahrenheit')
plt.legend()
plt.grid(True)
plt.show()

for c, f in zip(celsius, fahrenheit):
    print(f'цельсия{c}= фаренгейт {f}')

lr = LinearRegression()
lr.fit(celsius, fahrenheit)
lr.predict([[256],[123]])
celsius_test = [[-50], [10], [30], [20], [70], [87]]
fahrenheit_test = lr.predict(celsius_test)


for c, f in zip(celsius_test, fahrenheit_test):
    print(f'цельсия {c} фаренгейта{f}')

x_range = np.arange(-70, 120)
y_range = x_range*1.8+32
plt.figure(figsize=(15, 8), dpi=280)
plt.plot(x_range, y_range, label='уравнение', linewidth=1)
plt.scatter(celsius, fahrenheit, label='входные  данные', color='green')
plt.scatter(celsius_test, fahrenheit_test, label=' предсказанное значение', color='blue')
plt.xlabel('Цельсия')
plt.ylabel('Фаренгейта')
plt.legend()
plt.grid(True)
plt.show()

