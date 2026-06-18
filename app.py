from scanner.probe_generator import ProbeGenerator

generator = ProbeGenerator()

payloads = generator.load_payloads()

print(f"Loaded {len(payloads)} payloads")

for payload in payloads:
    print(payload)