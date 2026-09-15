<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&duration=3000&pause=1000&color=2563EB&center=true&vCenter=true&width=750&lines=Hi%2C+I'm+Maitreya+Gaikwad+%F0%9F%91%8B;Blockchain+%26+Web3+Developer;Smart+Contracts+%7C+DeFi+%7C+Solana;Building+production-grade+Web3+systems" alt="Typing SVG" />

<br/>

![Profile Views](https://komarev.com/ghpvc/?username=Assassin859&color=2563EB&style=for-the-badge&label=PROFILE+VIEWS)
[![Twitter](https://img.shields.io/twitter/follow/assassin_859?style=for-the-badge&color=1DA1F2&logo=twitter&label=TWITTER)](https://twitter.com/assassin_859)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/maitreya-gaikwad-9b358b2a4)
[![GitHub](https://img.shields.io/badge/GitHub-Assassin859-181717?style=for-the-badge&logo=github)](https://github.com/Assassin859)
[![Email](https://img.shields.io/badge/Email-maitreyagaikwad859%40gmail.com-EA4335?style=for-the-badge&logo=gmail)](mailto:maitreyagaikwad859@gmail.com)

</div>

---

## About

Blockchain & backend developer with ~2 years of production experience building decentralized systems, smart contracts, and full-stack Web3 apps.

- Sole engineer on a private Ethereum pharma supply-chain platform (**Hyperledger Besu**, IBFT 2.0, 4-node AWS, 5 production Solidity contracts)
- **KeeperHub Community Partner** — 19 merged PRs (~18.5k LOC) across Solana adapter, MCP/agent DX, and execution safety
- Merged contributor to **OpenZeppelin Contracts**
- **ETHOnline 2026** (ETHGlobal) · **DoraHacks** Best UI/UX bounty winner

**Focus:** execution safety, money-moving correctness, and developer tooling.

---

## Web3 Developer Dashboard

<div align="center">
  <table>
    <tr>
      <td valign="top">
        <img src="https://raw.githubusercontent.com/Assassin859/Assassin859/main/metamask.svg" width="310" alt="MetaMask Wallet Mockup" />
      </td>
      <td valign="top">
        <img src="https://raw.githubusercontent.com/Assassin859/Assassin859/main/terminal.svg" width="490" alt="Foundry Terminal Mockup" />
      </td>
    </tr>
  </table>
</div>

---

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

/// @title Profile — stylized skill registry (not deployed)
/// @notice Maitreya Gaikwad · Blockchain & Web3 Developer · Mumbai, India
contract Profile {
    string public constant NAME = "Maitreya Gaikwad";
    string public constant ROLE = "Blockchain Developer | Smart Contracts & Web3 Infrastructure";
    string public constant LOCATION = "Mumbai, India | Remote";

    string[] public languages;
    string[] public blockchain;
    string[] public backend;
    string[] public devops;

    constructor() {
        languages = ["Solidity", "TypeScript", "JavaScript", "Python", "SQL"];
        blockchain = [
            "Ethereum",
            "Solana",
            "Hyperledger Besu (IBFT 2.0)",
            "Hardhat",
            "Foundry",
            "OpenZeppelin",
            "Ethers.js",
            "Wagmi",
            "Web3.js",
            "IPFS"
        ];
        backend = ["Node.js", "Express.js", "Supabase", "PostgreSQL", "MySQL", "REST APIs"];
        devops = ["AWS (EC2)", "Docker", "GitHub Actions / CI-CD", "Vercel", "Netlify"];
    }
}
```

---

## Block Explorer (Projects & Deployments)

| Txn | Method | Block | Project | Status |
| :--- | :--- | :--- | :--- | :---: |
| [`0xa82d…7f6b`](https://github.com/Assassin859/cryptp) | `deployAethonIDE` | 2025–Present | **[Aethon IDE](https://cryptp-production.up.railway.app)** — browser-native Solidity IDE with gas heatmap, AI security linting, WASM terminal · ETHOnline 2026 | Success |
| [`0x4d2e…9a3c`](https://pharbit.com) | `createPharbitChain` | 2024–2026 | **[Pharbit](https://pharbit.com)** — Besu private chain, 5 Solidity contracts, 4-node AWS validators · [codebase](https://github.com/Maitreyapharbit/Blockchain) | Success |
| [`0x92f8…2b1a`](https://github.com/Assassin859/vaultflow) | `launchVaultFlow` | 2025 | **[VaultFlow](https://vaultflow-production-8062.up.railway.app)** — DeFi lending on Oasis Sapphire Testnet | Success |
| [`0x7c3a…6e8f`](https://github.com/Assassin859/chainquest-home-task) | `deployChainQuest` | 2024 | **[ChainQuest](https://github.com/Assassin859/chainquest-home-task)** — on-chain bounty escrow (ETH/ERC-20, fee routing) | Success |
| [`0x5d8c…3b9e`](https://github.com/Assassin859/AI-CFO) | `initAICFO` | 2024 | **[AI-CFO](https://github.com/Assassin859/AI-CFO)** — AI startup treasury tooling | Success |
| [`0xkhub…19pr`](https://github.com/KeeperHub/keeperhub) | `mergeKeeperHubPRs` | 2026 | **[KeeperHub](https://github.com/KeeperHub/keeperhub)** — Community Partner · 19 merged PRs (Solana + MCP + execution safety) | Merged |
| [`0x6604…oz`](https://github.com/OpenZeppelin/openzeppelin-contracts/pull/6604) | `addMerkleTreeTests` | 2026 | **[OpenZeppelin #6604](https://github.com/OpenZeppelin/openzeppelin-contracts/pull/6604)** — MerkleTree non-commutative hashing tests | Merged |

---

## Open Source

### [KeeperHub](https://github.com/KeeperHub/keeperhub) — Community Partner · Jul–Sep 2026

**19 merged PRs** (~18.5k lines added) across three areas:

| Area | Highlights |
| :--- | :--- |
| **Solana foundation** | ChainAdapter read/write paths — balances, explorer URLs, failover, spend caps, SPL coverage, fees, blockhash retry, Turnkey signing |
| **Agent / MCP DX** | Dev-login recovery, MCP aliases & manifest sync, structured errors, auth → `apiError` envelope, hackathon quickstart docs |
| **Execution safety** | Required-param rejection, idempotency keys, refuse re-dispatch of terminal executions, stop For-Each on iteration failure |

Also filed [#2435](https://github.com/KeeperHub/keeperhub/issues/2435) (stablecoin-to-gas top-up) and implementing the follow-up PR.

### [OpenZeppelin Contracts](https://github.com/OpenZeppelin/openzeppelin-contracts)

- **[#6604](https://github.com/OpenZeppelin/openzeppelin-contracts/pull/6604)** — non-commutative hashing test coverage for `MerkleTree`; reviewed and merged by core maintainers

---

## Experience

| Role | Org | Period |
| :--- | :--- | :--- |
| **Blockchain Engineer (Contract)** | Pharbit Technologies · Remote / Germany | Aug 2024 – Jul 2026 |
| **Freelance Blockchain Developer** | Self-employed · Mumbai | May 2024 – Aug 2024 |

**Pharbit highlights:** sole engineer for full blockchain stack — Besu IBFT 2.0 network, USDT-backed custody contracts with OpenZeppelin access control + reentrancy guards, IPFS document verification, React + Supabase + Ethers.js admin dashboard.

---

## Hackathons

- **ETHOnline 2026 (ETHGlobal)** — submitted Aethon IDE (continuity track); Chainlink CRE, The Graph, Uniswap v4 CounterHook integrations
- **KeeperHub × DoraHacks 2026** — Winner, Best UI/UX Bounty

---

## Education & Certifications

- **B.E. Computer Science — Blockchain Specialization** · University of Mumbai · Expected 2028
- **Build on BNB Chain / BNB Chain Fundamentals** · Rise In · Jul 2025
- **Ethereum Bootcamp** · Alchemy University · 2024
- **AI for Techies** · Microsoft · Feb 2025

---

## Tech Stack

```text
Blockchain   Solidity · Hyperledger Besu · Ethereum · Solana · Hardhat · Foundry
             OpenZeppelin · IPFS · Ethers.js · Web3.js · Wagmi
Backend      Node.js · Express · Supabase · PostgreSQL · MySQL · REST
Frontend     React · Next.js · TypeScript · Tailwind · Monaco / Vite
Infra        AWS EC2 · Docker · GitHub Actions · Vercel · Netlify
```

---

## Stats

<div align="center">

[![Trophies](https://github-profile-trophy-fork-two.vercel.app/?username=Assassin859&theme=tokyonight&no-bg=true&no-frame=true&margin-w=15)](https://github.com/ryo-ma/github-profile-trophy)

<br/>

![GitHub Stats](https://github-readme-stats-sigma-five.vercel.app/api?username=Assassin859&show_icons=true&theme=tokyonight&hide_border=true&count_private=true)
![Top Languages](https://github-readme-stats-sigma-five.vercel.app/api/top-langs/?username=Assassin859&layout=compact&theme=tokyonight&hide_border=true&langs_count=6)

</div>

### Contribution snake

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Assassin859/Assassin859/output/github-contribution-grid-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Assassin859/Assassin859/output/github-contribution-grid-snake.svg">
  <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/Assassin859/Assassin859/output/github-contribution-grid-snake.svg">
</picture>

</div>

---

<div align="center">

[![Discord](https://img.shields.io/badge/Discord-maitsol-5865F2?style=for-the-badge&logo=discord)](https://discord.com)

**Available for remote contracts, internships & full-time Web3 roles** · Immediate

*Building at the intersection of blockchain infrastructure and developer tooling.*

</div>
