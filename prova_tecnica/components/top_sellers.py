from imports import import_names as imp

order_details = imp.order_details
products = imp.products

def best_sellers():
    order_details['Faturamento'] = order_details['unit_price'] * order_details['quantity']

    faturamento_total = order_details.groupby('product_id').agg({'Faturamento': 'sum'}).reset_index()

    top3_faturamento = faturamento_total.sort_values(by='Faturamento', ascending=False).head(5)

    top3_faturamento_com_nomes = top3_faturamento.merge(products, on='product_id', how='left')

    top3_faturamento_com_nomes = top3_faturamento_com_nomes[['product_name', 'Faturamento']]

    return top3_faturamento_com_nomes

def worst_sellers():
    order_details['Faturamento'] = order_details['unit_price'] * order_details['quantity']

    faturamento_total = order_details.groupby('product_id').agg({'Faturamento': 'sum'}).reset_index()

    top3_faturamento = faturamento_total.sort_values(by='Faturamento', ascending=True).head(5)

    top3_faturamento_com_nomes = top3_faturamento.merge(products, on='product_id', how='left')

    top3_faturamento_com_nomes = top3_faturamento_com_nomes[['product_name', 'Faturamento']]

    return top3_faturamento_com_nomes