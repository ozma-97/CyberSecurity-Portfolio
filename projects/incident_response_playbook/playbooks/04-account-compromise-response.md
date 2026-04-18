# Account Compromise Incident Response Playbook

## Incident Overview

**What It Is:** Unauthorized Account Access  
**How Serious:** MEDIUM to HIGH  
**How Fast:** URGENT (< 1 hour)  
**How Long It Takes:** Hours to Days  

---

## What is Account Compromise?

Account compromise happens when someone unauthorized gets into a user's account and can do stuff as that user. They have all the permissions that user has.

**What Can Happen:**
- Legitimate password used illegally
- Attacker can do whatever the user can do
- They might steal data the user can access
- They might use the account to get into other systems
- Often goes unnoticed for weeks
- Can affect customers or break systems

**Types of Compromise:**
- **Password Stolen:** Via phishing, malware, or data breach
- **Session Hijacking:** Attacker intercepts active session
- **Privilege Escalation:** Attacker elevates from user to admin
- **Third-party Breach:** Vendor account compromised
- **Insider Threat:** Malicious employee using their own access

---

## How to Spot It

**Users Saying:**
- "I got a password reset email I didn't ask for"
- "Someone accessed my email"
- "I see login activity I didn't do"
- "My email sent messages I didn't write"
- "My account got locked"
- "I can't login but someone's using my account"

**Technical Alerts:**
- Login from different continents in impossibly short time
- Login from weird location/time/device
- Multiple failed logins then sudden success
- Tons of failed login attempts
- VPN login from random country
- Password reset request
- MFA disabled
- New API key created
- Email forwarding rule created
- Account added to sensitive groups
- Privilege escalation

**Email Red Flags:**
- Email sent from account user didn't write
- Email forwarding rule appeared
- Emails going to weird people
- Weird attachments being sent
- Password reset email not requested
- Recovery email sent to different address

**System Red Flags:**
- Files accessed user doesn't normally use
- Login at 3am
- Multiple simultaneous logins from different places
- Sensitive shared drives accessed
- Huge file downloads
- System changes made
- Admin group changes

---

##  PHASE 1: RIGHT NOW - First 30 Minutes

### **Step 1: Check It's Real & Assess**
- [ ] Get the compromise report
- [ ] Ask how serious:
  - **CRITICAL:** Admin account, data access, money systems
  - **HIGH:** Regular employee, some sensitive access
  - **MEDIUM:** Limited access, contractor
- [ ] Create incident ticket
- [ ] Escalate based on severity
- [ ] Write down when and who reported it

---

### **Step 2: Confirm It's Actually Compromised**
Ask the user:
- [ ] When did you notice?
- [ ] What's the evidence?
- [ ] Have you accessed sensitive systems?
- [ ] Do you have admin access?
- [ ] What systems can you access?

Check technically:
- [ ] Review login logs
- [ ] Check for weird activity
- [ ] Password reset events
- [ ] MFA disable attempts

**Big Question:** Is this actually a compromise or did the user just forget they did something?

---

### **Step 3: Lock It Down**
- [ ] **Reset their password immediately**
  - You do it (not the user)
  - Strong temporary password
  - Force them to change it next time they login
  
- [ ] **Force logout everywhere**
  - Kick them out of all sessions
  - Clear cached passwords
  - Revoke active tokens
  
- [ ] **Disable account (if really bad)**
  - Stop any access
  - Tell the user
  - Give them a temporary clean account
  
- [ ] **Block bad IP addresses**
  - If attack came from specific IP
  - Update firewall
  - Block it everywhere

---

