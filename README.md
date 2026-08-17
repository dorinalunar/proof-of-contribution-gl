# 🧠 Proof of Contribution - GenLayer Intelligent Contract

This repository contains a standalone Python-based **GenLayer Intelligent Contract** designed to automate and decentralize the evaluation of Web3 community contributions.

Instead of relying on manual moderation, this contract leverages GenLayer's **DeAI consensus** to analyze the analytical depth and originality of a user's content. By fetching exact post records from an authoritative indexer, verifying post authorship, and processing content through LLM prompts, the system objectively assigns and updates community tiers on-chain.

## 🏆 On-Chain Role Assignment

The contract distinguishes between different levels of engagement, deterministically assigning roles based on accumulated historical contributions:

*   **`CONTENT_CREATOR`**: A basic entry-level role. Users qualify for this tier by publishing **7 or more** organic posts.
*   **`OG`**: A prestigious, top-tier role that requires sustained, high-quality contributions. This requires accumulating **at least 21** unique analytical posts (deep technical breakdowns, architecture reviews, etc.). 
*   **`NONE`**: Assigned if the contribution thresholds are not yet met, or if posts fail the originality/depth criteria.
*   **`UNASSESSED`**: The default state for newly registered contributors.

> **Note:** Because LLMs evaluate batches of up to 25 posts at a time, the contract intelligently *accumulates* validated post metrics across multiple evaluations. This ensures users can build their reputation over time.

## 🛡️ Key Security & Architecture Features

*   **Authenticated Author Binding**: Fetches post metadata directly via API and strictly verifies that each evaluated post belongs to the target wallet address inside validator execution.
*   **Post Reuse Prevention (`used_posts`)**: Tracks processed post IDs on-chain to completely eliminate double-claiming and prevent replay attacks.
*   **DeAI Soft Consensus**: Employs GenLayer's non-deterministic execution (`gl.vm.run_nondet_unsafe`). The Leader node performs the initial LLM evaluation, while Validator nodes use a secondary AI prompt to independently verify the fairness and accuracy of the Leader's findings, preventing consensus failures while maintaining strict moderation.
*   **Deterministic Storage & Auditing**: Stores SHA-256 digests of fetched evidence and LLM findings securely on-chain for total transparency.
*   **Trustless Moderation**: Removes human bias and central points of failure from community reward systems and ambassador programs.

## ⚙️ Contract Workflow

1.  **Registry Verification**: Confirms that the target contributor is registered in the contract state.
2.  **Batch & Uniqueness Checks**: Validates post ID counts (max 25 per batch), ensures IDs are positive and unique, and checks that none have been processed before.
3.  **DeAI Execution (Leader)**: Fetches content via the Indexer API and prompts the AI evaluator to assess each post for organic writing and analytical depth.
4.  **DeAI Validation (Validators)**: Validators fetch the same data, verify the data hash, and use AI to validate the Leader's proposed assessment.
5.  **State Commit**: Marks posts as used, logs the findings, updates the contributor's lifetime metrics, and calculates the new assigned role.

## 🔌 Contract Interface (API)

### Write Methods
*   `register_contributor(wallet_address: str)`: Registers a new EVM-compatible wallet address to start tracking contributions.
*   `evaluate_contributor(wallet_address: str, post_ids: list[u256])`: Triggers the DeAI consensus to fetch, evaluate, and score a batch of posts. Updates the user's role if thresholds are met.
*   `upgrade(new_code: bytes)`: (Admin only) Upgrades the contract's bytecode while preserving the storage state.

### View Methods
*   `get_role_status(wallet_address: str) -> str`: Returns the current assigned role of the contributor (`OG`, `CONTENT_CREATOR`, `NONE`, or `UNASSESSED`).

## 🛠️ Dependencies
*   Designed for the **GenLayer** network.
*   Requires `py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6`.

## 🚀 How to Deploy

1. **Local Setup:** Install the required GenLayer package for your local environment:
   ```bash
   pip install py-genlayer
