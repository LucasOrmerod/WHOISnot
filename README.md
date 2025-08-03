# WHOISnot
WHOISnot is a Python script used to check which of the words on a list are available as domains with a choice of TLDs.

## Usage Instructions

There are four configuration variables within the script: WORDLIST_FILE, TLD_LIST_FILE, SLEEP_INTERVAL, and WHOIS_SREVER_ADDRESS. You will need to set a WHOIS server address, and you may need to change the other three variables too.

WORDLIST_FILE refers to the file containing the words to query.
TLD_LIST_FILE refers to the file containing the TLDs to append to the words.
SLEEP_INTERVAL refers to the time that will be left between requests to avoid overloading the WHOIS server.
WHOIS_SERVER_ADDRESS refers to the WHOIS server which will be used for the queries.

### Formatting

The script will convert words to lowercase and convert ASCII character and spaces to hyphens. Below is a list of formatting instructions.

- Each TLD or word should be on a new line
- TLDs should not have a full stop at the beginning (e.g. com instead of .com)
- TLDs and words should be in lowercase
- TLDs should be valid
- Words should only contain letters (a-z), numbers (0-9), and hypens (-)

Incorrectly formatted words and TLDs will be skipped when the script runs. Duplicates will be removed following formatting.

Example files have been included in the repository; these are wordlist.txt and tldlist.txt.