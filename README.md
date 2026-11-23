# clean-first-repos

Minimal Python starter project demonstrating isolated virtual environments, environment-based configuration via `python-dotenv`, and clean Git hygiene.

## Setup

1. Clone the repository and open the project folder:

   ```bash
   git clone [https://github.com/AsakuraXava/clean-first-repos.git](https://github.com/AsakuraXava/clean-first-repos.git)
   cd clean-first-repos

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows PowerShell: .\.venv\Scripts\Activate.ps1

3. Install dependencies:
   

```bash

pip install -r requirements.txt


Configuration

Copy .env.example to .env and fill in your values:
    
   ```bash
   cp .env.example .env  # Windows PowerShell: Copy-Item .env.example .env

APP_NAME — application name displayed when the script runs.

API_KEY — secret API key loaded from the environment (never commit .env or print the key value).

Run

Run the script:

   ```bash

   python main.py


Expected output:

APP_NAME: CleanRepository
API_KEY loaded: True