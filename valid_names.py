import re
def validate_name(arr):
    pattern = re.compile("(^[A-Z][a-z]+) ([A-Z][a-z]*)?\s?([A-Z][a-z]+)")
    for name in arr:
        if re.match(pattern, name):
            print(name)
        else:
            print("Invalid name")