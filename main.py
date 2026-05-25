import argparse      # Handles command-line arguments (hash, attack mode, options)
import hashlib       # Generates cryptographic hashes for password comparison
import itertools     # Produces combinations of characters for brute-force attacks
import time          # Measures execution time of cracking attempts
import os            # Checks file existence (e.g., wordlist validation)
import sys           # Exits the program cleanly on errors or completion


def start_program():
    parser = argparse.ArgumentParser(
        prog = "Johness The Dissector",
        description = "Password cracker",
    )
    parser.add_argument()

def dictionary_attack(user_input_password_hash, selected_hash_algorithm):
    user_password_hash = normalize_user_password_hash(user_input_password_hash)
    # compare every entry with target hash
    with open("rockyou.txt", "r", encoding="utf-8", errors="ignore") as file:
        for password_entry in file:
            password = password_entry.strip()
            wordlist_password_hash = hash_password(password,selected_hash_algorithm)
            if user_password_hash == wordlist_password_hash:
                return password


def brute_force_attack(min_length, max_length, character_set, user_input_password_hash, selected_hash_algorithm):
    user_password_hash = normalize_user_password_hash(user_input_password_hash)
    CHARACTER_PRESETS = {
        "lowercase": "abcdefghijklmnopqrstuvwxyz",
        "digits": "0123456789",
        "lowerdigits": "abcdefghijklmnopqrstuvwxyz0123456789",
        "alphanumeric": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    }
    chosen_preset = CHARACTER_PRESETS[character_set.lower().strip()]

    # Go through each possible password length
    for password_combination_length in range(min_length, max_length + 1):

        # create an object that produces every possible combination
        iterator = itertools.product(chosen_preset, repeat = password_combination_length)

        # hash each combination and compare it
        for combination_tuple in iterator:
            password_combination = "".join(combination_tuple)
            hashed_combination = hash_password(password_combination, selected_hash_algorithm)
            if hashed_combination == user_password_hash:
                return password_combination



def hash_password(plain_password, selected_hash_algorithm):
    # standardize selected hash input
    selected_hash_algorithm_normalized = selected_hash_algorithm.lower().strip()

    hash_obj = hashlib.new(selected_hash_algorithm_normalized)

    # hash plain password
    hash_obj.update(plain_password.encode())
    return hash_obj.hexdigest()


def normalize_user_password_hash(user_password_hash):
    return user_password_hash.lower().strip()