import hashlib

def hash_password(plain_password, selected_hash_algorithm):
    # standardize selected hash input
    selected_hash_algorithm_normalized = selected_hash_algorithm.lower().strip()

    hash_obj = hashlib.new(selected_hash_algorithm_normalized)

    # hash plain password
    hash_obj.update(plain_password.encode())
    return hash_obj.hexdigest()


def normalize_user_password_hash(user_password_hash):
    return user_password_hash.lower().strip()