from pathlib import Path
import gspread
from google.oauth2.service_account import Credentials

SCOPES = ["https://www.googleapis.com/auth/spreadsheets",
          "https://www.googleapis.com/auth/drive"]

BASE_DIR = Path(__file__).resolve().parent
SERVICE_FILE = BASE_DIR / "service_account.json"


def append_to_sheet(data):
    creds = Credentials.from_service_account_file(
        SERVICE_FILE,
        scopes=SCOPES
    )

    client = gspread.authorize(creds)
    sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1gV7Esg0e9D8BrqAA5F5F9a94efkVwb90S85Ry7tLC7k/edit?gid=0#gid=0").sheet1

    sheet.append_row([
        data["phone"],
        data["intent"],
        data["urgency"],
        data["summary"]
    ])