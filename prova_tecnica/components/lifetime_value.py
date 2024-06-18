from imports import import_names as imp

orders = imp.orders
order_details = imp.order_details

def ltv():

    ordermerge = orders.merge(order_details)

    receita_media_por_cliente = ordermerge.groupby('customer_id').sum()['total'].mean()
    media_pedidos_por_cliente = ordermerge.groupby('customer_id').size().mean()
    ltv = receita_media_por_cliente * media_pedidos_por_cliente

    print(f"Lifetime Value (LTV): R${ltv:.2f}")