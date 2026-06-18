import asyncio
from rich import print

from scanner.probe_generator import ProbeGenerator
from scanner.request_engine import RequestEngine
from scanner.analyzer import ResponseAnalyzer
from scanner.report import ReportGenerator

TARGET_URL = "http://localhost:8000/chat"


async def main():

    generator = ProbeGenerator()
    engine = RequestEngine(TARGET_URL)
    analyzer = ResponseAnalyzer()
    report_generator = ReportGenerator()

    payloads = generator.load_payloads()
    findings = []
    for item in payloads:
        result = await engine.send_payload(item["payload"])
        analysis = analyzer.analyze(item["type"],item["payload"],result["response_text"])
        findings.extend(analysis)
        print(f"\nPayload: {item['payload']}")
        print(f"Findings: {analysis}")
    print("\nFINAL FINDINGS")
    for finding in findings:
        print(finding)
    report_file = report_generator.generate_json_report(TARGET_URL,findings)
    print(f"\nReport saved to: {report_file}")

if __name__ == "__main__":
    asyncio.run(main())