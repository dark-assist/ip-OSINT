#IPWhois CLI 

██╗██████╗        ██████╗ ███████╗██╗███╗   ██╗████████╗
██║██╔══██╗      ██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝
██║██████╔╝█████╗██║   ██║███████╗██║██╔██╗ ██║   ██║
██║██╔═══╝ ╚════╝██║   ██║╚════██║██║██║╚██╗██║   ██║
██║██║           ╚██████╔╝███████║██║██║ ╚████║   ██║
╚═╝╚═╝            ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝

IPWhoIs CLI Tool            By SANATANI_x_ANONYMOUS
---------------------
A robust and colorful command-line interface tool built in Python to retrieve and display comprehensive information about any given IP address using the ipwho.is API.FeaturesInteractive CLI: Prompts the user for an IP address and provides detailed information.Colorful Output: Uses ANSI escape codes to make the output easy to read and visually appealing.Recursive Display: Handles nested JSON data gracefully, printing all fields with proper indentation.Google Maps Link: Automatically generates a clickable Google Maps link for the IP's geographical coordinates.Error Handling: Catches common network and API errors to provide a smooth user experience.PrerequisitesPython 3.6 or higherrequests libraryInstallationClone the repository:git clone https://github.com/your-username/ipwhois-cli-tool.git
cd ipwhois-cli-tool
(Note: Replace your-username with your actual GitHub username.)Install the required Python library:pip install requests
UsageRun the script from your terminal:python ipwhois.py
The tool will display a banner and then prompt you to enter an IP address.Enter an IP address (or 'q' to quit): 8.8.8.8
To exit the tool, simply type q and press Enter.Example OutputFetching data for IP: 8.8.8.8...

--- Full IP Information ---
ip: 8.8.8.8
success: True
type: IPv4
continent: North America
continent_code: NA
country: United States
country_code: US
region: California
region_code: CA
city: Mountain View
latitude: 37.42261
longitude: -122.08428
is_eu: False
postal: 94043
calling_code: 1
capital: Washington D.C.
borders: CA,MX
flag: 🇺🇸
  img: https://cdn.ipwhois.io/flags/us.svg
  emoji: 🇺🇸
  emoji_unicode: U+1F1FA U+1F1F8
connection:
  asn: 15169
  org: Google LLC
  isp: Google LLC
  domain: google.com
timezone:
  id: America/Los_Angeles
  abbr: PDT
  is_dst: True
  offset: -25200
  utc: -07:00
  current_time: 2024-05-18T10:47:06-07:00
---
LicenseThis project is licensed under the MIT License - see the LICENSE.md file for details.
