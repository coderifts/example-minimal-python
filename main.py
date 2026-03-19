"""Minimal CodeRifts enforcement demo — Python."""
import requests

CODERIFTS_URL = "https://app.coderifts.com/api/v1/public/preflight"


def check_api_safety(spec_url: str) -> dict:
    """Call CodeRifts public preflight to check if an API spec is safe."""
    response = requests.get(f"{CODERIFTS_URL}?url={spec_url}")
    return response.json()


def execute_workflow(spec_url: str):
    """Run a workflow that aborts if CodeRifts returns BLOCK."""
    decision = check_api_safety(spec_url)

    print(f"[CODERIFTS] decision: {decision['decision']}")
    print(f"[CODERIFTS] risk_score: {decision.get('risk_score', 'N/A')}")
    print(f"[CODERIFTS] safe_for_agent: {decision.get('safe_for_agent', 'N/A')}")

    if decision["decision"] == "BLOCK":
        print("[EXECUTION] ABORTED — CodeRifts blocked unsafe execution")
        return

    if decision["decision"] == "PENDING":
        print("[EXECUTION] PENDING — retry in 5 seconds")
        import time
        time.sleep(5)
        return execute_workflow(spec_url)

    print("[EXECUTION] Proceeding with API call...")


if __name__ == "__main__":
    execute_workflow("https://petstore3.swagger.io/api/v3/openapi.json")
