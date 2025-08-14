```md
# 🛰️ IPWhois CLI Tool
```
<p align="center">
  <img src="https://raw.githubusercontent.com/dark-assist/Cloudpc/refs/heads/main/Screenshot_2025_0814_085040.png" width="900">
</p>

**Author:** `SANATANI_x_ANONYMOUS`  
**Description:**  
A **fast**, **colorful**, and **interactive** Python CLI tool to fetch **detailed IP address information** using the [ipwho.is API](https://ipwho.is).  
Perfect for OSINT, network diagnostics, and geolocation lookups — all **from your terminal**.

---

## ✨ Features
- 🎨 **Colorful Output** – ANSI escape colors for a hacker-style, readable UI  
- 🧭 **Geo Lookup** – Country, region, city, coordinates, timezone, and more  
- 🌍 **Google Maps Link** – Direct link to pinpoint IP location  
- 🔄 **Recursive Display** – Nicely formatted nested JSON output  
- 🛡️ **Error Handling** – Handles API errors, invalid IPs, and network issues gracefully  
- 🚀 **Interactive CLI** – Just run, type an IP, get results instantly  

---

## 📦 Installation
```bash
# Clone this repo
git clone https://github.com/YOUR-USERNAME/ipwhois-cli-tool.git
cd ipwhois-cli-tool

# Install dependencies
pip install requests
````

---

## 🚀 Usage

```bash
python ipwhois.py
```

Then enter:

```
Enter an IP address (or 'q' to quit): 8.8.8.8
```

---

## 🖥 Example Output

```
Fetching data for IP: 8.8.8.8...

--- Full IP Information ---
ip: 8.8.8.8
success: True
type: IPv4
continent: North America
country: United States 🇺🇸
region: California
city: Mountain View
latitude: 37.42261
longitude: -122.08428
Google Maps: https://maps.google.com/?q=37.42261,-122.08428
connection:
  asn: 15169
  org: Google LLC
  isp: Google LLC
timezone:
  id: America/Los_Angeles
  utc: -07:00
```

---

## 📜 License

This project is licensed under the **MIT License**.
See [`LICENSE.md`](LICENSE.md) for details.

---
