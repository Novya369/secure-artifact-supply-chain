import requests
from pathlib import Path

VERSION = Path("version.txt").read_text().strip()

def main():
    print(f"Secure Artifact Supply Chain Demo - v{VERSION}")
    try:
        r = requests.get("https://pypi.org/", timeout=5)
        print("HTTP status:", r.status_code)
    except requests.exceptions.SSLError:
        print("SSL verification failed : running in restricted environment")

if __name__ == "__main__":
    main()

