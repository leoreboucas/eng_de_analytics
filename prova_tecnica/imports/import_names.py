import pandas as pd

categories = pd.read_csv("./northwind/categories.csv", sep=';', encoding='utf-8')

customers = pd.read_csv("./northwind/customers.csv", sep=';', encoding='utf-8')

employee_territories = pd.read_csv("./northwind/employee_territories.csv", sep=';', encoding='utf-8')

employees = pd.read_csv("./northwind/employees.csv", sep=';', encoding='utf-8')

order_details = pd.read_csv("./northwind/order_details.csv", sep=';', encoding='utf-8')

orders = pd.read_csv("./northwind/orders.csv", sep=';', encoding='utf-8')

products = pd.read_csv("./northwind/products.csv", sep=';', encoding='utf-8')

region = pd.read_csv("./northwind/region.csv", sep=';', encoding='utf-8')

shippers = pd.read_csv("./northwind/shippers.csv", sep=';', encoding='utf-8')

suppliers = pd.read_csv("./northwind/suppliers.csv", sep=';', encoding='utf-8')

territories = pd.read_csv("./northwind/territories.csv", sep=';', encoding='utf-8')

us_states = pd.read_csv("./northwind/us_states.csv", sep=';', encoding='utf-8')
