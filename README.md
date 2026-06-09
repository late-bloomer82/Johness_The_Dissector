# Johness The Dissector

Johness The Dissector is a CLI password hash cracking program that accepts a target password hash and attempts to recover the plaintext password using dictionary mode or brute force mode.

Supported hash algorithms:

* `md5`
* `sha1`
* `sha256`
* `sha512`


This project is for educational use only.

## Features

* Dictionary attack mode
* Brute force attack mode
* Support for simple `hashlib` algorithms
* Character presets for brute force mode
* Execution time reporting

## How to Use

Show the help menu:

```bash
python3 johness.py --help
```

### Dictionary Mode

Use dictionary mode to test password candidates from a wordlist file.

```bash
python3 johness.py dictionary --hash <target_hash> --algorithm sha256 --wordlist wordlist.txt
```

### Brute Force Mode

Use brute force mode to generate password guesses from a character preset.

```bash
python3 johness.py bruteforce --hash <target_hash> --algorithm sha256 --character-preset lowercase --min-length 1 --max-length 4
```

The selected algorithm must match the algorithm originally used to create the target hash. If the wrong algorithm is selected, the correct password will not produce a matching hash.

## Character Presets

* `lowercase`
* `digits`
* `lowerdigits`
* `alphanumeric`

## Wordlists

Dictionary mode expects a plain text wordlist with one password candidate per line.

Large wordlists, such as `rockyou.txt`, should not be committed to GitHub.

## Limitations

* Only supports simple unsalted hashes
* Only supports `md5`, `sha1`, `sha256`, and `sha512`
* Does not support salted hashes or advanced hash formats
* Brute force mode can become very slow as password length and character set size increase

## Usage Suggestions

- Start with dictionary mode if you have a relevant wordlist. Dictionary mode is usually much faster than brute force
- Use brute force mode with small length ranges first, such as `--min-length 1 --max-length 4`.
- Choose the smallest character preset that could contain the password.
- Avoid large brute force ranges unless you are prepared to wait a long time.
- Make sure the selected algorithm matches the algorithm used to create the target hash.

## Learning Objectives

* Practice Python syntax and standard libraries
* Learn basic cybersecurity concepts
* Understand dictionary and brute force attack logic
* Practice building a command-line tool with `argparse`

## Project Notes

* The project uses a functional style because the current logic does not require shared object state.