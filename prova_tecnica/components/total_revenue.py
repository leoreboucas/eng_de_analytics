from imports import import_names as imp

def total_revenue():
    order_details = imp.order_details

    order_details['total'] = order_details['unit_price'] * order_details['quantity']

    total = order_details['total'].sum()

    print(f"Faturamento total da empresa: R${total:.2f}")