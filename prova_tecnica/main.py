import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
from components import top_sellers

from components import top_sellers, total_revenue, average_tickets, lifetime_value, top_employees
from imports import import_names as imp
from presentation import presentation

# Faturamento total

total_revenue.total_revenue()

# # # TOP 3 mais vendidos

better_products = top_sellers.best_sellers()
plt.figure(figsize=(10, 10))
sns.barplot(x=better_products['product_name'], y=better_products['Faturamento'])
plt.title('Top 5 Produtos Mais Vendidos')
plt.xlabel('Produtos')
plt.ylabel('Faturamento Total')
plt.show()

# # # TOP 3 menos vendidos

worst_products = top_sellers.worst_sellers()
plt.figure(figsize=(10, 10))
sns.barplot(x=worst_products['product_name'], y=worst_products['Faturamento'])
plt.title('Top 5 Produtos Menos Vendidos')
plt.xlabel('Produtos')
plt.ylabel('Faturamento Total')
plt.show()

#  Cálculo do ticket médio

average_tickets.average_tickets()

# Receitas por cliente

lifetime_value.ltv()

# Empregados com melhores vendas

employess_revenue = top_employees.top_employees()
full_name = employess_revenue['first_name'] + ' ' + employess_revenue['last_name']
plt.figure(figsize=(10, 10))
sns.barplot(x=full_name, y=employess_revenue['Faturamento'])
plt.title('Faturamento de venda dos funcionários')
plt.xlabel('Nome dos funcionários')
plt.ylabel('Faturamento por funcionário')
plt.show()

