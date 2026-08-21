# 🧠 Proof of Contribution - GenLayer Intelligent Contract

This repository contains a standalone Python-based GenLayer Intelligent Contract designed to automate and decentralize the evaluation of Web3 community contributions.

Instead of relying on manual moderation, this contract leverages GenLayer's DeAI consensus to analyze the analytical depth and originality of a user's content. By fetching exact post records from an authoritative indexer, verifying post authorship, and processing content through LLM prompts, the system objectively assigns and updates community tiers on-chain. 

**Recent Upgrades:** This contract now features strict ownership checks, admin recovery controls, and comprehensive event emission for total security and auditability.

---

## 🏆 On-Chain Role Assignment

The contract distinguishes between different levels of engagement, deterministically assigning roles based on accumulated historical contributions:

*   **CONTENT_CREATOR:** A basic entry-level role. Users qualify for this tier by publishing **7 or more organic posts**.
*   **OG:** A prestigious, top-tier role that requires sustained, high-quality contributions. This requires accumulating at least **21 unique analytical posts** (deep technical breakdowns, architecture reviews, etc.).
*   **NONE:** Assigned if the contribution thresholds are not yet met, or if posts fail the originality/depth criteria.
*   **UNASSESSED:** The default state for newly registered contributors.

> **Note:** Because LLMs evaluate batches of up to 25 posts at a time, the contract intelligently accumulates validated post metrics across multiple evaluations. This ensures users can build their reputation over time.

---

## 🛡️ Key Security & Architecture Features

*   **Strict Access Control (Ownership Check):** Registration, deregistration, and evaluation can **only** be triggered by the owner of the wallet or the contract Administrator. This prevents malicious actors from hijacking evaluations or poisoning a user's post history.
*   **Administrator Controls:** The contract is initialized with an `admin` address capable of emergency interventions and contract upgrades.
*   **Authenticated Author Binding:** Fetches post metadata directly via API and strictly verifies that each evaluated post belongs to the target wallet address inside validator execution.
*   **Post Reuse Prevention (`used_posts`):** Tracks processed post IDs on-chain to completely eliminate double-claiming and prevent replay attacks.
*   **DeAI Soft Consensus:** Employs GenLayer's non-deterministic execution. The Leader node performs the initial LLM evaluation, while Validator nodes use a secondary AI prompt to independently verify the fairness and accuracy of the Leader's findings.
*   **Deterministic Storage & Auditing:** Stores SHA-256 digests of fetched evidence and LLM findings securely on-chain. Emits events (`WalletRegistered`, `ContractUpgraded`) for off-chain tracking.

---

## 🔌 Contract Interface (API)

### Setup & Admin Methods
*   `__init__(admin: str)`: Initializes the contract and sets the `administrator` address.
*   `upgrade(new_code: bytes)`: Allows the `administrator` to safely upgrade the contract's bytecode while preserving the storage state.

### Write Methods
*   `register_wallet(wallet_address: str)`: Registers a new EVM-compatible wallet address. **Note: This method can only be called from the same account specified in the `wallet_address` parameter (or by the administrator).**
*   `deregister_wallet(wallet_address: str)`: Removes a wallet from the registry. **Note: This method can only be called from the same account specified in the `wallet_address` parameter (or by the administrator).**
*   `evaluate_contributor(wallet_address: str, post_ids: list[u256])`: Triggers the DeAI consensus to fetch, evaluate, and score a batch of posts. **Note: This method can only be called from the same account specified in the `wallet_address` parameter (or by the administrator).**

### View Methods
*   `get_role_status(wallet_address: str) -> str`: Returns the current assigned role of the contributor.

---

## 🎮 How to Interact (Usage Guide)

To test and use this contract (e.g., via **GenLayer Studio**), follow this exact sequence to ensure transactions do not revert due to security checks:

### Step 1: Deployment
1. Click **Deploy new instance**.
2. Pass a valid EVM address into the `admin` parameter of the initialization prompt.
    * *Note: Admin address — 0x... (42 characters, starts with 0x).*

### Step 2: Register a Wallet
1. In GenLayer Studio, **switch your active sender account** to the wallet you want to register (e.g., `Account 1: 0xAAA...`).
2. Go to Write Methods and select `register_wallet`.
3. Enter your active wallet address (`0xAAA...`) into the `wallet` field.
    * *Important: `register_wallet` can only be called from the exact account specified in the parameter.*
4. Click **Send Transaction**. (If you use a different address, it will revert with `UNAUTHORIZED_WALLET_REGISTRATION`).

### Step 3: Evaluate Contributions
1. **Remain on the same active sender account** (`0xAAA...`).
2. Select the `evaluate_contributor` method.
3. Enter your registered wallet address into the `wallet_address` field.
    * *Important: `evaluate_contributor` can only be called from the exact account specified in the parameter.*
4. Enter `post_ids` as an array (e.g., `[1, 2, 3]`). 
    * *Note: These IDs must exist in the Indexer API database, must not have been used before, and must belong to your wallet.*
5. Click **Send Transaction** to trigger the AI evaluation. Wait for the `ACCEPTED` status.

### Step 4: Check Status
1. Go to the Read State section.
2. Select `get_role_status`.
3. Enter your `wallet_address`.
4. Click **Call Contract** to reveal your newly assigned role!
    * *Example response: `CONTENT_CREATOR` or `OG`.*

---
*Powered by GenLayer DeAI Consensus*
