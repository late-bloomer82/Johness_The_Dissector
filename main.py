import argparse      # Handles command-line arguments (hash, attack mode, options)
import hashlib       # Generates cryptographic hashes for password comparison
import itertools     # Produces combinations of characters for brute-force attacks
import time          # Measures execution time of cracking attempts
import os            # Checks file existence (e.g., wordlist validation)
import sys           # Exits the program cleanly on errors or completion


def start_program():

    pass

def dictionary_attack(user_input_hash,selected_hash_algorithm):
    with open("rockyou.txt", "r", encoding="utf-8", errors="ignore") as file:
        for password_entry in file:
            password = password_entry.strip()
            password_hash = hash_password(password,selected_hash_algorithm)

            # compare hashes
            if user_input_hash == password_hash:
                return True


def brute_force_attack():

    pass


def hash_password(plain_password, selected_hash_algorithm):
    # standardize selected hash input
    selected_hash_algorithm_normalized = selected_hash_algorithm.lower().strip()

    hash_obj = hashlib.new(selected_hash_algorithm_normalized)

    # hash plain password
    hash_obj.update(plain_password.encode())
    return hash_obj.hexdigest()