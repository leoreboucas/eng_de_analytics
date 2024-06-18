from imports import import_names as imp

orders = imp.orders
order_details = imp.order_details
employees = imp.employees

def top_employees():

    orders_merge = orders.merge(order_details)

    employees_sells = orders_merge.groupby('employee_id').sum()['Faturamento'].reset_index()

    sort_employees = employees_sells.sort_values(by='Faturamento', ascending=False).head(9)

    topthree_employees = sort_employees.merge(employees, on='employee_id', how='left')
    topthree_employees_names = topthree_employees[['employee_id', 'first_name', 'last_name', 'Faturamento']]

    return topthree_employees_names