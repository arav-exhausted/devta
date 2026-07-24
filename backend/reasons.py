


def reasons_for_too_much_late(data:dict) -> list[str]:
    reasons=[]

    if data["traffic"] == "Jam":
        reasons.append((
            100,"Heavy traffic is expected to significantly increase delivery time."
        ))

    elif data["traffic"] == "High":
        reasons.append((
            90,"High traffic may delay the delivery."
        ))

    if data["distance"] > 10:
        reasons.append((
            80,"The delivery location is relatively far from the restaurant."
        ))

    if data["festival"] == "Yes":
        reasons.append((
            70,"Festival demand may result in longer delivery times."
        ))

    if ('12' <= data["order_time"] <= '14') or ('19' <= data["order_time"] <= '`21`'):
        reasons.append((
            60,"The order was placed during peak delivery hours."
        ))

    
    if data["multiple_deliveries"] >= 2:
        reasons.append((
            50,"The delivery partner may already be handling multiple orders."
        ))

    
    reasons.sort(key=lambda x: x[0], reverse=True)
    if not reasons:
        reasons.append(
            (0,"No major factors have affected your order this estimate is based on normal delivery conditions")
        )
    return [reason for _, reason in reasons[:2]]