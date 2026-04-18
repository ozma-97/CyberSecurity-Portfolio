# Data Breach Incident Response Playbook

## Incident Overview

**What It Is:** Unauthorized Data Access/Exfiltration (someone stole data)  
**How Serious:** CRITICAL  
**How Fast:** IMMEDIATE (< 15 minutes)  
**How Long It Takes:** Days to Weeks  
**Legal Stuff:** LOTS of notification laws apply  

---

## What is a Data Breach?

A data breach happens when someone unauthorized gets access to sensitive data and steals it. It's different from ransomware because they're just copying your data, not locking it up.

**What Happens:**
- Unauthorized person gets into sensitive systems
- They download or copy data
- They might sell it, post it online, or use it
- You often don't find out for weeks or months
- Sometimes ransomware is involved too (double threat)

**What To Look For:**
- Huge data downloads from weird times/users
- Multiple failed login attempts then suddenly success
- Passwords showing up for sale on the dark web
- Your company data published online
- Someone else tells you your data is out there
- Weird activity in logs from months ago
- Email saying "we have your data, pay us"

**Types of Data That Matter:**
- Customer info (names, addresses, Social Security numbers)
- Financial data (credit cards, bank account info)
- Secret company stuff (source code, trade secrets)
- Employee records and tax forms
- Medical information (HIPAA)
- Payment card info (PCI-DSS)

---

## How to Spot It

**Technical Red Flags:**
- Huge data transfer to someone outside the company
- Database access from weird location or 3am
- Multiple files downloaded from sensitive folders
- VPN access from random countries
- Passwords found on dark web
- Weird database queries
- Backup data accessed or deleted
- Admin credentials being used weirdly

**External Red Flags:**
- Dark web surveillance picks it up
- Sites like "Have I Been Pwned" flag your data
- Email saying "we stole your data, pay us and proof attached"
- Your data on hacker forums
- Another company tells you your data is there
- Customers complaining they got scammed
- Police call you

**Behavioral Red Flags:**
- Employee says they got weird email from "vendor"
- Someone's password was reset and they didn't do it
- Unexpected email from their own account
- Someone asking lots of questions about your systems

---

##  PHASE 1: RIGHT NOW - First Hour

### **Step 1: Check It's Real & Escalate (0-15 min)**
- [ ] Get the breach report
- [ ] Figure out who reported it and how they know
- [ ] What specific data do they say they have?
- [ ] **CALL your IR Lead AND a lawyer RIGHT NOW**
- [ ] Write down when you found out
- [ ] Create incident ticket

**Key Questions:**
- How do they know this happened?
- Can they prove they have the data?
- Are they asking for money?
- Is the data actually yours?

**Big Red Flags That Need Immediate Escalation:**
- Data includes Social Security numbers → escalate NOW
- Data includes credit cards → escalate NOW
- Data includes medical info → escalate NOW
- They're demanding money → escalate NOW
- It's confirmed real → escalate NOW

---

### **Step 2: Get a Lawyer Involved (0-10 min)**
- [ ] Contact legal team ASAP
- [ ] Tell them what's happening
- [ ] Listen to what they tell you to do
- [ ] Get external incident response help if needed
- [ ] Write down every decision they make

**Why This First:**
- There are strict deadlines for telling people (laws)
- Lawyers can protect your investigation
- They know the legal requirements for your location
- They'll tell you what to tell people

---

