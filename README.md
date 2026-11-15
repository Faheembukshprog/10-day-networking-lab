# 🌐 10-Day Networking & Protocol Fundamentals Lab 🚀🛡️

![License: MIT](https://img.shields.io/badge/license-MIT-2563EB?style=for-the-badge)
![Repository status: Active](https://img.shields.io/badge/status-Active-16A34A?style=for-the-badge)
![Branch: Main](https://img.shields.io/badge/branch-main-475569?style=for-the-badge)
![Tech stack](https://img.shields.io/badge/tools-PowerShell%20%7C%20Packet%20Tracer%20%7C%20Wireshark-0EA5E9?style=for-the-badge)

Build practical networking knowledge in ten focused days. This hands-on roadmap
starts with Layer 2 and Layer 3 fundamentals, then progresses through network
simulation, packet capture, protocol analysis, and security-focused exercises in
authorized, isolated lab environments.

## Learning Roadmap

```mermaid
graph TD
    A["Days 01–02<br/>Network identity, IP, ARP & ping"] --> B["Day 03<br/>Network simulation"]
    B --> C["Days 04–05<br/>Packet capture, protocols & routes"]
    C --> D["Days 06–07<br/>Local services & self-hosting"]
    D --> E["Days 08–09<br/>Isolated security labs & evaluation"]
    E --> F["Day 10<br/>Review, notes & key takeaways"]

    classDef fundamentals fill:#dbeafe,stroke:#2563eb,color:#172554
    classDef analysis fill:#cffafe,stroke:#0891b2,color:#164e63
    classDef practice fill:#dcfce7,stroke:#16a34a,color:#14532d
    classDef review fill:#f3e8ff,stroke:#9333ea,color:#581c87
    class A fundamentals
    class B,C analysis
    class D,E practice
    class F review
```

## Progress

**Status key:** ✅ Completed · 🔄 In Progress · ⏳ Pending

| Day | Focus | Status | Notes / exercise |
|---|---|---|---|
| 01 | Network identity: interface, MAC and IP addresses, subnet mask, gateway, and DNS | ✅ Completed | [Day 01 notes](logs/10-day-networking-notes.txt) |
| 02 | ARP, ping, and observing the address-resolution cache | ✅ Completed | [Day 02 notes](logs/10-day-networking-notes.txt) |
| 03 | Complete a network-simulation challenge | ⏳ Pending | [Roadmap](assets/10-days-roadmap.png) |
| 04 | Explore packet capture and protocol analysis | ⏳ Pending | [Roadmap](assets/10-days-roadmap.png) |
| 05 | Trace routes and study wireless-security concepts in a lab | ⏳ Pending | [Roadmap](assets/10-days-roadmap.png) |
| 06 | Host a basic web page locally | ⏳ Pending | [Roadmap](assets/10-days-roadmap.png) |
| 07 | Explore a self-hosted metasearch service | ⏳ Pending | [Roadmap](assets/10-days-roadmap.png) |
| 08 | Work through an isolated network-security lab | ⏳ Pending | [Roadmap](assets/10-days-roadmap.png) |
| 09 | Evaluate a deliberately vulnerable training environment | ⏳ Pending | [Roadmap](assets/10-days-roadmap.png) |
| 10 | Review the lab notes and summarize key learnings | ⏳ Pending | [Progress notes](logs/10-day-networking-notes.txt) |

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
├── labs/                         # Workspace for hands-on lab material
├── logs/
│   └── 10-day-networking-notes.txt
├── LICENSE
└── README.md
```
