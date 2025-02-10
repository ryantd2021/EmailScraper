# Email Scraper

## Description
This Python script extracts email addresses from a given webpage and optionally scans multiple pages in a directory. It uses `requests` to fetch web content and `re` (regex) to extract emails from the page source.

## Features
- Extracts email addresses from a specified website.
- Supports scanning multiple pages within a directory structure.
- Defaults to scanning only the provided URL if no additional pages are specified.

## Requirements
- Python 3.x
- `requests` module (install using `pip install requests`)

## Usage
Run the script from the command line with the following options:

```sh
python script.py -host <website_url> [-pages <number_of_pages>]
```

### Arguments:
- `-host` (required): The base website URL to search for emails. Example: `example.com`
- `-pages` (optional): The number of pages to scan within the directory. Example: `5`

### Example Usage:
Scan a single page:
```sh
python script.py -host example.com
```

Scan multiple pages in a directory:
```sh
python script.py -host example.com -pages 5
```

## Notes
- If no `-pages` argument is provided, only the specified URL is scanned.
- The script assumes a pagination structure of `page/x/` if scanning multiple pages.

## License
This project is open-source and available under the MIT License.


