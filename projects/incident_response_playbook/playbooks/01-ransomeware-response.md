# Ransomware Incident Response Playbook

## Incident Overview

**What It Is:** Ransomware Infection  
**How Serious:** CRITICAL  
**How Fast:** IMMEDIATE (< 15 minutes)  
**How Long It Takes:** Hours to Days  

---

## What is Ransomware?

Ransomware is malware that locks up your files and the attacker demands money to unlock them. It's one of the worst attacks because it shuts down your whole operation.

**What It Does:**
- Encrypts your files so you can't open them
- Makes systems unusable
- Shows a ransom note demanding payment
- Spreads to shared drives and backups
- Sometimes steals data too (double threat)

**What To Look For:**
- Files suddenly have weird extensions (.locked, .encrypted, .ransom, etc.)
- A ransom note appears on the desktop
- Users can't open their files
- Computer gets really slow
- Strange network activity

---

## How to Spot It

**Things That Trigger Alerts:**
- Weird file creation activity
- Tons of files changing extensions all at once
- Unknown process using a lot of CPU/disk
- Strange outbound connections
- High network activity

**File Clues:**
- Extensions: .locked, .encrypted, .ransom, .crypto, .bin
- Files named things like: README.txt, HELP_RECOVER_FILES.txt, DECRYPT_INSTRUCTIONS.html

**People Saying:**
- "I can't open my files"
- "My computer is demanding money"
- "My files have weird names"
- "Everything is really slow"

---

##  PHASE 1: RIGHT NOW - First 30 Minutes

