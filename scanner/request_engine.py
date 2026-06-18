import httpx
import asyncio


class RequestEngine:
    def __init__(self, target_url):
        self.target_url = target_url

    async def send_payload(self, payload):
        try:
            async with httpx.AsyncClient(timeout=15.0) as client:

                response = await client.post(
                    self.target_url,
                    json={
                        "message": payload
                    }
                )

                return {
                    "status_code": response.status_code,
                    "response_text": response.text
                }

        except Exception as e:
            return {
                "status_code": None,
                "response_text": str(e)
            }