import requests
import json
from typing import Dict, Any

# ANSI escape codes for colors and formatting
class Colors:
    CYAN = '\033[1;36m'
    BLUE = '\033[1;34m'
    WHITE = '\033[0;37m'
    WHITE_BOLD = '\033[1;37m'
    GREEN = '\033[1;32m'
    RED = '\033[1;31m'
    LINK = '\033[1;35m'  # New color for the link
    RESET = '\033[0m'
    BOLD = '\033[1m'

def print_banner():
    """Prints a colorful ASCII art banner for the tool."""
    banner = f"""
{Colors.CYAN}
██╗██████╗        ██████╗ ███████╗██╗███╗   ██╗████████╗
██║██╔══██╗      ██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝
██║██████╔╝█████╗██║   ██║███████╗██║██╔██╗ ██║   ██║
██║██╔═══╝ ╚════╝██║   ██║╚════██║██║██║╚██╗██║   ██║
██║██║           ╚██████╔╝███████║██║██║ ╚████║   ██║
╚═╝╚═╝            ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝

{Colors.RESET}
{Colors.WHITE}IPWhoIs CLI Tool            {Colors.CYAN}By {Colors.WHITE_BOLD}SANATANI_x_ANONYMOUS{Colors.RESET}
---------------------
"""
    print(banner)

class IPWhoIsClient:
    """
    A robust client for the ipwho.is API with colorful output.

    This tool retrieves and displays all available information for a given
    IP address, with a focus on clear and organized output, including nested
    data structures and colorful formatting.
    """

    def __init__(self):
        """Initializes the client with the base API URL."""
        self.base_url = "https://ipwho.is/"

    def get_ip_info(self, ip_address: str) -> Dict[str, Any] | None:
        """
        Retrieves the full JSON data for a specified IP address.

        Args:
            ip_address (str): The IP address to query.

        Returns:
            dict | None: The full API response as a dictionary if successful,
                         otherwise None.
        """
        if not ip_address:
            print(f"{Colors.RED}Error: An IP address must be provided.{Colors.RESET}")
            return None

        url = f"{self.base_url}{ip_address}"
        print(f"{Colors.WHITE_BOLD}Fetching data for IP: {ip_address}...{Colors.RESET}")
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data.get("success"):
                return data
            else:
                print(f"{Colors.RED}API returned an error: {data.get('message', 'Unknown error')}{Colors.RESET}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"{Colors.RED}A network error occurred: {e}{Colors.RESET}")
            return None
        except json.JSONDecodeError as e:
            print(f"{Colors.RED}Failed to decode JSON from response: {e}{Colors.RESET}")
            return None

    def _print_dict_recursively(self, data: Dict[str, Any], indent: int = 0):
        """
        A helper method to print key-value pairs from a dictionary,
        handling nested dictionaries with increasing indentation and color.
        """
        for key, value in data.items():
            prefix = "  " * indent
            # Check for specific keys to format differently
            key_color = Colors.BLUE
            value_color = Colors.GREEN

            if isinstance(value, dict):
                # Special handling for the 'flag' key to display the emoji
                if key == 'flag':
                    emoji = value.get('emoji', '')
                    print(f"{prefix}{key_color}{key}: {value_color}{emoji}{Colors.RESET}")
                    # Continue recursively for nested flag info
                    self._print_dict_recursively(value, indent + 1)
                else:
                    print(f"{prefix}{key_color}{key}:{Colors.RESET}")
                    self._print_dict_recursively(value, indent + 1)
            else:
                print(f"{prefix}{key_color}{key}: {value_color}{value}{Colors.RESET}")

    def display_all_info(self, ip_address: str):
        """
        Retrieves and prints all available information for an IP address
        in a structured, easy-to-read, and colorful format.
        """
        ip_info = self.get_ip_info(ip_address)
        if ip_info:
            print(f"{Colors.BOLD}\n--- Full IP Information ---{Colors.RESET}")
            self._print_dict_recursively(ip_info)
            print(f"{Colors.BOLD}---------------------------\n{Colors.RESET}")

            # Check for coordinates and generate a Google Maps link
            latitude = ip_info.get('latitude')
            longitude = ip_info.get('longitude')
            if latitude is not None and longitude is not None:
                google_maps_url = f"https://www.google.com/maps/place/{latitude},{longitude}"
                print(f"🗺️ {Colors.LINK}Google Maps Link: {google_maps_url}{Colors.RESET}\n")
        else:
            print(f"{Colors.RED}Failed to retrieve information for {ip_address}.{Colors.RESET}")


# Main execution block
if __name__ == "__main__":
    print_banner()

    client = IPWhoIsClient()

    while True:
        user_input = input(f"{Colors.WHITE_BOLD}Enter an IP address (or 'q' to quit): {Colors.RESET}")
        if user_input.lower() == 'q':
            print("Goodbye!")
            break

        client.display_all_info(user_input)
