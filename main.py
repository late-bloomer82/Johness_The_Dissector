import argparse      # Handles command-line arguments (hash, attack mode, options)
import hashlib       # Generates cryptographic hashes for password comparison
import itertools     # Produces combinations of characters for brute-force attacks
import time          # Measures execution time of cracking attempts
import os            # Checks file existence (e.g., wordlist validation)
import sys           # Exits the program cleanly on errors or completion


def start_program():
    print("Johness The Dissector")
    pass

def dictionary_attack(hash):
    pass

def brute_force_attack():


def hash_password(plain_password, selected_hash_algorithm):
    # standardize selected hash input
    selected_hash_algorithm_normalized = selected_hash_algorithm.lower().strip()

    hash_obj = hashlib.new(selected_hash_algorithm_normalized)

    # hash plain password
    hash_obj.update(plain_password.encode())
    return hash_obj.hexdigest()