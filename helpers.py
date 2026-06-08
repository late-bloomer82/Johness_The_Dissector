import hashlib

def hash_password(plain_password, selected_hash_algorithm):
    # standardize selected hash input
    selected_hash_algorithm_normalized = selected_hash_algorithm.lower().strip()

    hash_obj = hashlib.new(selected_hash_algorithm_normalized)

    # hash plain password
    hash_obj.update(plain_password.encode())
    return hash_obj.hexdigest()

def validate_bruteforce_lengths(min_length, max_length):
    if min_length < 1:
        print("Minimum password length must be at least 1.")
        return False

    if max_length > 7:
        print("Maximum password length must be 7 or lower.")
        return False

    if min_length > max_length:
        print("Minimum length must be less than or equal to maximum length.")
        return False

    return True

def normalize_user_password_hash(user_password_hash):
    return user_password_hash.lower().strip()