import os
import sys
from dotenv import load_dotenv

# Load configuration from a local .env file if it exists
load_dotenv()


def get_required_env(name: str) -> str:
    """Return a required environment variable or exit with a clear message."""
    value = os.getenv(name)
    if not value:
        print(f"Error: missing required environment variable '{name}'.")
        sys.exit(1)
    return value


def main() -> None:
    # Read a regular setting and a secret from environment variables
    app_name = get_required_env("APP_NAME")
    api_key = get_required_env("API_KEY")

    print(f"APP_NAME: {app_name}")
    # Print only whether the secret is loaded, never its value
    print(f"API_KEY loaded: {bool(api_key)}")


if __name__ == "__main__":
    main()