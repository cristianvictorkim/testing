from app.discounts import calculate_total


def request_subtotal() -> float:
    subtotal_text = input("Ingrese el subtotal de la compra: ")
    return float(subtotal_text)


def request_customer_type() -> str:
    return input("Ingrese el tipo de cliente (regular, premium o vip): ")


def main() -> None:
    try:
        subtotal = request_subtotal()
        customer_type = request_customer_type()
        result = calculate_total(subtotal, customer_type)
    except ValueError as error:
        print(f"Error: {error}")
        return

    print(f"Subtotal: ${result.subtotal}")
    print(f"Cliente: {result.customer_type}")
    print(f"Descuento: ${result.discount_amount}")
    print(f"Total final: ${result.total}")


if __name__ == "__main__":
    main()