### **Step 1: Tell Someone & Create a Ticket (0-5 min)**
- [ ] Get the incident report
- [ ] **CALL your Incident Response Lead RIGHT NOW** (don't email)
- [ ] If it's after hours, call the on-call security person
- [ ] Create an incident ticket
- [ ] Write down when it was discovered and who reported it

**Why:** Every minute counts with ransomware.

---

### **Step 2: Isolate the System (5-15 min)**
- [ ] **DO NOT SHUT IT DOWN YET**
- [ ] **Unplug the network cable** or turn off WiFi
  - This stops it from spreading to other computers
  - This stops it from calling home to the attacker
- [ ] Keep the power ON (we need it for investigation)
- [ ] Note the exact time you did this
- [ ] Take a photo of the ransom note on screen (evidence)

**Why this way:**
- Unplugging first = stops the spread immediately
- Keeping it on = we can investigate the memory and running processes
- Shutdown might trigger the malware to do more damage

---

### **Step 3: Get Details from the User (10-20 min)**
Ask them or their manager:
- [ ] When did they first notice something wrong?
- [ ] Which files are affected?
- [ ] What does the ransom message say?
- [ ] What's the computer name and username?
- [ ] Did anyone already pay? (If yes, escalate ASAP)
- [ ] How important is the lost data?
- [ ] Do they have recent backups?

**Write everything down.** You'll need this for decisions later.

---

### **Step 4: Check if It Spread (15-30 min)**
- [ ] **Don't open files from the infected computer**
- [ ] Look for similar file changes on shared drives
- [ ] Use your monitoring tools (EDR/SIEM) to search for similar activity
- [ ] Search network shares for ransom notes
- [ ] Look for weird activity in the last day or two

**Signs it spread:**
- Multiple computers reporting problems
- Shared drive files encrypted
- Backup files encrypted
- Multiple departments affected

---

### **Step 5: Tell the Right People (20-30 min)**
- [ ] Notify your IT Director/Manager
- [ ] Notify the CEO/executive team if it's widespread
- [ ] **Don't tell customers/public yet**
- [ ] Talk to legal counsel
- [ ] Prepare a quick briefing with what you know so far

**What To Tell Executives:**
- Ransomware detected on [computer/department]
- When it happened
- What's affected
- What we're doing about it
- When they'll hear from us again

---

## PHASE 2: INVESTIGATION - First Few Hours

### **Step 1: Figure Out How Bad It Is**
- [ ] How many computers are infected?
- [ ] Servers, desktops, or both?
- [ ] What data is encrypted?
- [ ] Are backups safe?

**If it's getting worse:**
- Make it a full company emergency
- Maybe isolate bigger parts of the network
- Call in extra help

---

### **Step 2: Collect Evidence**
- [ ] **Keep the infected computer ON and isolated**
- [ ] Screenshot the desktop and ransom note
- [ ] Write down what processes are running
- [ ] Save the Windows Event Logs
- [ ] Note any network connections
- [ ] Check if the system clock has been messed with

**This matters because:**
- Law enforcement might need it
- Investigation teams need it
- You might need it later if there's a lawsuit

---

### **Step 3: Identify Which Ransomware**
Look at the ransom note for:
- What group/name is mentioned?
- Any email addresses or websites?
- Any unique IDs or victim numbers?

Use threat intelligence:
- ID Ransomware (https://www.idransomware.com)
- Your threat intel team

**Why:** Different ransomware = different options. Some have free decryption tools available.

---

### **Step 4: How Did They Get In?**
Try to figure out:
- [ ] When did the attack start?
- [ ] What process started the encryption?
- [ ] How did malware get on the system?
  - Phishing email?
  - Exposed RDP?
  - Stolen password?
  - Unpatched vulnerability?
  - USB drive?

- [ ] Did they move around the network?
- [ ] When was the last good backup?

---

### **Step 5: Check Your Backups**
- [ ] Do you have recent backups?
- [ ] Are the backups also encrypted?
- [ ] How long would it take to restore?
- [ ] Can you actually restore from them?

**This is the big decision:**
- Good backups = restore everything in hours
- No backups = very bad situation

---

## PHASE 3: STOP THE SPREAD - 1-4 Hours

### **Step 1: Network Lockdown**
- [ ] Disconnect infected system(s)
- [ ] Isolate that department's network if needed
- [ ] Block any connections to attacker servers (if you know them)
- [ ] Update firewall rules

---

### **Step 2: Password Reset**
- [ ] Reset passwords for affected users
- [ ] Force password resets for RDP accounts
- [ ] Reset API keys if needed
- [ ] Turn on multi-factor authentication
- [ ] Watch for suspicious login attempts

---

### **Step 3: Kill Backdoors**
- [ ] Find and remove any persistence mechanisms
- [ ] Delete suspicious scheduled tasks
- [ ] Disable unauthorized services
- [ ] Document what you changed

---

### **Step 4: Protect Your Backups**
- [ ] Make sure backups are NOT encrypted
- [ ] Check backup integrity
- [ ] Test restoring a small file
- [ ] Know how long full restoration takes

---

## PHASE 4: GET SYSTEMS BACK - 4-48 Hours

### **Choose Your Recovery Method:**

**Option A: Restore from Backup** (Best choice)
- Fastest if backups exist
- Clean system
- Usually done in 2-24 hours
- **Recommended**

**Option B: Clean In-Place** (Not great)
- Risky - malware might hide
- Takes longer
- Might not get all files back
- **Not recommended**

**Option C: Wipe & Rebuild** (Safest)
- Completely clean
- Takes longer (24-72 hours)
- Guaranteed no malware
- **Good for important systems**

---

### **Execute Recovery:**
- [ ] Back up current system for investigation first
- [ ] Restore from backup OR wipe and rebuild
- [ ] Test everything works
- [ ] Verify no encrypted files left
- [ ] Plug back into network

---

### **Make Sure It's Actually Clean:**
- [ ] Run antivirus scans
- [ ] Check backup is good
- [ ] Look for persistence mechanisms
- [ ] Watch for suspicious activity
- [ ] Verify all services are running
- [ ] Check data is intact

---

### **Give Access Back to Users:**
- [ ] Return computer to user
- [ ] Reset their password
- [ ] Confirm they can access their files
- [ ] Note when recovery was complete
- [ ] Get sign-off from user

---

## PHASE 5: TELL PEOPLE WHAT'S HAPPENING

### **Timeline:**

**First Hour:**
- Tell: Executives, IT leadership
- Say: Ransomware detected, isolated, investigating, backups are safe

**Every Hour During Incident:**
- Tell: Response team, management
- Say: How many systems, what we're doing, what we found so far, how long until fixed

**When It's Over:**
- Tell: Everyone affected
- Say: Incident fixed, how we fixed it, what we're doing to prevent it, when systems are back

---

### **Do We Tell Anyone Else?**

**Law Enforcement?**
- If data was stolen
- If they're threatening to leak it
- If it's a major attack
- Contact: FBI, local police

**Customers?**
- If their data was accessed
- If there's a legal requirement
- Always ask legal first

**Pay the Ransom?**
- Generally: NO
- Only if executives and lawyers say yes
- Work with law enforcement
- Use negotiation specialists

---

## PHASE 6: WHAT DID WE LEARN?

### **Meeting Within 1 Week**

**Who:** Response team, affected managers, IT leadership, security

**Talk About:**
1. How fast did we detect it?
2. Did everyone follow the playbook?
3. Did isolation stop the spread?
4. How long did recovery take?
5. Did people know what was happening?
6. How did they get in?
7. How do we prevent this next time?

---

### **Fix Things ASAP (Within 48 hours):**
- [ ] Patch the vulnerability they used
- [ ] Update firewall rules
- [ ] Disable RDP if not needed
- [ ] Update security tools
- [ ] Monitor for similar attacks

---

### **Bigger Fixes (Within 30 days):**
- [ ] Better backups & disaster recovery
- [ ] Train users on security
- [ ] Deploy EDR (Endpoint Detection & Response)
- [ ] Segment the network
- [ ] Turn on MFA everywhere
- [ ] Regular vulnerability scans

---

## How To Prevent This

**Technical Stuff:**
- Keep everything patched and updated
- Deploy EDR tools
- Enable MFA
- Disable RDP (if not needed)
- Segment your network
- Use DNS filtering
- Keep offline backups

**Process Stuff:**
- Test backups regularly
- Do incident response drills
- Review user access regularly
- Train everyone on security
- Run phishing tests

**User Training:**
- Don't open weird email attachments
- Check who the email is actually from
- Report suspicious emails
- Keep software updated
- Use strong passwords

---

*Ransomware Response Playbook - Version 1.0*  
*Last Updated: April 17, 2026*  