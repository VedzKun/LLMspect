import json
from pathlib import Path


class ProbeGenerator:
    def __init__(self):
        self.payload_dir = Path("payloads")

    def load_payloads(self):
        payloads = []

        for file in self.payload_dir.glob("*.json"):
            with open(file, "r", encoding="utf-8") as f:
                payloads.extend(json.load(f))

        return payloads