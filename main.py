import argparse      # Handles command-line arguments (hash, attack mode, options)
import hashlib       # Generates cryptographic hashes for password comparison
import itertools     # Produces combinations of characters for brute-force attacks
import time          # Measures execution time of cracking attempts
import sys           # Exits the program cleanly on errors or completion


# allowed preset config
CHARACTER_PRESETS = {
        "lowercase": "abcdefghijklmnopqrstuvwxyz",
        "digits": "0123456789",
        "lowerdigits": "abcdefghijklmnopqrstuvwxyz0123456789",
        "alphanumeric": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    }

def start_program():
    parser = argparse.ArgumentParser(
        prog = "Johness The Dissector",
        usage= "This program attempts to crack a password hash using brute force, or dictionaries.",
        help= ''
    )
    subparsers = parser.add_subparsers(dest='mode', required=True)

    # Dictionary mode
    dictionary_parser = subparsers.add_parser('dictionary')
    dictionary_parser.add_argument('--hash', required = True, help = 'password hash')
    dictionary_parser.add_argument('--algorithm', default= 'sha256', choices = ['md5', 'sha1','sha256', 'sha512'], help = 'hashing algorithm, md5, sha1, sha256, and sha512')
    dictionary_parser.add_argument('--wordlist', required = True, help = 'password wordlist')

    # Brute force mode
    brute_force_parser = subparsers.add_parser('bruteforce')
    brute_force_parser.add_argument('--hash', required = True, help = 'password hash')
    brute_force_parser.add_argument('--algorithm', default= 'sha256', choices = ['md5', 'sha1','sha256', 'sha512'], help = 'hashing algorithm, md5, sha1, sha256, or sha512')
    brute_force_parser.add_argument('--character_preset', choices= CHARACTER_PRESETS, default= 'alphaanumeric', help = 'character preset to be used, lowercase, digits, lowerdigits or alphanumeric')
    brute_force_parser.add_argument('--min_length', type = int, default= 3, help = 'minimum length of the password')
    brute_force_parser.add_argument('--max_length', type = int,  default=7, help = 'maximum length of the password')

    # parse arguments
    args = parser.parse_args()

    # validate brute force password length arguments
    if args.min_length < 3:
        print("Minimum length of the password is 3")
        return
    if args.max_length > 8:
        print("Maximum length of the password is 8")
        return

    # execute attacks
    start_time = time.perf_counter()
    if args.mode == 'dictionary':
        password = dictionary_attack(args.hash, args.algorithm, args.wordlist)
    elif args.mode == 'bruteforce':
        password = brute_force_attack(args.min_length, args.max_length, args.character_preset, args.hash, args.algorithm)
    total_time_elapsed = time.perf_counter() - start_time

    # Result
    if password is not None:
        print(f"A match has been found!\nYour password is {password}")
    else:
        print("Your password could not be found. Please try again.")

    print(f"Total time elapsed : {total_time_elapsed:.2f} seconds")



def dictionary_attack(user_input_password_hash, selected_hash_algorithm, wordlist_path):
    user_password_hash = normalize_user_password_hash(user_input_password_hash)
    # compare every entry with target hash
    with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as file:
        for password_entry in file:
            password = password_entry.strip()
            wordlist_password_hash = hash_password(password,selected_hash_algorithm)
            if user_password_hash == wordlist_password_hash:
                return password


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


def hash_password(plain_password, selected_hash_algorithm):
    # standardize selected hash input
    selected_hash_algorithm_normalized = selected_hash_algorithm.lower().strip()

    hash_obj = hashlib.new(selected_hash_algorithm_normalized)

    # hash plain password
    hash_obj.update(plain_password.encode())
    return hash_obj.hexdigest()


def normalize_user_password_hash(user_password_hash):
    return user_password_hash.lower().strip()