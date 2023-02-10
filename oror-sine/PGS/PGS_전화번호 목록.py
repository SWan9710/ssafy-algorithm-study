def solution(phone_book):
    hash_map = {key: 1 for key in sorted(phone_book)}
    keys = hash_map.keys()
    for key in keys:
        digits = ""
        for digit in key:
            digits += digit
            if digits in hash_map and digits != key:
                return False
    return True
