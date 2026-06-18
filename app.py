import asyncio

from scanner.probe_generator import ProbeGenerator
from scanner.request_engine import RequestEngine


TARGET_URL = "http://localhost:8000/chat"


async def main():

    generator = ProbeGenerator()

    payloads = generator.load_payloads()

    engine = RequestEngine(TARGET_URL)

    for item in payloads:

        result = await engine.send_payload(
            item["payload"]
        )

        print("=" * 50)

        print(item["type"])

        print(item["payload"])

        print(result["status_code"])


if __name__ == "__main__":
    asyncio.run(main())