# Proof of Contribution - GenLayer Intelligent Contract

This repository contains a standalone Python-based GenLayer Intelligent Contract designed to automate and decentralize the evaluation of Web3 community contributions. 

Instead of relying on manual moderation, this contract leverages GenLayer's DeAI consensus to analyze the analytical depth, originality, and consistency of a user's content. By fetching exact post records and processing them through deterministic LLM prompts, the system objectively assigns community tiers.

## On-Chain Role Assignment

The contract is configured to distinguish between different levels of engagement, specifically assigning roles based on strict criteria:

*   **Content Creators:** A basic entry-level role. Users can qualify for this tier by publishing just seven or eight organic posts.
*   **OG Role:** A prestigious, top-tier role that is difficult to earn. It requires sustained, high-quality contributions and deep analytical work over a significant period. The DeAI consensus ensures that only users who consistently deliver exceptional value achieve this status.

## Key Features

*   **DeAI Consensus:** Uses decentralized AI to evaluate text and context objectively.
*   **Automated Evaluation:** The `evaluate_contributor` function checks wallet addresses against submitted post IDs, preventing duplicate or invalid claims.
*   **Python Smart Contract:** Built with Python for GenLayer's execution environment, allowing for complex logic and easy integration of AI evaluation models.
*   **Trustless Moderation:** Removes human bias from community reward systems and ambassador programs.

## Usage

The primary function of the contract is `evaluate_contributor(wallet_address, post_ids)`. When called, the contract:
1. Verifies the user's registry status.
2. Validates the batch of submitted post IDs.
3. Triggers the DeAI consensus to evaluate the quality and quantity of the submissions against the role thresholds.
