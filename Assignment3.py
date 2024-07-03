def encode(message):
    encoded_message = []
    current_char = message[0]
    count = 1

    for char in message[1:]:
        if char == current_char:
            count += 1
        else:
            encoded_message.append(f"{count}{current_char}")
            current_char = char
            count = 1

    encoded_message.append(f"{count}{current_char}")
    return "".join(encoded_message)

test_message = "AAAABBBBCCCCCCCC"
encoded_message = encode(test_message)
print(f"Original Message: {test_message}")
print(f"Encoded Message: {encoded_message}")
