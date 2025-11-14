# 02 – Ports & Protocols (Beginner Cybersecurity Notes)

Understanding ports and protocols is essential for networking and cybersecurity.  
Every device on a network communicates using **ports** (doorways) and **protocols** (rules).

---

# 🔌 What Are Ports?

A **port** is like a doorway on a computer or server that allows certain types of traffic in or out.

- Ports are numbered **0–65535**
- They help organize different kinds of network communication
- Security analysts must know common ports to identify suspicious traffic

Example:  
When you visit a website using HTTPS, your computer automatically uses **Port 443**.

---

# 📡 What Are Protocols?

A **protocol** is a rulebook that defines how data is sent and received.

Examples:
- HTTP/HTTPS – web browsing
- SMTP – email
- DNS – domain lookups

Protocols use ports to communicate.

---

# 🔢 Most Important Ports (You MUST Know These)

| Port | Protocol | What It Does |
|------|----------|---------------|
| **80**  | HTTP       | Unsecured web traffic |
| **443** | HTTPS      | Secure web browsing (encrypted) |
| **22**  | SSH        | Secure remote login |
| **21**  | FTP        | File transfer (insecure) |
| **53**  | DNS        | Domain name lookups |
| **25**  | SMTP       | Sending email |
| **110** | POP3       | Receiving email |
| **143** | IMAP       | Receiving email |
| **3389**| RDP        | Remote Desktop Protocol |
| **3306**| MySQL      | Database traffic |
| **1433**| MSSQL      | Microsoft SQL Server |

These 10–15 ports appear in:
- Security+  
- SSCP  
- Real job interviews  
- Cloud network security setups  
- Firewall rules  
- SIEM alerts

---

# 🛡 Why Ports Matter in Security

Ports help identify:
- What services are running
- What traffic should or should NOT be happening
- Suspicious scanning (like nmap scans)
- Misconfigurations
- Attacks (RDP attacks often target Port 3389)

Example:  
If a server has **Port 22** open to the entire internet, that’s a security risk.

---

# 🌩 Ports in the Cloud (Very Important!)

In AWS or Azure:
- Security Groups / NSGs control which ports are open
- By default, cloud servers should have LIMITED ports open
- Cloud services often only allow ports you explicitly configure

Example:
- AWS EC2 web server → Port 443 open only
- Azure VM for SSH → Port 22 restricted to **your IP only**

---

# 📝 Summary (In My Own Words)

Ports are basically doorways on a device that let specific types of network traffic come in and out. 
Protocols are the rules that tell the traffic how to communicate and what format to use. 
Knowing which ports should be open and what protocol is behind them is important for security, because attackers often test those doorways to find vulnerabilities.
