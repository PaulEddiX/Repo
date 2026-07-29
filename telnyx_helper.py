"""Simple Telnyx API helper example."""

BASE_URL = "https://api.telnyx.com/v2"

def list_phone_numbers(api_key: str) -> dict:
    """Return phone numbers associated with the account."""
    import urllib.request

    req = urllib.request.Request(
        f"{BASE_URL}/phone_numbers",
        headers={"Authorization": f"Bearer {api_key}"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        import json
        return json.loads(resp.read().decode())

if __name__ == "__main__":
    print("Set TELNYX_API_KEY and call list_phone_numbers() to fetch numbers.")
def log_event(event: str) -> None:
    print(f'[telnyx] {event}')
