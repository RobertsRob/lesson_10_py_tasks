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
# Загрузите данные в DataFrame.
# Заполните пропущенные значения в столбце Discount средним значением.
# Заполните пропущенные значения в столбце Total произведением Quantity на Price (если данные по этим столбцам есть).
# Выведите итоговую таблицу с заполенными пропусками.

df = pd.read_excel('t4.xlsx')

df['Discount'] = df['Discount'].fillna(df['Discount'].mean())
df['Total'] = df.apply(lambda row: row['Quantity'] * row['Price'] if pd.isna(row['Total']) else row['Total'], axis=1)

print(df)

# 5.task
# Загрузите данные в DataFrame.
# Заполните пропуски в столбце Age медианным значением.
# Заполните пропуски в столбце Grade средним значением по этому столбцу.
# Выведите итоговую таблицу с заполенными данными.

df = pd.read_excel('t5.xlsx')

df['Age'] = df['Age'].fillna(df['Age'].median())
df['Grade'] = df['Grade'].fillna(df['Grade'].mean())

print(df)
