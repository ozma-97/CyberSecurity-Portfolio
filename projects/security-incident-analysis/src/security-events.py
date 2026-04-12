import json
import random
from datetime import datetime, timedelta
import hashlib

# Generate realistic security logs with attacks
logs = []

# Base timestamp
start_time = datetime(2026, 4, 10, 8, 0, 0)

# Attack 1: Brute Force Attack (10:00 AM - 10:45 AM)
attacker_ip = "203.0.113.42"
target_username = "admin"
brute_force_start = start_time + timedelta(hours=2)

print("Generating Brute Force Attack...")
for i in range(247):
    logs.append({
        "timestamp": (brute_force_start + timedelta(seconds=i*10)).isoformat() + "Z",
        "source_ip": attacker_ip,
        "destination_ip": "192.0.2.50",
        "event_type": "authentication",
        "event_category": "authentication",
        "event_outcome": "failure",
        "username": target_username,
        "password_attempt": f"pass{random.randint(1000, 9999)}",
        "http_status": 401,
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "protocol": "HTTP",
        "port": 443,
        "event_severity": "high"
    })

# Successful login after brute force
successful_login_time = brute_force_start + timedelta(seconds=247*10 + 30)
logs.append({
    "timestamp": successful_login_time.isoformat() + "Z",
    "source_ip": attacker_ip,
    "destination_ip": "192.0.2.50",
    "event_type": "authentication",
    "event_category": "authentication",
    "event_outcome": "success",
    "username": target_username,
    "http_status": 200,
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "protocol": "HTTP",
    "port": 443,
    "event_severity": "critical",
    "session_id": "sess_a1b2c3d4"
})

# Attack 2: SQL Injection (11:00 AM - 11:30 AM)
print("Generating SQL Injection Attack...")
sql_injection_start = brute_force_start + timedelta(minutes=15)
sql_payloads = [
    "' OR '1'='1",
    "' UNION SELECT * FROM users--",
    "admin' --",
    "' DROP TABLE users--",
    "'; DELETE FROM logs--"
]

for i in range(35):
    payload = random.choice(sql_payloads)
    logs.append({
        "timestamp": (sql_injection_start + timedelta(seconds=i*60)).isoformat() + "Z",
        "source_ip": attacker_ip,
        "destination_ip": "192.0.2.50",
        "event_type": "web_application_attack",
        "event_category": "web_application",
        "event_outcome": "success",
        "username": target_username,
        "http_method": "GET",
        "url": f"/api/search?q={payload}",
        "http_status": 200,
        "http_response_body_bytes": random.randint(5000, 50000),
        "user_agent": "sqlmap/1.4.9",
        "protocol": "HTTP",
        "port": 443,
        "attack_type": "sql_injection",
        "payload": payload,
        "event_severity": "critical"
    })

# Attack 3: Data Exfiltration (11:45 AM - 12:30 PM)
print("Generating Data Exfiltration...")
exfil_start = sql_injection_start + timedelta(minutes=45)
exfil_destination_ip = "198.51.100.89"  # External IP (attacker controlled)

for i in range(15):
    logs.append({
        "timestamp": (exfil_start + timedelta(minutes=i*5)).isoformat() + "Z",
        "source_ip": "192.0.2.50",  # Internal server
        "destination_ip": exfil_destination_ip,
        "event_type": "data_transfer",
        "event_category": "network_traffic",
        "event_outcome": "success",
        "username": target_username,
        "protocol": "HTTPS",
        "port": 443,
        "network_bytes_out": random.randint(100000000, 500000000),  # 100MB - 500MB
        "destination_geo_country": "RU",  # Russia
        "destination_geo_city": "Moscow",
        "http_status": 200,
        "event_severity": "critical",
        "data_transferred_mb": random.randint(100, 500)
    })

# Normal background traffic (to make it realistic)
print("Generating normal background traffic...")
normal_start = start_time
normal_users = ["user1", "user2", "user3", "user4", "user5", "admin"]
normal_ips = ["192.168.1.100", "192.168.1.101", "192.168.1.102", "192.168.1.103"]

for i in range(500):
    random_time = normal_start + timedelta(hours=random.randint(0, 24), minutes=random.randint(0, 59), seconds=random.randint(0, 59))
    
    # Skip times during attacks to make it cleaner
    if brute_force_start <= random_time <= brute_force_start + timedelta(hours=1):
        continue
    if sql_injection_start <= random_time <= sql_injection_start + timedelta(hours=1):
        continue
    if exfil_start <= random_time <= exfil_start + timedelta(hours=1):
        continue
    
    logs.append({
        "timestamp": random_time.isoformat() + "Z",
        "source_ip": random.choice(normal_ips),
        "destination_ip": "192.0.2.50",
        "event_type": "web_request",
        "event_category": "web",
        "event_outcome": "success",
        "username": random.choice(normal_users),
        "http_method": random.choice(["GET", "POST"]),
        "url": random.choice(["/api/users", "/api/data", "/dashboard", "/login"]),
        "http_status": 200,
        "http_response_body_bytes": random.randint(1000, 100000),
        "user_agent": "Mozilla/5.0",
        "protocol": "HTTPS",
        "port": 443,
        "event_severity": "low"
    })

# Sort by timestamp
logs.sort(key=lambda x: x["timestamp"])

# Save as JSON (Elasticsearch format)
output_file = "security-logs.json"
with open(output_file, "w") as f:
    for log in logs:
        # Elasticsearch bulk format (one JSON per line)
        f.write(json.dumps(log) + "\n")

print(f"\n✅ Generated {len(logs)} security logs")
print(f"📁 Saved to: {output_file}")
print(f"\n📊 Attack Summary:")
print(f"  - Brute Force: 247 failed attempts + 1 success from {attacker_ip}")
print(f"  - SQL Injection: 35 injection attempts")
print(f"  - Data Exfiltration: 15 large transfers to {exfil_destination_ip}")
print(f"  - Background Traffic: ~500 normal events")