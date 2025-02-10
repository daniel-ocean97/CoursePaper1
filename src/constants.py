import json
import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv

load_dotenv()
currency_token = os.getenv("CURRENCY_API_KEY")
stocks_token = os.getenv("STOCKS_API_KEY")
file_path = Path(__file__).resolve().parent.parent / "user_settings.json"
with open(file_path, "r") as f:
    user_settings = json.load(f)
data_file_path = Path(__file__).resolve().parent.parent / "data" / "operations.xlsx"
DF = pd.read_excel(data_file_path)
