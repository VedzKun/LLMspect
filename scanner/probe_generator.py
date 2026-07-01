import json
from pathlib import Path


class ProbeGenerator:
    def __init__(self, payload_dir="payloads"):
        self.payload_dir = Path(payload_dir)

    def load_payloads(self):
        payloads = []

        for file in self.payload_dir.glob("*.json"):
            with open(file, "r", encoding="utf-8") as f:
                payloads.extend(json.load(f))

        return payloads