# 1.task
# У вас есть Series с ценами на товары в интернет-магазине. Нужно заменить все цены, которые равны 0, на среднюю цену всех товаров.
# data:
prices = pd.Series([150, 0, 200, 0, 300, 250])

mean_price = prices[prices > 0].mean()
prices = prices.replace(0, mean_price)
print(prices)

# 2.task
# У вас есть Series с результатами тестов учеников. Необходимо проверить, кто не сдал тест, то есть, у кого значение равно NaN. Выведите индексы этих учеников.
# data:
scores = pd.Series([95, 88, None, 76, None, 65], index=["Student1", "Student2", "Student3", "Student4", "Student5", "Student6"])

failed_students = scores[scores.isna()]
print(failed_students)

# 3.task
# У вас есть Series, в которой находятся строки с датами в формате "день/месяц/год". Нужно извлечь из этих строк только год.
# data:
dates = pd.Series(["15/08/2021", "22/12/2020", "01/01/2022", "25/10/2021"])

years = dates.str.split("/").str[2]
print(years)

# 4.task
# В Series с результатами тестов есть значения NaN, которые означают, что тест не был пройден. Замените NaN на 0 и выведите результаты.
# data:
test_scores = pd.Series([80, 90, None, 85, None])

test_scores.fillna(0, inplace=True)
print(test_scores)

# 5.task
# У вас есть Series с температурой в Цельсиях. Нужно преобразовать ее в шкалу Фаренгейта и вывести результат.
# data:
celsius = pd.Series([0, 10, 20, 30, 40])

fahrenheit = celsius * 9/5 + 32
print(fahrenheit)

# 6.task
# Создайте Series с числами от 1 до 10. Используя метод apply(), примените к каждому числу функцию, которая умножает его на 2.
# data:
numbers = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

doubled_numbers = numbers.apply(lambda x: x * 2)
print(doubled_numbers)

# 7.task
# У вас есть Series с данными о продажах товара за 30 дней. Однако некоторые значения (например, 0) явно являются аномальными и не могут быть учтены в расчётах. 
# Задача — очистить данные от таких аномальных значений и подсчитать статистику по оставшимся данным (среднее, стандартное отклонение).
# data
sales = pd.Series([100, 120, 0, 110, 95, 0, 130, 125, 140, 105,
                  98, 0, 112, 115, 130, 140, 150, 0, 125, 118, 
                  110, 100, 105, 98, 120, 110, 95, 135, 140, 0, 130])


clean_sales = sales[sales > 0]

mean_sales = clean_sales.mean()
std_sales = clean_sales.std()

print(f"Среднее значение: {mean_sales}")
print(f"Стандартное отклонение: {std_sales}")

