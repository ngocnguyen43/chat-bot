def extract_origin_and_destination(message):
    # Extract origin and destination from the message
    parts = message.split("from")
    if len(parts) == 2:
        print(parts)
        origin, dest_part = (
            parts[0].split("go")[1].strip(),
            parts[1].strip(),
        )
        return origin.strip(), dest_part.strip()
    return None, None


def handle_go_request(message):
    origin, destination = extract_origin_and_destination(message)
    if origin and destination:
        return f"Sure! Here's the link to help you plan your journey from {origin} to {destination}: [link_to_journey_planner]"
    else:
        return "I couldn't understand the origin and destination in your request."


def handle_receipts_or_tickets_request(message):
    if "receipts" in message or "tickets" in message:
        return "Sure! Here's the link to view your receipts/tickets: [link_to_receipts_or_tickets]"
    else:
        return "I couldn't understand what you're looking for."


def chatbot(message):
    # Case 1: If the user wants to go from one place to another
    if "go" in message:
        return handle_go_request(message)

    # Case 2: If the user wants to see receipts or tickets
    elif "receipts" in message or "tickets" in message:
        return handle_receipts_or_tickets_request(message)

    # Default case
    else:
        return "Nah...☹️"
