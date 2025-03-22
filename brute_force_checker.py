import string

def password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    strength = 0
    if length >= 8:
        strength += 1
    if has_upper:
        strength += 1
    if has_lower:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1

    if strength == 5:
        return "Very Strong"
    elif strength == 4:
        return "Strong"
    elif strength == 3:
        return "Moderate"
    else:
        return "Weak"

def brute_force_time(password):
    char_space = 0
    if any(c.islower() for c in password):
        char_space += 26
    if any(c.isupper() for c in password):
        char_space += 26
    if any(c.isdigit() for c in password):
        char_space += 10
    if any(c in string.punctuation for c in password):
        char_space += len(string.punctuation)

    total_combinations = char_space ** len(password)
    speed_per_second = 10**9  # 1 billion guesses per second
    time_seconds = total_combinations / speed_per_second
    return time_seconds
