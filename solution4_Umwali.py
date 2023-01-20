mport re

isbn_pattern = re.compile(r"^ISBN \d{3}.\d.\d{3}.\d{5}.\d$")

isbn_number = input("Test, eg: ISBN 978-0-306-40615-7")

match = isbn_pattern.match(isbn_number)

if match:
    print("Valid ISBN number.")
else:
    print("Invalid ISBN number.")
