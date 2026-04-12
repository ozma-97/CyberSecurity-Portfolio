# Screenshots & Visual Documentation

## Overview

This folder contains visual documentation of the security incident investigation dashboards created in Kibana. These screenshots show the attack patterns, timelines, and geographic data exfiltration identified during the analysis.

---

## Dashboard Visualizations

### 1. Brute Force Attack Timeline
**File:** `06-brute-force-chart.jpg`

**What it shows:**
- Line chart displaying failed login attempts over time
- Time interval: 30-second buckets
- Peak activity at 15:00 UTC on April 10, 2026
- Total: 247 failed login attempts

**Key Insights:**
- Clear spike pattern indicating automated credential spray attack
- Rapid, sequential login attempts
- High attack intensity over 40-minute window
- Suggests organized threat actor with pre-staged attack infrastructure

**Analysis:**
This visualization demonstrates the brute force attack's intensity and timing. The sharp spike indicates an automated tool attempting to crack user credentials at scale. The concentrated time window suggests pre-planning and coordination.

---

### 2. SQL Injection Events Timeline
**File:** `07-sql-injection-chart.jpg`

**What it shows:**
- Stacked bar chart of SQL injection attempts by timestamp
- Time interval: 30-minute buckets
- Peak activity at 12:00 UTC on April 10, 2026
- Total: 35 SQL injection attempts detected

**Key Insights:**
- Concentrated exploitation attempts at database interface
- Multiple injection types detected (UNION-based, time-based, error-based)
- Coordinated with brute force attack (different time window)
- Suggests multi-phase attack strategy

**Analysis:**
This visualization shows the SQL injection phase of the attack. Unlike the brute force attempts (which focused on authentication), this attack targeted the database layer. The separated timing suggests the attacker may have used credentials obtained from the brute force phase to gain deeper access.

---

### 3. Geographic Threat Map - Data Exfiltration Destinations
**File:** `08-origin-of-attacks-chart.jpg`

**What it shows:**
- Region map with color intensity showing data exfiltration destinations
- Primary destination: Russia (high-intensity red/dark coloring)
- Data volume represented by color intensity
- Geographic concentration of outbound data transfers

**Key Insights:**
- Russia as primary C2 (command & control) destination
- High-volume data exfiltration to single geographic region
- Suggests pre-staged infrastructure in Russia
- Clear intent to steal and extract customer data

**Analysis:**
This visualization is the most critical finding. The concentrated exfiltration to Russia indicates a well-organized threat actor with established infrastructure. This is not random or exploratory activity—it's a targeted data theft operation. The geographic concentration suggests either:
- Organized cybercriminal group based in Russia
- Advanced Persistent Threat (APT) with Russian attribution
- Compromised Russian servers used as data staging point

---

## How These Dashboards Were Created

### Data Source
- Security event logs from multiple systems
- Imported into Elasticsearch for indexing and storage
- Normalized and correlated in Kibana

### Visualization Techniques
1. **Time-Series Analysis**
   - Events bucketed by 30-second intervals (brute force)
   - Events bucketed by 30-minute intervals (SQL injection)
   - Allows clear pattern visualization

2. **Geographic Mapping**
   - IP geolocation data used to identify destinations
   - Color intensity represents data volume
   - Highlights geographic concentrations

3. **Event Correlation**
   - Events linked across attack vectors
   - Timeline reconstruction for attack chain
   - Pattern matching for anomaly detection

### Tools Used
- **Elasticsearch:** Log storage and indexing
- **Kibana:** Dashboard creation and visualization
- **KQL (Kibana Query Language):** Data filtering and querying

---

## Key Observations

### Attack Coordination
All three attack vectors occurred within a 3-hour window on the same day, suggesting:
- Coordinated multi-phase attack
- Single threat actor or organized group
- Pre-planned attack sequence
- Reconnaissance completed before execution

### Attack Progression
1. **12:00 UTC** - SQL injection attempts begin (database layer attack)
2. **12:00-15:00 UTC** - Brute force intensifies (authentication layer attack)
3. **15:00 UTC** - Data exfiltration to Russia (data theft phase)

### Threat Actor Behavior
- Sophisticated attack planning
- Knowledge of multiple attack vectors
- Access to pre-staged infrastructure (Russia C2)
- Professional-grade tooling and execution
- Organized cybercriminal or APT activity

---

## Screenshot Descriptions for Reference

| File | Attack Vector | Metric | Peak Activity | Total Events |
|------|---|---|---|---|
| 01-brute-force.png | Credential Attack | Failed Logins | 15:00 UTC | 247 |
| 02-sql-injection.png | Database Attack | Injection Attempts | 12:00 UTC | 35 |
| 03-geographic-map.png | Data Theft | Exfiltration Volume | Russia | High Volume |

---

## Analysis Takeaways

 **Multi-vector attack** - Three coordinated attack types  
 **Well-organized** - Professional execution and planning  
 **High-impact** - Customer data confirmed compromised  
 **Geographic attribution** - Russian C2 infrastructure  
 **Advanced threat** - Suggests APT or organized criminal group  

---

## Related Documentation

- **Full Analysis:** [View INCIDENT_REPORT.pdf](../INCIDENT_REPORT.pdf)
- **Investigation Methodology:** [View METHODOLOGY.md](../docs/METHODOLOGY.md)
- **Main Project:** [Back to Project README](../README.md)

---

*Screenshots captured from Kibana dashboards during security incident investigation*  
*April 10, 2026 - Incident Date*  
*April 11, 2026 - Analysis Date*