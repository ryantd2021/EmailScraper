import requests
import re
import argparse
from urllib.parse import urlparse, urljoin

def extract_emails(content):
    # Regex pattern to match email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(email_pattern, content)

def fetch_page(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching page: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(
        description='Extract emails from a webpage and its subpages.',
        epilog='Example usage: python script.py -host example.com -pages 5'
    )
    parser.add_argument('-host', required=True, help='Base website URL to search for emails. Example: example.com (Required)')
    parser.add_argument('-pages', type=int, help='Number of pages to scan within the directory. Example: 5 (Optional)')
    args = parser.parse_args()
    
    parsed_url = urlparse(args.host)
    if not parsed_url.scheme:
        base_url = 'https://' + args.host  # Default to HTTPS if no scheme provided
    else:
        base_url = args.host
    
    print(f"Searching for emails on: {base_url}")
    
    if args.pages:
        for i in range(1, args.pages + 1):
            url = urljoin(base_url, f'page/{i}/')  # Assuming page follows 'page/x/' pattern
            print(f"Fetching: {url}")
            content = fetch_page(url)
            if content:
                emails = extract_emails(content)
                if emails:
                    print("Found email addresses:")
                    for email in set(emails):
                        print(email)
                else:
                    print("No email addresses found on this page.")
    else:
        content = fetch_page(base_url)
        if content:
            emails = extract_emails(content)
            if emails:
                print("Found email addresses:")
                for email in set(emails):
                    print(email)
            else:
                print("No email addresses found.")

if __name__ == "__main__":
    main()
