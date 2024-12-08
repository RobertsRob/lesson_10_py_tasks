# 1.task
# Загрузите данные в DataFrame.
# Выберите сотрудников, чей возраст больше 30 лет.
# Отсортируйте их по зарплате по убыванию.
# Добавьте новый столбец "Senior", который будет указывать, старше ли сотрудник 35 лет.

df = pd.read_excel('t1.xlsx')

df_filtered = df[df['Age'] > 30].sort_values('Salary', ascending=False)
df_filtered['Senior'] = df_filtered['Age'] > 35

print(df_filtered)

# 2.task
# Загрузите данные в DataFrame.
# Рассчитайте процент проданных товаров для каждого продукта.
# Отсортируйте товары по этому проценту продаж по убыванию.
# Выберите только те товары, процент продаж которых больше 50%.

df = pd.read_excel('t2.xlsx')

df['Sale Percentage'] = df['Sold'] / df['Quantity'] * 100
df_sorted = df.sort_values('Sale Percentage', ascending=False)
df_filtered = df_sorted[df_sorted['Sale Percentage'] > 50]

print(df_filtered)

# 3.task
# Загрузите данные в DataFrame.
# Отсортируйте заказы по дате.
# Выберите все заказы, сделанные в ноябре 2024 года.
# Рассчитайте общую сумму всех заказов.

df = pd.read_excel('t3.xlsx')

df['Total'] = df['Quantity'] * df['Price']
df_sorted = df.sort_values('Order Date')

df_sorted['Order Date'] = pd.to_datetime(df_sorted['Order Date'])
df_filtered = df_sorted[(df_sorted['Order Date'] >= '2024-11-01') & (df_sorted['Order Date'] <= '2024-11-30')]

print(df_filtered)

# 4.task

# 5.task

# 6.task

# 7.task

# 8.task

# 9.task

# 10.task
