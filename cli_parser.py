import argparse
from attacks import CHARACTER_PRESETS

def build_parser():
    parser = argparse.ArgumentParser(
        prog = "Johness The Dissector",
        description=(
            "CLI password hash cracking tool.\n\n"
            "Johness The Dissector attempts to recover the plaintext password "
            "for a supported hash using either dictionary mode or brute force mode.\n\n"
            "Supported hash algorithms: md5, sha1, sha256, sha512.\n"
            "The selected algorithm must match the algorithm used to create the target hash."),
        epilog=(
            "Examples:\n"
            "  python johness.py dictionary --hash <hash> --algorithm sha256 --wordlist wordlist.txt\n"
            "  python johness.py bruteforce --hash <hash> --algorithm sha256 --character-preset lowercase --min-length 1 --max-length 4" ),
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    subparsers = parser.add_subparsers(dest='mode', required=True)

    # Dictionary mode
    dictionary_parser = subparsers.add_parser(
        "dictionary",
        help="Try passwords from a wordlist file.",
    )

    dictionary_parser.add_argument(
        "--hash",
        required=True,
        help="Target password hash to crack.",
    )

    dictionary_parser.add_argument(
        "--algorithm",
        default="sha256",
        choices=["md5", "sha1", "sha256", "sha512"],
        help="Hashing algorithm to use. Options: md5, sha1, sha256, sha512. Default: sha256.",
    )

    dictionary_parser.add_argument(
        "--wordlist",
        required=True,
        help="Path to a password wordlist file.",
    )

    # Brute force mode
    brute_force_parser = subparsers.add_parser(
        "bruteforce",
        help="Generate password guesses using a character preset.",
    )

    brute_force_parser.add_argument(
        "--hash",
        required=True,
        help="Target password hash to crack.",
    )

    brute_force_parser.add_argument(
        "--algorithm",
        default="sha256",
        choices=["md5", "sha1", "sha256", "sha512"],
        help="Hashing algorithm to use. Options: md5, sha1, sha256, sha512. Default: sha256.",
    )

    brute_force_parser.add_argument(
        "--character-preset",
        choices= CHARACTER_PRESETS,
        default="alphanumeric",
        help=(
            "Character preset to use. Options: lowercase, digits, lowerdigits, "
            "alphanumeric. Default: alphanumeric."
        ),
    )

    brute_force_parser.add_argument(
        "--min-length",
        type=int,
        default=1,
        help="Minimum password length to try. Default: 1.",
    )

    brute_force_parser.add_argument(
        "--max-length",
        type=int,
        default=6,
        help="Maximum password length to try. Default: 6.",
    )
    return parser

def parse_args():
    parser = build_parser()
    return parser.parse_args