### **Step 3: Save the Evidence**
- [ ] **Don't investigate compromised systems yourself yet**
- [ ] Save all log files (don't delete them)
- [ ] Make backup copies of affected systems (if cloud)
- [ ] Write down how you collected everything
- [ ] Keep it organized (chain of custody)
- [ ] Lock it up in encrypted storage

**This matters because:**
- Police might need it
- You might need it in court
- Messed up evidence = useless evidence

---

### **Step 4: Tell Internal People Only (0-30 min)**
- [ ] CEO/executives (just the basics)
- [ ] Response team
- [ ] Lawyers
- [ ] Security team
- [ ] IT leadership

**What to Say:**
- Possible breach reported
- Lawyers are handling this
- Investigation starting
- Don't tell anyone outside yet
- Only share details if they need to know

---

## PHASE 2: INVESTIGATION - First Day

### **Step 1: Figure Out How Bad It Is**
- [ ] What type of data was accessed?
- [ ] How many records?
- [ ] What time period?
- [ ] How many people affected?
- [ ] Was data encrypted or plain text?
- [ ] How sensitive is it?

**Data Sensitivity Scale:**
| Data | Risk Level | Example |
|------|-----------|---------|
| Names | Low | 50,000 people |
| Emails | Low | 50,000 people |
| Phone #s | Medium | 50,000 people |
| Addresses | Medium | 50,000 people |
| Social Security # | HIGH | 50,000 people = EMERGENCY |
| Credit cards | HIGH | 50,000 people = EMERGENCY |
| Medical info | HIGH | 1,000 people = EMERGENCY |

---

### **Step 2: How Did They Get In?**
Try to figure out:
- [ ] Stole someone's password?
  - Phishing? Reused password? Weak password?
- [ ] Found an unpatched vulnerability?
  - Check what wasn't updated
- [ ] Misconfigured cloud storage?
  - Check S3 buckets, Azure storage
- [ ] Inside job?
  - Check employee access logs
- [ ] Third-party company gave them access?
  - Check vendor relationships
- [ ] Weak login security?
  - Was MFA on? Default passwords?

**Investigation Steps:**
1. Look at access logs for weird stuff
2. Check if they moved around your network
3. Look for backdoors they left behind
4. What systems did they touch?
5. How long were they in there?

---

### **Step 3: When Did Each Thing Happen?**
Write a timeline:
- [ ] When did account/system get compromised?
- [ ] When did data stealing start?
- [ ] When did data stealing stop?
- [ ] When did we find out?
- [ ] Time gap between breach and discovery?

**Why This Matters:**
- Longer they had access = more data stolen
- Longer we didn't know = more damage possible
- Affects legal notification requirements

---

### **Step 4: Is This Data Actually Theirs?**
If they send you a sample:
- [ ] Compare with your actual records
- [ ] Does it match your format?
- [ ] Is it recent data?
- [ ] Is the data complete and accurate?
- [ ] How confident are we this is real?

**Confidence Levels:**
- **High:** Data matches perfectly, recent records
- **Medium:** Data looks similar but some questions
- **Low:** Data doesn't match or they got it from somewhere else

---

### **Step 5: What Laws Apply?**
- [ ] Does it include customer info? → GDPR, CCPA, state laws
- [ ] Medical data? → HIPAA
- [ ] Financial data? → Bank laws
- [ ] Payment cards? → PCI-DSS
- [ ] Student data? → FERPA

**Notification Requirements:**
- Customer info in breach → You probably have to tell people
- Unencrypted data → Definitely have to tell people
- Encrypted data → Maybe don't have to (depends where)

---

##  PHASE 3: STOP IT - 4-24 Hours

### **Step 1: Stop Them from Stealing More**
- [ ] Reset their password
- [ ] Force them offline
- [ ] Block their IP address
- [ ] Watch that account really carefully
- [ ] Revoke API keys
- [ ] Remove VPN access

---

### **Step 2: Prevent Them From Coming Back**
- [ ] Fix the vulnerability they used
- [ ] Better password rules
- [ ] Turn on MFA
- [ ] Update firewall
- [ ] Add more monitoring
- [ ] Review who has access to what
- [ ] Delete unused accounts

---

### **Step 3: Check Other Systems**
- [ ] Find all systems they touched
- [ ] Reset passwords on related accounts
- [ ] Scan for malware
- [ ] Update patches
- [ ] Add monitoring
- [ ] Tighten network access
- [ ] Review access rules

---

##  PHASE 4: TELL PEOPLE - Days 1-3

### **Step 1: Know the Deadlines**

Different places have different laws:
- **GDPR (Europe):** Tell authorities in 72 hours if serious
- **CCPA (California):** Tell people ASAP
- **HIPAA (Medical):** Tell people ASAP
- **Other states:** Varies (check your state)
- **PCI-DSS (Credit cards):** 30 days

**Important:** Ask your lawyer about YOUR specific deadlines.

---

### **Step 2: Prepare What to Tell Each Person**

#### **A. Government/Regulators**
Include:
- What data was involved
- How many people affected
- What you're doing about it
- How to contact you

*(Lawyer will write this)*

---

#### **B. Customers/People Affected**
Subject: Important Security Notice

Include:
- What happened (simple English, not technical)
- What data was involved
- What you're doing
- What they should do
- Free credit monitoring offer
- How to contact you
- Timeline

---

#### **C. Your Employees**
Include:
- Here's what happened
- We're handling it
- Here's what to tell customers who call
- Resources available to staff
- We're working on prevention

---

#### **D. Media (If Big Breach)**
Include:
- Factual statement
- What we're doing
- Commitment to security
- Contact info

*(PR team handles with lawyer approval)*

---

### **Step 3: Send All Notifications**
- [ ] Send emails all at once if possible
- [ ] Coordinate with police/regulators
- [ ] Watch for questions and respond
- [ ] Set up customer support hotline
- [ ] Offer free credit monitoring
- [ ] Watch dark web for data sales
- [ ] Track police investigation

---

##  PHASE 5: RANSOM EMAIL (If You Get One)

**If They Send: "Pay us or we publish your data"**

### **First Response:**
- [ ] DO NOT PAY YET
- [ ] Save the email as evidence
- [ ] Tell the police (FBI)
- [ ] Tell your lawyer
- [ ] Tell incident response firm

### **Then Analyze:**
- [ ] Is the data actually yours?
- [ ] What happens if they publish?
- [ ] How bad is the business impact?
- [ ] What's the legal impact?
- [ ] What's the financial impact?

### **Decision:**
- **Generally:** Don't pay (seriously)
- **Maybe consider:** Only if executives and lawyers say so
- **Work with:** Police and negotiation experts
- **Understand:** Paying doesn't guarantee they delete it

---

## PHASE 6: WHAT DID WE LEARN? - 1-2 Weeks

### **Lessons Learned Meeting**

**Who:** Response team, security, IT, legal, affected business

**Talk About:**
1. How did we find out about it?
2. When did they actually get in?
3. What let them get in?
4. Why didn't we catch it sooner?
5. Did we contain it fast enough?
6. Did we tell people the right way?
7. What stops this next time?
8. What security gaps did we find?

---

### **Fix Things ASAP (Within 48 hours):**
- [ ] Reset all related passwords
- [ ] Patch the vulnerability
- [ ] Update firewall rules
- [ ] Turn on MFA everywhere critical
- [ ] Add more monitoring
- [ ] Review who has access
- [ ] Lock down critical systems

---

### **Bigger Fixes (Within 30 days):**
- [ ] Full security audit of access
- [ ] Data protection review
- [ ] Better backups
- [ ] EDR tools on all computers
- [ ] Better security training
- [ ] Vulnerability scanning
- [ ] Third-party security assessment

---

## How To Prevent This

**Access Control:**
- MFA on everything important
- Limit access (only what people need)
- Check access every 3 months
- Separate job duties
- Disable unused accounts
- VPN with MFA
- Restrict access by location

**Data Protection:**
- Encrypt sensitive data (stored and in transit)
- Data loss prevention tools
- Encrypted backups offline
- Check cloud storage permissions
- Database activity monitoring
- Tag sensitive data
- Know where your data is

**Detection:**
- SIEM monitoring
- EDR on all computers
- Watch for behavior anomalies
- Keep logs for a long time
- Monitor dark web
- Regular vulnerability scans
- Intrusion detection

**Response:**
- Incident response plan
- Regular drills
- Team training
- Hire incident response firm on retainer
- Forensics firm contacts
- Insurance
- Playbooks like this one

---

## Key Numbers to Track

**Timing:**
- Days from breach to discovery: _____
- Hours from discovery to investigation: _____
- Hours to contain it: _____
- Days to notify people: _____

**Impact:**
- People affected: _____
- Type of data: __________
- Required legal notifications: Y/N
- Customer notification sent: Y/N
- Police involved: Y/N

**Business Impact:**
- Cost: $_______
- Reputation damage: __________
- Customer loss: ___%
- News articles: ___ articles

---

*Data Breach Response Playbook - Version 1.0*  
*Last Updated: April 17, 2026*  
*Check with a lawyer about laws in your area*