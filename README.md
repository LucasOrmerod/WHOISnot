# WHOISnot
WHOISnot is a Python script used to check which of the words on a list are available as unregistered domains.

## Usage Instructions
Insert the words you want to search into wordlist.txt.
Insert the TLDs you want to append to these words into tldlist.txt.
You may wish to change the WHOIS_SERVER and SLEEP_INTERVAL values, however please note I have not tested the script with different values.

Make sure all TLDs selected are valid as invalid TLDs will be shown as "unregistered".

### Formatting

### Formatting

The script will convert words to lowercase and convert ASCII characters and spaces to hyphens. Below is a list of formatting instructions.

- Each TLD or word should be on a new line
- TLDs should not have a full stop at the beginning (e.g. com instead of .com)
- TLDs and words should be in lowercase
- Words should only contain letters (a-z), numbers (0-9), and hypens (-)

Incorrectly formatted words and TLDs will be skipped when the script runs. Duplicates will be removed following formatting.

Example files have been included in the repository; these are wordlist.txt and tldlist.txt.
