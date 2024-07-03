import re

def fetch_phone_numbers(s):
    phone_numbers = re.findall(r'\+91 \d{10}', s)
    return phone_numbers

# Example usage
input_str = "My name is Rushikesh. My phone number is +91 8766525204. Also I have an alternative phone number +91 6764345644"
phone_numbers = fetch_phone_numbers(input_str)
print(phone_numbers)
