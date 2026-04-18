# Incident Response Framework

## Overview

This document explains the basic framework and key ideas we use for all the incident response playbooks in this project. It's meant to be a guide so everyone on the team knows how to handle security incidents the same way.

---

## NIST Incident Response Lifecycle

Our playbooks follow the **NIST Cybersecurity Framework** phases for handling incidents. Here's how it breaks down:

### **Phase 1: Preparation**
Before anything bad happens, we need to be ready:
- Have the right tools and procedures set up
- Make sure the team knows what to do (training matters)
- Configure systems to detect problems
- Set up ways for the team to communicate

### **Phase 2: Detection & Analysis**
When something might be wrong, we figure out what's happening:
- Spot potential security incidents
- Look for indicators of compromise (IOCs) - basically evidence that something went wrong
- Figure out what type of attack it is and how serious it is
- Check what the damage might be so far

### **Phase 3: Containment, Eradication & Recovery**
Now it's time to actually fix things:
- Stop the attacker from doing more damage
- Remove the threat from our systems
- Make sure they can't get back in
- Get everything back to normal

### **Phase 4: Post-Incident Activities**
After it's over, we learn from it:
- Look back at how we handled it
- Write down what we learned
- Update our procedures and tools so it doesn't happen the same way again
- Share what happened with the people who need to know

---

## Incident Severity Levels

Not all incidents are the same. Here's how we rank them:

### **CRITICAL**
- The attack is still happening right now
- Lots of systems are affected
- We probably have to tell customers or follow some law about reporting it
- Management needs to know immediately
- Someone's got to be working on it 24/7

### **HIGH**
- Multiple systems got compromised
- Important data might be at risk
- We need to jump on this right away

### **MEDIUM**
- Only one system or a few systems are affected
- It's bad but manageable
- We handle this with our normal procedures

### **LOW**
- Just one thing is affected
- It's not a big deal
- Can wait until normal business hours
- Just keep an eye on it

---

## Key Response Principles

### **1. Speed Matters**
- The faster we respond, the less damage happens
- Having plans ahead of time saves us precious minutes
- Knowing who to call and when prevents confusion

### **2. Tell People What's Going On**
- Keep everyone in the loop (management, team, whoever needs to know)
- Be clear and honest about what's happening
- Don't sugarcoat it, but don't panic either

### **3. Save the Evidence**
- Write everything down as it happens
- Keep track of what happened and in what order (chain of custody)
- Don't delete stuff we might need later for investigating or legal stuff

### **4. Stop the Bleeding First**
- Lock things down before we try to figure out how they got in
- Prevent them from doing more damage
- We can investigate the root cause after we've contained it

### **5. Work Together**
- Everyone knows their job
- One person is in charge of coordinating the response
- We give regular updates so everyone knows where we stand

---

## Escalation Procedures

Depending on how serious it is, different people get involved:

### **Level 1: SOC Analyst**
- First person to notice something's wrong
- Does the first analysis and tries to contain it
- Writes down what they find

### **Level 2: Incident Response Lead**
- Takes over and coordinates everyone
- Decides what we're going to do
- Talks to people above them and outside people (like vendors)

### **Level 3: Security Manager**
- Handles the big incidents that need more oversight
- Decides when to escalate to executives
- Makes sure people outside the security team know what's going on

### **Level 4: Executive Leadership**
- Only called for the really serious stuff
- Gets briefed on what happened and what we're doing
- Makes decisions about the business side of things (like whether to shut systems down, tell customers, etc.)

---

## Investigation Checklist

Every time we have an incident, we check off these things:

- [ ] When did we first notice it? How?
- [ ] Saved all the evidence we need?
- [ ] Which systems got hit?
- [ ] How much of the system is compromised?
- [ ] How did they get in?
- [ ] Write down what happened and when
- [ ] What did the attacker do once they were in?
- [ ] What data could they have seen?
- [ ] What actually caused this to happen in the first place?

---

## Communication Templates

We use these to keep everyone updated:

### **Initial Alert (First Hour)**
**Subject:** SECURITY INCIDENT ALERT - [Type of Attack]

Include:
- What type of attack this is and how serious
- Which systems are affected
- What we think the damage is right now
- What we're doing about it
- When you'll hear from us again

### **Status Update (Every 4 Hours)**
**Subject:** SECURITY INCIDENT UPDATE - [Type of Attack]

Include:
- Where things stand right now
- What we've found so far
- What we've done
- When we think we'll have this fixed
- Is anything still down or broken?

### **It's Fixed (When Contained)**
**Subject:** SECURITY INCIDENT RESOLVED - [Type of Attack]

Include:
- We got it under control
- What actually caused it (in simple terms)
- What we did to stop it
- How we're making sure it doesn't happen the same way again
- What we learned

---

## Post-Incident Review Questions

After everything's settled, we ask ourselves:

1. **Detection:** Did we catch this pretty quickly?
2. **Response:** Did we actually follow our procedures?
3. **Containment:** Did stopping the attack work?
4. **Investigation:** Did we figure out what caused it?
5. **Recovery:** Is everything back to normal?
6. **Communication:** Did we keep people informed?
7. **Prevention:** What could've helped us catch this earlier?
8. **Next Time:** What should we do differently?

---

## Key Metrics

We track these numbers to see how we're doing:

- **Time to Detect (TTD):** How long until we noticed the problem?
- **Time to Respond (TTR):** How long until we started fixing it?
- **Time to Contain (TTC):** How long to stop the attack?
- **Time to Resolve (MTTR):** How long to get everything back to normal?
- **Impact:** What data was affected? What systems went down? What's the impact on the business?

---

## Tools & Resources

**For Finding Problems:**
- SIEM (Security Information & Event Management) - basically looks through a bunch of logs to find weird stuff
- EDR (Endpoint Detection & Response) - monitors individual computers/servers for suspicious activity
- IDS/IPS (Intrusion Detection/Prevention) - watches network traffic for attacks

**For Investigating:**
- Wireshark - lets you see network traffic in detail
- Volatility - digs through computer memory to find traces of what happened
- EnCase - looks at hard drives to recover files and find evidence

**For Talking to Each Other:**
- Slack/Teams - quick messages with the team
- Email - official records and documentation
- Conference calls - coordinate during the actual incident

---

## References

- NIST Cybersecurity Framework: https://www.nist.gov/cyberframework
- NIST SP 800-61: Incident Handling Guide
- SANS Incident Response: https://www.sans.org/

---

*This framework is used for all incident response playbooks in this project*