import subprocess
import time
import re

pattern = r'^[a-z0-9-]+$'

# Configuration
WORDLIST_FILE = "./wordlist.txt" # Every line in this file will be queried to WHOIS
TLD_LIST_FILE = "./tldlist.txt" # Every subdomain in this file will be used for each word in the wordlist
SLEEP_INTERVAL = 0.1 # Sleep interval between WHOIS queries
WHOIS_SERVER_ADDRESS = "whois.iana.org" # WHOIS server to query

def get_lines_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]
    
def make_domain_list():
    wordlist = get_lines_from_file(WORDLIST_FILE)
    tld_list = get_lines_from_file(TLD_LIST_FILE)

    print(wordlist)
    print(tld_list)

    for tld in tld_list:
        if not re.match(r'^[a-z]{2,}$', tld):
            raise ValueError(f"Invalid TLD format: {tld}")
        
    # check the TLDs with the WHOIS server
    for tld in tld_list:
        try:
            subprocess.run(["whois", "-h", WHOIS_SERVER_ADDRESS, tld], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError as e:
            print(f"Error querying TLD {tld}: {e}")
            continue
        
        time.sleep(SLEEP_INTERVAL)
    
    domain_list = []
    for word in wordlist:
        word = word.lower().replace(" ", "-")  # Replace spaces with hyphens

        if not re.match(pattern, word):
            continue

        for tld in tld_list:
            domain_list.append(f"{word}.{tld}")
    # Remove duplicates by converting to a set and back to a list
    domain_list = list(set(domain_list))
    
    return domain_list

def main():
    list = make_domain_list()
    print(list)