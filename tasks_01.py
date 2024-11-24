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

# 4.task

# 5.task

# 6.task

# 7.task

# 8.task

# 9.task

# 10.task
