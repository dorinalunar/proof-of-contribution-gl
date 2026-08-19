import pytest

# Ensure this import matches your contract filename (e.g. from contract import ...)
from contract import (
    _is_valid_wallet,
    _validate_llm_output,
    _evaluation_key,
    _finding_key,
)

# Real addresses from deployment and test transactions
CREATOR_WALLET = "0x38409cCa5f5ca70F3fe189638a87862318b478dd"
CONTRACT_ADDRESS = "0xc5F020df146c0ef767fC836E461E98899967E8AD"
CONTRIBUTOR_WALLET = "0x6f6077eC587f2964d30aCE8D803Edc27988046e3"
ACTIVATOR_WALLET = "0x9D998aD7C7f9Cc448A4DbDf49edD7CADBe3d57B6"


def test_is_valid_wallet_with_real_addresses():
    # Verify all actual transaction wallets pass validation
    assert _is_valid_wallet(CREATOR_WALLET) is True
    assert _is_valid_wallet(CONTRACT_ADDRESS) is True
    assert _is_valid_wallet(CONTRIBUTOR_WALLET) is True
    assert _is_valid_wallet(ACTIVATOR_WALLET) is True

    # Negative tests: invalid formats and lengths
    assert _is_valid_wallet("0x38409cCa5f5ca70F3fe189638a87862318b478") is False
    assert _is_valid_wallet("0x38409cCa5f5ca70F3fe189638a87862318b478ZZ") is False
    assert _is_valid_wallet("") is False


def test_storage_keys_with_real_contributor():
    # Testing key formatting using real evaluated contributor address
    assert _evaluation_key(CONTRIBUTOR_WALLET, 1) == f"{CONTRIBUTOR_WALLET}:1"
    assert _finding_key(CONTRIBUTOR_WALLET, 1, 0) == f"{CONTRIBUTOR_WALLET}:1:0"


def test_validate_llm_output_real_post_evaluation():
    # Evaluation payload for evaluated post_id: 1
    expected_ids = [1]
    raw_llm_response = {
        "findings": [
            {
                "post_id": 1,
                "is_organic": True,
                "analytical_depth": True,
            }
        ]
    }
    
    result = _validate_llm_output(raw_llm_response, expected_ids)
    assert len(result["findings"]) == 1
    assert result["findings"][0]["post_id"] == 1
    assert result["findings"][0]["is_organic"] is True
    assert result["findings"][0]["analytical_depth"] is True


def test_validate_llm_output_mismatched_post_id():
    # Expecting evaluated post_id 1, but LLM returns an unexpected ID
    expected_ids = [1]
    mismatched_response = {
        "findings": [
            {
                "post_id": 999,
                "is_organic": True,
                "analytical_depth": True,
            }
        ]
    }
    
    with pytest.raises(Exception):
        _validate_llm_output(mismatched_response, expected_ids)
