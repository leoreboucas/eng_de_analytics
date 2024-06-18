from imports import import_names as imp

order_details = imp.order_details
products = imp.products

def best_sellers():
    order_details['Faturamento'] = order_details['unit_price'] * order_details['quantity']

    total_revenue = order_details.groupby('product_id').agg({'Faturamento': 'sum'}).reset_index()

    top3_revenue = total_revenue.sort_values(by='Faturamento', ascending=False).head(5)

    top3_revenue_with_names = top3_revenue.merge(products, on='product_id', how='left')

    top3_revenue_with_names = top3_revenue_with_names[['product_name', 'Faturamento']]

    return top3_revenue_with_names

def worst_sellers():
    order_details['Faturamento'] = order_details['unit_price'] * order_details['quantity']

    total_revenue = order_details.groupby('product_id').agg({'Faturamento': 'sum'}).reset_index()

    top3_revenue = total_revenue.sort_values(by='Faturamento', ascending=True).head(5)

    top3_revenue_with_names = top3_revenue.merge(products, on='product_id', how='left')

    top3_revenue_with_names = top3_revenue_with_names[['product_name', 'Faturamento']]

    return top3_revenue_with_names