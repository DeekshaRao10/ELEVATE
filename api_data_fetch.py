# api_data_fetch.py
# Demonstrates API fetching, JSON parsing, error handling, and clean output

import requests  # Make sure you installed: pip install requests


# ----------------------------
# Function to fetch user data
# ----------------------------
def fetch_random_user():
    """Fetch data from Random User API and return parsed JSON."""

    url = "https://randomuser.me/api/"

    try:
        # 4. Send GET request
        response = requests.get(url, timeout=5)

        # Check status code
        if response.status_code != 200:
            return None, f"API Error: Status Code {response.status_code}"

        # 5. Parse JSON response
        data = response.json()

        return data, None

    except requests.exceptions.Timeout:
        return None, "Request timed out. Please try again."

    except requests.exceptions.ConnectionError:
        return None, "Connection error. Check your internet."

    except requests.exceptions.RequestException as e:
        return None, f"Unexpected error: {e}"


# ----------------------------
# Function to extract details
# ----------------------------
def extract_user_info(data):
    """Extract nested JSON fields safely."""

    try:
        user = data["results"][0]  # nested JSON

        full_name = (
            user["name"]["title"] + " " +
            user["name"]["first"] + " " +
            user["name"]["last"]
        )

        email = user["email"]
        country = user["location"]["country"]
        username = user["login"]["username"]

        return {
            "Name": full_name,
            "Email": email,
            "Country": country,
            "Username": username
        }

    except (KeyError, IndexError):
        return None


# ----------------------------
# Main Execution
# ----------------------------
def main():
    print("\n--- Fetching Random User Data ---")

    data, error = fetch_random_user()

    if error:
        print("Error:", error)
        return

    user_info = extract_user_info(data)

    if not user_info:
        print("Error: Could not extract user data.")
        return

    # 8. Clean formatted output
    print("\nUser Details:")
    print("-" * 30)
    for key, value in user_info.items():
        print(f"{key:<10}: {value}")
    print("-" * 30)


if __name__ == "__main__":
    main()
