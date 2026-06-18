import _frozen_importlib_external
import json
from datetime import datetime
from pathlib import Path

class ReportGenerator:

    def __init__(self):
        self.report_dir = Path("reports")
        self.report_dir.mkdir(exist_ok=True)

    def generate_json_report(self, target, findings):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report = {
            "target": target,
            "scan_time": timestamp,
            "total_findings": len(findings),
            "findings": findings
        }
        filename = self.report_dir / f"report_{timestamp}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4)

        return filename
    
    def get_summary(self, findings):
        summary = {}
        for finding in findings:
            vuln = finding["vulnerability"]
            summary[vuln] = summary.get(vuln, 0) + 1

        return summary
        report["summary"] = self.get_summary(findings)