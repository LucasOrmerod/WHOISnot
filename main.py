import re
import subprocess
import time
from collections import OrderedDict
import string

WORD_REGEX = r'^[a-z0-9-]+$'
TLD_REGEX = r'^(?!\.)([a-z.]+)$'

# --- CONFIGURATION ------------------
WORD_LIST_FILE = "wordlist.txt"
TLD_LIST_FILE = "tldlist.txt"
WHOIS_SERVER = "whois.iana.org"
SLEEP_INTERVAL = 1.5
# --- CONFIGURATION ------------------

def read_lines_from_text(file):
    with open(file, "r") as f:
        lines = [line.strip() for line in f]
        return lines
    
def make_list(input_wordlist, input_tldlist):
    filtered_wordlist = []
    filtered_tldlist = []

    chars_to_replace = string.punctuation + " "
    translation_table = str.maketrans(chars_to_replace, "-" * len(chars_to_replace))

    for word in input_wordlist:
        word = word.lower().translate(translation_table)

        if not re.match(WORD_REGEX, word) or not 1 <= len(word) <=63:
            print(f"Skipping Word: {word}")
            continue
        else:
            filtered_wordlist.append(word)
    
    for tld in input_tldlist:
        tld = tld.lower()

        if not re.match(TLD_REGEX, tld) or not len(tld) > 1:
            print(f"Skipping TLD: {tld}")
            continue
        else:
            filtered_tldlist.append(tld)

    appending_wordlist = list(OrderedDict.fromkeys(filtered_wordlist))
    appending_tldlist = list(OrderedDict.fromkeys(filtered_tldlist))

    output_domains = []

    for word in appending_wordlist:
        for tld in appending_tldlist:
            output_domains.append(f"{word}.{tld}")
    
    return output_domains

def query_whois(list, server):
    referral_regex = r'Found a referral to [^\n]*\n.*?Domain Name:\s*([A-Z0-9.-]+)'

    output = []

    for domain in list:
        if server:
            cmd = ["whois"]
            cmd.extend(["-h", server])
            cmd.append(domain)
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)

            if not result.returncode == 0:
                continue

            match = re.search(referral_regex, result.stdout, re.IGNORECASE | re.DOTALL)
            
            if not match:
                print(f"Domain {domain} is unregistered :)")
                output.append(domain)
            else:
                print(f"Domain {domain} has already been registered :(")
                
        time.sleep(SLEEP_INTERVAL)

    return output

def main():
    wordlist = read_lines_from_text(WORD_LIST_FILE)
    tldlist = read_lines_from_text(TLD_LIST_FILE)

    domains = make_list(wordlist, tldlist)
    unregistered = query_whois(domains, WHOIS_SERVER)

    print("\nThe following domains are unregistered:\n")
    for d in unregistered:
        print(f'{d}')

main()