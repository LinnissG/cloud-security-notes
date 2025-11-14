# 01 – The CIA Triad (Beginner Cybersecurity Notes)

The CIA Triad is the foundation of all cybersecurity.  
It stands for:

---

## 🔐 1. Confidentiality  
Making sure information is only accessed by people who are **authorized**.

**Examples:**
- Passwords protecting your bank app  
- Encryption (scrambling data so others can’t read it)
- Multi-factor authentication (MFA)

Think:  
> “Who is allowed to see this?”

---

## 🌱 2. Integrity  
Ensuring data is **accurate**, **unchanged**, and **trustworthy**.

**Examples:**
- A file not being edited by someone unauthorized  
- Hashing to detect tampering  
- Version control (like Git!)

Think:  
> “Is this information correct and unmodified?”

---

## ⚙️ 3. Availability  
Making sure systems and data are available when needed.

**Examples:**
- Websites staying online  
- Backups  
- Redundant servers  
- DDoS protection

Think:  
> “Can users access this when they need it?”

---

## 🔁 Why does this matter for cloud security?

The cloud (Azure, AWS, Google Cloud) stores millions of systems and data sets.  
Protecting them revolves around the CIA model:

| Cloud Security Concept | Which CIA Element? |
|------------------------|--------------------|
| Encryption             | Confidentiality    |
| IAM permissions        | Confidentiality    |
| Backups                | Availability       |
| Logging                | Integrity          |
| Multi-region apps      | Availability       |

This is one of the FIRST things cloud security engineers think about.

---

## ✔️ Summary in My Own Words

The CIA Triad is the foundation of cybersecurity. It stands for Confidentiality, Integrity, and Availability. 
These three principles help protect data and systems by making sure information is only seen by the right people, stays accurate and unmodified, and is available when needed.
Every security control, whether in cloud or traditional IT, is built around these three goals.
---

**My Understanding:**  
The CIA Triad helps me understand what security is actually trying to protect. 
Confidentiality is about keeping information private and making sure only the right people can access it. 
Integrity means the data stays correct and nobody has changed it behind the scenes. 
Availability means everything should be up and working when people need it. 
Thinking about these three together helps me see why security controls exist and how cloud systems stay protected.
