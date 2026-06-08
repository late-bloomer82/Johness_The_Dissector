import time

from attacks import brute_force_attack, dictionary_attack
from helpers import validate_bruteforce_lengths
from cli_parser import parse_args

def start_program():

    args = parse_args()

    # execute attacks
    if args.mode == 'dictionary':
        start_time = time.perf_counter()
        password = dictionary_attack(args.hash, args.algorithm, args.wordlist)

    elif args.mode == 'bruteforce':
        if not validate_bruteforce_lengths(args.min_length,args.max_length):
            return
        start_time = time.perf_counter()
        password = brute_force_attack(args.min_length, args.max_length, args.character_preset, args.hash, args.algorithm)

    total_time_elapsed = time.perf_counter() - start_time

    # Result
    if password is not None:
        print(f"A match has been found!\nYour password is {password}")
    else:
        print("Your password could not be found. Please try again.")

    print(f"Total time elapsed : {total_time_elapsed:.2f} seconds")


if __name__ == "__main__":
    start_program()