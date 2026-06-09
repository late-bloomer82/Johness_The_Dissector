import itertools

from helpers import normalize_user_password_hash, hash_password

# allowed preset config
CHARACTER_PRESETS = {
        "lowercase": "abcdefghijklmnopqrstuvwxyz",
        "digits": "0123456789",
        "lowerdigits": "abcdefghijklmnopqrstuvwxyz0123456789",
        "alphanumeric": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    }

def dictionary_attack(user_input_password_hash, selected_hash_algorithm, wordlist_path):
    user_password_hash = normalize_user_password_hash(user_input_password_hash)
    # compare every entry with target hash
    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as file:
            for password_entry in file:
                password = password_entry.strip()
                wordlist_password_hash = hash_password(password, selected_hash_algorithm)
                if user_password_hash == wordlist_password_hash:
                    return password
    except FileNotFoundError as e:
        print(f"{e}. Wordlist could not be found.")
        return None


def brute_force_attack(min_length, max_length, character_set, user_input_password_hash, selected_hash_algorithm):
    user_password_hash = normalize_user_password_hash(user_input_password_hash)
    chosen_preset = CHARACTER_PRESETS[character_set.lower().strip()]

    # Go through each possible password length
    for password_combination_length in range(min_length, max_length + 1):

        # create an object that produces every possible combination for a password defined length
        iterator = itertools.product(chosen_preset, repeat = password_combination_length)

        # hash each combination and compare it
        for combination_tuple in iterator:
            password_combination = "".join(combination_tuple)
            hashed_combination = hash_password(password_combination, selected_hash_algorithm)
            if hashed_combination == user_password_hash:
                return password_combination