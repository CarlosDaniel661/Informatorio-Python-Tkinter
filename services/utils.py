def validate_amount(amount):
    try:
        amount = float(amount)
        return amount > 0
    except ValueError:
        return False

def show_alert_if_needed(amount, threshold=100):
    if amount > threshold:
        print(f"Alerta! Has gastado más que {threshold} en un simple gasto")
