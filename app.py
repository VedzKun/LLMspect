import argparse
import asyncio
from rich import print

from scanner.probe_generator import ProbeGenerator
from scanner.request_engine import RequestEngine
from scanner.analyzer import ResponseAnalyzer
from scanner.report import ReportGenerator


async def main(target_url, payload_dir, debug):

    generator = ProbeGenerator(payload_dir)
    engine = RequestEngine(target_url)
    analyzer = ResponseAnalyzer()
    report_generator = ReportGenerator()

    payloads = generator.load_payloads()
    findings = []
    for item in payloads:
        result = await engine.send_payload(item["payload"])
        analysis = analyzer.analyze(item["type"], item["payload"], result["response_text"], debug=debug)
        findings.extend(analysis)
        print(f"\nPayload: {item['payload']}")
        print(f"Findings: {analysis}")
    print("\nFINAL FINDINGS")
    for finding in findings:
        print(finding)
    report_file = report_generator.generate_json_report(target_url, findings)
    print(f"\nReport saved to: {report_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LLMspect - AI Security Scanner")
    parser.add_argument("-t", "--target", type=str, default="http://localhost:8000/chat", help="Target LLM API URL")
    parser.add_argument("-p", "--payloads", type=str, default="payloads", help="Directory containing payload JSON files")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging in analyzer")
    args = parser.parse_args()

    asyncio.run(main(args.target, args.payloads, args.debug))