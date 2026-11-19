# Cost and Latency Note

For 8 job posts, normal use is about 8 LLM requests per run. Because the program retries once after an invalid or failed response, the theoretical maximum is 16 attempts. If there is no API key, it uses offline fallback and makes no successful API calls.

Latency depends on provider, model, network and post length. Use 2–10 seconds per request only as a planning estimate; measure actual time in your own run. Successful API call elapsed time is measured in the program.

Estimated cost = (input tokens × current input-token price + output tokens × current output-token price) × request count. Check the provider's current pricing and actual token usage before entering a currency amount. Do not present a guessed fixed cost as fact. Offline-only run API cost is zero.
