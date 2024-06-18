from imports import import_names as imp

order_details = imp.order_details

def average_tickets():
    ticket_medio = order_details['total'].mean()
    print(f"Ticket Médio: R${ticket_medio:.2f}")