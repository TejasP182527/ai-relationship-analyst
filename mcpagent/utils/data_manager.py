import os, json

import json
import os

def load_client_data(client_name: str) -> dict:
    """
    Load client transcript data from local JSON files.
    """
    base_path = os.path.join("mcpagent", "client_data", f"client_{client_name}.json")
    if not os.path.exists(base_path):
        raise FileNotFoundError(f"No transcript data found for client: {client_name}")

    with open(base_path, "r", encoding="utf-8") as f:
        return json.load(f)
