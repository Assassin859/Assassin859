<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&duration=3000&pause=1000&color=2563EB&center=true&vCenter=true&width=750&lines=Hi%2C+I'm+Maitreya+Gaikwad+%F0%9F%91%8B;Blockchain+%26+Web3+Developer;Smart+Contracts+%7C+DeFi+%7C+Solana;Building+production-grade+Web3+systems" alt="Typing SVG" />

<br/>

![Profile Views](https://komarev.com/ghpvc/?username=Assassin859&color=2563EB&style=for-the-badge&label=PROFILE+VIEWS)
[![Twitter](https://img.shields.io/twitter/follow/assassin_859?style=for-the-badge&color=1DA1F2&logo=twitter&label=TWITTER)](https://twitter.com/assassin_859)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/maitreya-gaikwad-9b358b2a4)

</div>

---

## 🌐 Web3 Developer Dashboard

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

import "@openzeppelin/contracts/access/Ownable.sol";

contract MaitreyaGaikwad is Ownable, Developer {
    string public constant name = "Maitreya Gaikwad";
    string public constant role = "Blockchain & Web3 Systems Architect";
    string public constant location = "Mumbai, India";
    
    mapping(string => string[]) public skills;
    
    constructor() {
        skills["languages"] = ["Solidity", "TypeScript", "JavaScript", "Python", "SQL", "HTML/CSS"];
        skills["blockchain"] = ["Ethereum", "Solana", "Hyperledger Besu", "Ethers.js", "Web3.js", "Wagmi", "Hardhat", "Truffle", "OpenZeppelin"];
        skills["backend"] = ["Node.js", "Express.js", "Supabase", "PostgreSQL", "MySQL", "REST APIs"];
        skills["devops"] = ["AWS (EC2)", "Docker", "Git/GitHub", "CI/CD (pipelines)"];
        skills["ai_assisted"] = ["Antigravity IDE", "Claude Code", "Cursor", "GitHub Copilot"];
    }
}
```

---

## 📑 Block Explorer (Verified Project Deployments)

<div style="border: 1px solid #30363d; border-radius: 8px; overflow: hidden; background-color: #0d1117; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 13px;">
    <thead>
      <tr style="background-color: #161b22; border-bottom: 1px solid #30363d;">
        <th style="padding: 12px; color: #8b949e; font-weight: 600; font-family: monospace;">Txn Hash</th>
        <th style="padding: 12px; color: #8b949e; font-weight: 600; font-family: monospace;">Method</th>
        <th style="padding: 12px; color: #8b949e; font-weight: 600;">Block</th>
        <th style="padding: 12px; color: #8b949e; font-weight: 600;">To (Verified Contract / Project)</th>
        <th style="padding: 12px; color: #8b949e; font-weight: 600; text-align: right;">Status</th>
      </tr>
    </thead>
    <tbody>
      <!-- Row 1 -->
      <tr style="border-bottom: 1px solid #21262d;">
        <td style="padding: 12px;"><a href="https://github.com/Assassin859/cryptp" style="color: #58a6ff; text-decoration: none; font-family: monospace; font-size: 12px;">0xa82d...7f6b</a></td>
        <td style="padding: 12px;"><span style="background-color: rgba(56, 189, 248, 0.1); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.2); padding: 3px 6px; border-radius: 4px; font-family: monospace; font-size: 11px;">deployAtheonIDE</span></td>
        <td style="padding: 12px; color: #c9d1d9;">2025 – 2026</td>
        <td style="padding: 12px;"><a href="https://cryptp-production.up.railway.app" style="color: #58a6ff; font-weight: 600; text-decoration: none;">Atheon IDE</a> <span style="color: #8b949e; font-size: 11px;">(Browser-native gas cost heatmap, built-in AI linting, WASM terminal)</span></td>
        <td style="padding: 12px; text-align: right;"><span style="background-color: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.3); padding: 3px 8px; border-radius: 20px; font-size: 11px; font-weight: 500;">Success</span></td>
      </tr>
      <!-- Row 2 -->
      <tr style="border-bottom: 1px solid #21262d;">
        <td style="padding: 12px;"><a href="https://pharbit.com" style="color: #58a6ff; text-decoration: none; font-family: monospace; font-size: 12px;">0x4d2e...9a3c</a></td>
        <td style="padding: 12px;"><span style="background-color: rgba(139, 92, 246, 0.1); color: #a78bfa; border: 1px solid rgba(139, 92, 246, 0.2); padding: 3px 6px; border-radius: 4px; font-family: monospace; font-size: 11px;">createPharbitChain</span></td>
        <td style="padding: 12px; color: #c9d1d9;">2024 – 2026</td>
        <td style="padding: 12px;"><a href="https://pharbit.com" style="color: #58a6ff; font-weight: 600; text-decoration: none;">Pharbit System</a> <span style="color: #8b949e; font-size: 11px;">(Besu Ethereum private chain, 5 Solidity contracts, 4-node AWS validation)</span></td>
        <td style="padding: 12px; text-align: right;"><span style="background-color: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.3); padding: 3px 8px; border-radius: 20px; font-size: 11px; font-weight: 500;">Success</span></td>
      </tr>
      <!-- Row 3 -->
      <tr style="border-bottom: 1px solid #21262d;">
        <td style="padding: 12px;"><a href="https://github.com/Assassin859/vaultflow" style="color: #58a6ff; text-decoration: none; font-family: monospace; font-size: 12px;">0x92f8...2b1a</a></td>
        <td style="padding: 12px;"><span style="background-color: rgba(56, 189, 248, 0.1); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.2); padding: 3px 6px; border-radius: 4px; font-family: monospace; font-size: 11px;">launchVaultFlow</span></td>
        <td style="padding: 12px; color: #c9d1d9;">2025</td>
        <td style="padding: 12px;"><a href="https://vaultflow-production-8062.up.railway.app" style="color: #58a6ff; font-weight: 600; text-decoration: none;">VaultFlow DeFi</a> <span style="color: #8b949e; font-size: 11px;">(Lending protocol on Oasis Sapphire Testnet, collateral management)</span></td>
        <td style="padding: 12px; text-align: right;"><span style="background-color: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.3); padding: 3px 8px; border-radius: 20px; font-size: 11px; font-weight: 500;">Success</span></td>
      </tr>
      <!-- Row 4 -->
      <tr style="border-bottom: 1px solid #21262d;">
        <td style="padding: 12px;"><a href="https://github.com/Assassin859/chainquest-home-task" style="color: #58a6ff; text-decoration: none; font-family: monospace; font-size: 12px;">0x7c3a...6e8f</a></td>
        <td style="padding: 12px;"><span style="background-color: rgba(139, 92, 246, 0.1); color: #a78bfa; border: 1px solid rgba(139, 92, 246, 0.2); padding: 3px 6px; border-radius: 4px; font-family: monospace; font-size: 11px;">deployChainQuest</span></td>
        <td style="padding: 12px; color: #c9d1d9;">2024</td>
        <td style="padding: 12px;"><a href="https://github.com/Assassin859/chainquest-home-task" style="color: #58a6ff; font-weight: 600; text-decoration: none;">ChainQuest</a> <span style="color: #8b949e; font-size: 11px;">(On-chain bounty escrow with ETH/ERC-20 & 3% fee routing logic)</span></td>
        <td style="padding: 12px; text-align: right;"><span style="background-color: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.3); padding: 3px 8px; border-radius: 20px; font-size: 11px; font-weight: 500;">Success</span></td>
      </tr>
      <!-- Row 5 -->
      <tr style="border-bottom: 1px solid #21262d;">
        <td style="padding: 12px;"><a href="https://github.com/Assassin859/AI-CFO" style="color: #58a6ff; text-decoration: none; font-family: monospace; font-size: 12px;">0x5d8c...3b9e</a></td>
        <td style="padding: 12px;"><span style="background-color: rgba(56, 189, 248, 0.1); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.2); padding: 3px 6px; border-radius: 4px; font-family: monospace; font-size: 11px;">initAICFO</span></td>
        <td style="padding: 12px; color: #c9d1d9;">2024</td>
        <td style="padding: 12px;"><a href="https://github.com/Assassin859/AI-CFO" style="color: #58a6ff; font-weight: 600; text-decoration: none;">AI-CFO</a> <span style="color: #8b949e; font-size: 11px;">(AI startup treasury management with forecasting models)</span></td>
        <td style="padding: 12px; text-align: right;"><span style="background-color: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.3); padding: 3px 8px; border-radius: 20px; font-size: 11px; font-weight: 500;">Success</span></td>
      </tr>
      <!-- Row 6 -->
      <tr style="border-bottom: 1px solid #21262d;">
        <td style="padding: 12px;"><a href="https://github.com/Assassin859/mini-project" style="color: #58a6ff; text-decoration: none; font-family: monospace; font-size: 12px;">0x3c9b...5a1d</a></td>
        <td style="padding: 12px;"><span style="background-color: rgba(139, 92, 246, 0.1); color: #a78bfa; border: 1px solid rgba(139, 92, 246, 0.2); padding: 3px 6px; border-radius: 4px; font-family: monospace; font-size: 11px;">runSharkTankSim</span></td>
        <td style="padding: 12px; color: #c9d1d9;">2024</td>
        <td style="padding: 12px;"><a href="https://github.com/Assassin859/mini-project" style="color: #58a6ff; font-weight: 600; text-decoration: none;">Shark Tank Simulator</a> <span style="color: #8b949e; font-size: 11px;">(Interactive business game with AI investor feedback mechanics)</span></td>
        <td style="padding: 12px; text-align: right;"><span style="background-color: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.3); padding: 3px 8px; border-radius: 20px; font-size: 11px; font-weight: 500;">Success</span></td>
      </tr>
      <!-- Row 7 — 2026 OSS -->
      <tr style="border-bottom: 1px solid #21262d;">
        <td style="padding: 12px;"><a href="https://github.com/KeeperHub/keeperhub/pull/1763" style="color: #58a6ff; text-decoration: none; font-family: monospace; font-size: 12px;">0x1763...3312</a></td>
        <td style="padding: 12px;"><span style="background-color: rgba(16, 185, 129, 0.1); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.2); padding: 3px 6px; border-radius: 4px; font-family: monospace; font-size: 11px;">mergeSolanaAdapter</span></td>
        <td style="padding: 12px; color: #34d399; font-weight: 600;">2026</td>
        <td style="padding: 12px;"><a href="https://github.com/KeeperHub/keeperhub/pull/1763" style="color: #58a6ff; font-weight: 600; text-decoration: none;">KeeperHub #1761 & #1763</a> <span style="color: #8b949e; font-size: 11px;">(Full Solana ChainAdapter — read + write side, Turnkey signing, 3,312 lines merged)</span></td>
        <td style="padding: 12px; text-align: right;"><span style="background-color: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.3); padding: 3px 8px; border-radius: 20px; font-size: 11px; font-weight: 500;">Merged ✓</span></td>
      </tr>
      <!-- Row 8 — 2026 OSS -->
      <tr>
        <td style="padding: 12px;"><a href="https://github.com/OpenZeppelin/openzeppelin-contracts/pull/6604" style="color: #58a6ff; text-decoration: none; font-family: monospace; font-size: 12px;">0x6604...0z3p</a></td>
        <td style="padding: 12px;"><span style="background-color: rgba(16, 185, 129, 0.1); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.2); padding: 3px 6px; border-radius: 4px; font-family: monospace; font-size: 11px;">addMerkleTreeTests</span></td>
        <td style="padding: 12px; color: #34d399; font-weight: 600;">2026</td>
        <td style="padding: 12px;"><a href="https://github.com/OpenZeppelin/openzeppelin-contracts/pull/6604" style="color: #58a6ff; font-weight: 600; text-decoration: none;">OpenZeppelin #6604</a> <span style="color: #8b949e; font-size: 11px;">(Non-commutative hashing test coverage for MerkleTree library — approved by core maintainers)</span></td>
        <td style="padding: 12px; text-align: right;"><span style="background-color: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.3); padding: 3px 8px; border-radius: 20px; font-size: 11px; font-weight: 500;">Merged ✓</span></td>
      </tr>
    </tbody>
  </table>
</div>

---

## 🤝 Open Source Contributions

| Project | Contribution Detail |
| :--- | :--- |
| **[KeeperHub](https://github.com/KeeperHub/keeperhub)** | **Solana ChainAdapter & Concurrency Fix**<br>• Deployed the read-side Solana ChainAdapter (balance queries, explorer URLs, failover handling) including a concurrency fix for shared provider caching (#1761, 606 lines).<br>• Deployed the write-side Solana ChainAdapter (Turnkey transaction signing, native SOL transfer routing, dual EVM+Solana account provisioning; #1763, 2,706 lines). |
| **[OpenZeppelin](https://github.com/OpenZeppelin/openzeppelin-contracts)** | **MerkleTree Library Testing**<br>• Added non-commutative hashing test coverage for MerkleTree library (#6604). Approved and merged by core maintainers. |

> 🟣 **KeeperHub Community Partner** — recognized for Solana ecosystem contributions.

---

## 🎓 Certifications & Education

* 🎓 **B.E. in Computer Science (Blockchain Specialization)** — University of Mumbai (Expected 2028)
* 📜 **Build on BNB Chain** — BNB Chain Fundamentals by Rise In (Jul 2025)
* 📜 **Ethereum Bootcamp** — Alchemy University (2024)
* 📜 **AI for Techies** — Microsoft (Feb 2025)

---

## 🏆 Badges & Stats

<div align="center">

[![Trophies](https://github-profile-trophy-fork-two.vercel.app/?username=Assassin859&theme=tokyonight&no-bg=true&no-frame=true&margin-w=15)](https://github.com/ryo-ma/github-profile-trophy)

<br/>

![Maitreya's GitHub Stats](https://github-readme-stats-sigma-five.vercel.app/api?username=Assassin859&show_icons=true&theme=tokyonight&hide_border=true&count_private=true)
![Top Languages](https://github-readme-stats-sigma-five.vercel.app/api/top-langs/?username=Assassin859&layout=compact&theme=tokyonight&hide_border=true&langs_count=6)

</div>

### 🐍 Contribution Snake

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

*Building at the intersection of blockchain infrastructure and developer tooling.*

</div>
