# 🌐 10-Day Networking & Protocol Fundamentals Lab

[![License: MIT](https://img.shields.io/badge/license-MIT-2563EB?style=flat-square)](LICENSE)
![Repository status: Active](https://img.shields.io/badge/status-Active-16A34A?style=flat-square)
![Branch: Main](https://img.shields.io/badge/branch-main-475569?style=flat-square)
![Tech stack](https://img.shields.io/badge/tools-PowerShell%20%7C%20Packet%20Tracer%20%7C%20Wireshark-0EA5E9?style=flat-square)

Build practical networking knowledge in ten focused days. This hands-on roadmap
starts with Layer 2 and Layer 3 fundamentals, then progresses through network
simulation, packet capture, protocol analysis, and security-focused exercises in
authorized, isolated lab environments.

## Learning Roadmap

```mermaid
graph TD
    A["Days 01–02<br/>Network identity, IP, ARP & ping"] --> B["Day 03<br/>Network simulation"]
    B --> C["Days 04–05<br/>Packet capture, protocols & routes"]
    C --> D["Days 06–07<br/>Local services & endpoint behavior"]
    D --> E["Day 08<br/>Socket audit & firewall boundaries"]
    E --> G["Day 09<br/>Reflected input & security headers"]
    G --> F["Day 10<br/>Review, notes & key takeaways"]

    classDef fundamentals fill:#dbeafe,stroke:#2563eb,color:#172554
    classDef analysis fill:#cffafe,stroke:#0891b2,color:#164e63
    classDef practice fill:#dcfce7,stroke:#16a34a,color:#14532d
    classDef review fill:#f3e8ff,stroke:#9333ea,color:#581c87
    class A fundamentals
    class B,C analysis
    class D,E,G practice
    class F review
```

## Progress

**Status key:** ✅ Completed · 🔄 In Progress · ⏳ Pending

| Day | Focus | Status | Notes / exercise |
|---|---|---|---|
| 01 | Network identity: interface, MAC and IP addresses, subnet mask, gateway, and DNS | ✅ Completed | [Day 01 notes](logs/10-day-networking-notes.txt) |
| 02 | ARP, ping, and observing the address-resolution cache | ✅ Completed | [Day 02 notes](logs/10-day-networking-notes.txt) |
| 03 | Complete a network-simulation challenge | ✅ Completed | [Packet Tracer lab](labs/day-03-packet-tracer/basic-IPv4-Configuration-completed.pkt) |
| 04 | Explore packet capture and protocol analysis | ✅ Completed | [Progress notes](logs/10-day-networking-notes.txt) |
| 05 | Trace routes and study wireless-security concepts in a lab | ✅ Completed | [Progress notes](logs/10-day-networking-notes.txt) |
| 06 | Host a basic web page locally | ✅ Completed | [Day 06 web lab](day6-web/index.html) |
| 07 | Probe metasearch endpoints and compare DNS, HTTP status, headers, and latency | ✅ Completed | [Probe script](day7-metasearch/metasearch_probe.py) · [Notes](logs/10-day-networking-notes.txt) |
| 08 | Audit a loopback listener, map its process, and test firewall permission boundaries | ✅ Completed | [Day 08 notes](logs/10-day-networking-notes.txt) |
| 09 | Audit reflected input, output encoding, debug information, and security headers in a local training app | ✅ Completed | [Training demo](day9-vuln-lab/vuln_demo.py) · [Day 09 notes](logs/10-day-networking-notes.txt) |
| 10 | Review the lab notes and summarize key learnings | ✅ Completed | [Day 10 reflection](logs/10-day-networking-notes.txt) |

## Day 6: Local Web Hosting

The static page in [`day6-web/index.html`](day6-web/index.html) can be served locally with Python:

```powershell
cd day6-web
python -m http.server 8080
```

Open `http://127.0.0.1:8080/` in a browser. Press `Ctrl+C` to stop the server.
The page was verified with a `200 OK` response and the server log recorded
`GET / HTTP/1.1 200`. Full execution and verification notes are in
[`logs/10-day-networking-notes.txt`](logs/10-day-networking-notes.txt).

## Challenge Summary

The ten-day progression covered network addressing and reachability, routing
and packet behavior, local services, endpoint resilience, and practical
application and host security. The final reflection and day-by-day observations
are recorded in the [challenge notes](logs/10-day-networking-notes.txt).

> **Lab safety:** Perform hands-on exercises only on systems and networks you
> own or are explicitly authorized to use. Keep security experiments isolated
> from production and public networks.

## Tech Stack & Environment

- **Platform:** Windows with Windows PowerShell
- **Network diagnostics:** `ipconfig`, `ping`, `arp`, and `tracert`
- **Network simulation:** Cisco Packet Tracer
- **Packet capture and analysis:** Wireshark
- **Scripting and automation:** Python
- **Version control:** Git and GitHub

Tools are introduced as the roadmap progresses; the repository's notes record
completed exercises and observations.

## Repository Structure

```text
10-day-networking-lab/
├── assets/
│   └── 10-days-roadmap.png
├── day6-web/
│   └── index.html             # Local Python HTTP server test page
├── day7-metasearch/
│   ├── 4get/
│   │   └── docker-compose.yml
│   ├── searxng/
│   │   └── docker-compose.yml
│   └── metasearch_probe.py
├── day9-vuln-lab/
│   └── vuln_demo.py
├── labs/
│   └── day-03-packet-tracer/
│       └── basic-IPv4-Configuration-completed.pkt
├── logs/
│   └── 10-day-networking-notes.txt
├── LICENSE
└── README.md
```
