# Proof of Contribution - GenLayer Intelligent Contract

This repository contains a standalone Python-based GenLayer Intelligent Contract designed to automate and decentralize the evaluation of Web3 community contributions.

Instead of relying on manual moderation, this contract leverages GenLayer's DeAI consensus to analyze the analytical depth, originality, and consistency of a user's content. By fetching exact post records from an authoritative indexer, verifying post authorship, and processing content through deterministic LLM prompts, the system objectively assigns community tiers.

---

## On-Chain Role Assignment

The contract is configured to distinguish between different levels of engagement, specifically assigning roles based on strict criteria:

* **Content Creators**: A basic entry-level role. Users qualify for this tier by publishing 7 or 8 organic posts.
* **OG Role**: A prestigious, top-tier role that requires sustained, high-quality contributions and deep analytical work (at least 21 unique analytical posts). The DeAI consensus ensures that only users who consistently deliver exceptional value achieve this status.
* **None**: Assigned if the contribution thresholds are not met or if posts fail originality/depth criteria.

---

## Key Security & Architecture Features

* **Authenticated Author Binding**: Fetches authenticated post metadata and strictly verifies that each evaluated post belongs to the target wallet address inside validator execution.
* **Post Reuse Prevention**: Tracks processed posts on-chain (`used_posts`) to eliminate double-claiming and prevent replay attacks.
* **DeAI Consensus**: Leverages decentralized AI execution (`gl.vm.run_nondet_unsafe`) with non-deterministic prompt evaluation to validate text quality objectively across validator nodes.
* **Deterministic Storage**: Stores digests of verified evidence and evaluation findings securely on-chain.
* **Trustless Moderation**: Removes human bias and central points of failure from community reward systems and ambassador programs.

---

## Contract Workflow & Usage

The primary entry point of the contract is `evaluate_contributor(wallet_address, post_ids)`:

1. **Registry Verification**: Confirms that the target contributor is registered in `cases`.
2. **Batch & Uniqueness Checks**: Validates post ID counts, ensures IDs are positive and unique, and checks that none of the IDs have been processed in previous evaluations.
3. **DeAI Leader-Validator Execution**: 
   * Fetches content and verifies post authors via the indexer API.
   * Prompts the AI evaluator under strict output constraints.
   * Reaches validator consensus on findings and role assignment.
4. **State Commit**: Marks posts as used, logs post findings and revision digests, and updates the contributor's assigned role.