### **Step 4: Tell the User**
- [ ] Call them (don't just email)
  - Tell them account was compromised
  - Tell them password was reset
  - Give them temporary password
  - Tell them what to do next
  
- [ ] Be nice—don't blame them
- [ ] Give them a ticket number
- [ ] Tell them we're watching it

---

##  PHASE 2: INVESTIGATION - 30 min to 4 Hours

### **Step 1: Figure Out When & For How Long**
Create a timeline:
- [ ] When did compromise start?
- [ ] When did we find out?
- [ ] How long was attacker in there?
- [ ] What did they do during that time?

**Example:**

April 10, 3:15 AM - Weird login from Russia April 10, 3:20 AM - 5 failed login attempts April 10, 3:25 AM - Login worked from Russia April 10, 3:30 AM - Email forwarding rule created April 10, 3:35 AM - Emails being forwarded out April 11, 2:00 PM - User reports account compromised

RESULT: In for ~22.5 hours before we knew!


---

### **Step 2: How Did They Get In?**
Try to figure out:
- [ ] Phishing email?
  - Ask if they clicked suspicious link
- [ ] Data breach?
  - Do they reuse passwords?
- [ ] Malware?
  - Notice any suspicious software?
- [ ] Social engineering?
  - Anyone ask them for password?
- [ ] Weak password?
  - Was it easy to guess?
- [ ] Unpatched vulnerability?
  - What systems accessed?
- [ ] Insider?
  - Could be someone they know

---

### **Step 3: What Could They Access?**
- [ ] Sensitive data available to user?
- [ ] Financial systems?
- [ ] Customer or personal data?
- [ ] Company secrets or source code?
- [ ] Other user passwords (if shared)?
- [ ] VPN or remote access?
- [ ] Email or communications?

**What Did They Actually Do?**
- [ ] Check access logs - what did they look at?
- [ ] Check email logs - what did they send/forward?
- [ ] Check file downloads - what did they copy?
- [ ] Check system changes - what did they modify?
- [ ] Check account changes - permissions changed?

---

### **Step 4: Did They Spread to Other Systems?**
- [ ] Access other systems?
- [ ] Create backdoor for later?
- [ ] Steal other passwords?
- [ ] Install malware?
- [ ] Modify other accounts?
- [ ] Access shared drives?

**Investigation Steps:**
1. Look for lateral movement signs
2. Check for privilege escalation
3. Look for backdoors
4. Check for credential theft
5. Review admin activity logs
6. Check for service account compromise

---

### **Step 5: Is This Actually Worse Than We Thought?**
Based on what you find:
- [ ] Sensitive data accessed? → Data breach protocol
- [ ] Admin account compromised? → Network-wide investigation
- [ ] Financial system accessed? → Tell Finance Security
- [ ] Customer data accessed? → Tell Legal (might need to notify)
- [ ] Backdoor created? → Start threat hunting
- [ ] Multiple accounts compromised? → Reset lots of passwords

---

##  PHASE 3: STOP IT - 1-4 Hours

### **Step 1: Secure Their Credentials**
- [ ] Reset password
- [ ] Force logout everywhere
- [ ] Revoke all API keys/tokens
- [ ] Remove app passwords (Gmail, etc.)
- [ ] Revoke VPN access
- [ ] Remove SSH keys
- [ ] Update SSH key fingerprints

---

### **Step 2: Remove Backdoors**
- [ ] Check email forwarding rules - delete bad ones
- [ ] Check alternate email addresses - remove bad ones
- [ ] Check account recovery options - fix them
- [ ] Check mobile devices - remove unauthorized
- [ ] Check SSH keys - remove bad ones
- [ ] Check browser extensions - remove suspicious
- [ ] Review 2FA settings - reset them

---

### **Step 3: Lock Down Their Access**
- [ ] Review groups they're in
- [ ] Remove from sensitive groups if not needed
- [ ] Review shared drive access
- [ ] Review VPN access
- [ ] Review admin permissions
- [ ] Review service account access
- [ ] Review application access

---

### **Step 4: Watch Them Closely**
- [ ] Enable high-level monitoring
- [ ] Alert if:
  - Password reset attempted
  - Failed logins
  - Impossible travel
  - Weird file access
  - Email forwarding created
  - Privilege escalation attempt

- [ ] Watch for 72+ hours

---

### **Step 5: If There's Malware**
If you think attacker has malware on their computer:
- [ ] Disconnect from network
- [ ] Run antivirus/anti-malware
- [ ] Check for backdoors
- [ ] Restore from clean backup if needed
- [ ] Deploy more monitoring

---

## PHASE 4: GET BACK TO NORMAL - 4-24 Hours

### **Step 1: Get Account Working Again**
- [ ] Re-enable if it was disabled
- [ ] Test that password works
- [ ] Test access to files/programs
- [ ] Test email
- [ ] Check everything's normal
- [ ] Document completion

---

### **Step 2: Talk to the User**
- [ ] Explain what happened (simple version)
- [ ] Explain what we did to fix it
- [ ] Tell them how to prevent it next time:
  - Use strong, unique passwords
  - Turn on MFA
  - Be suspicious of emails
  - Don't share passwords
  - Report weird stuff
  - Keep devices secure
  - Use password manager

- [ ] Give them support contact
- [ ] Schedule follow-up

---

### **Step 3: Do They Need All That Access?**
- [ ] Did they really need all their permissions?
- [ ] Can we reduce what they can access?
- [ ] Do we need to restrict anything?
- [ ] Least privilege principle
- [ ] Document their new baseline

---

### **Step 4: Check Their Password Habits**
- [ ] Do they reuse passwords? (teach password manager)
- [ ] Are passwords strong? (provide guidance)
- [ ] Do they share passwords? (address this)
- [ ] Is MFA on? (encourage if not)
- [ ] Do they know how to reset password?

---

## PHASE 5: WHAT DID WE LEARN?

### **Team Meeting Within 1 Week**

**Talk About:**
1. How did we find out about it?
2. Why was detection delayed?
3. How did they get in?
4. Could we have caught it faster?
5. Were security controls in place?
6. What failed?
7. What prevented detection?
8. How do we prevent this next time?

---

### **Fix Immediately (Within 48 hours):**
- [ ] Turn on MFA for this user
- [ ] Reset related passwords
- [ ] Update antivirus/anti-malware
- [ ] Patch vulnerabilities
- [ ] Update firewall

---

### **Bigger Fixes (Within 30 days):**
- [ ] Organization-wide MFA
- [ ] Check for password reuse
- [ ] Impossible travel detection
- [ ] Watch for email forwarding changes
- [ ] Security training
- [ ] Better password rules
- [ ] Better behavior detection

---

## How To Prevent This

**For Everyone:**

### **Password & Login Security:**
- Strong, unique passwords
- MFA everywhere
- No password reuse
- Regular password changes (every 90 days or less)
- Automatic login alerts to users
- Session timeout
- Account lockout after failed attempts

### **Detection & Monitoring:**
- Impossible travel detection
- Weird location/time alerts
- Rate limiting for failed logins
- Login activity notifications
- Email rule change alerts
- Privilege escalation alerts

### **Access Control:**
- Only access what they need
- Regular access reviews (every 3 months)
- Protect admin accounts
- Rotate service account passwords
- Restrict admin accounts
- Log all access to sensitive systems

### **User Training:**
- Phishing awareness
- Password security
- Social engineering awareness
- How to report incidents
- Password manager training
- MFA how-to
- Regular security reminders

---

## Key Numbers to Track

**Timing:**
- Time from compromise to discovery: _____ hours/days
- Time to reset password: _____ min
- Time to full containment: _____ hours
- Time to full recovery: _____ hours

**Impact:**
- Systems user could access: _____
- Sensitive data potentially exposed: _____
- Emails sent by attacker: _____
- Data downloaded: _____

**Response Quality:**
- Followed playbook: Y/N
- Detection worked: Y/N
- Containment successful: Y/N
- Came back (72 hours): Y/N


---

*Account Compromise Response Playbook - Version 1.0*  
*Last Updated: April 17, 2026*