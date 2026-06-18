class RiskEngine:

    def calculate(self, confidence):

        if confidence >= 80:
            return "Critical"

        if confidence >= 60:
            return "High"

        if confidence >= 40:
            return "Medium"

        return "Low"