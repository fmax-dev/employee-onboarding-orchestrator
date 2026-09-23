import asyncio
import random


# Step 1
class TransientError(Exception):
    """Raised when a temporary failure occurs."""


async def flaky_call(attempt: int):
    if attempt < 3:
        raise TransientError(f"Transient failure on attempt{attempt}")
    return "ok"


# Step 2 & 3
async def with_retry(fn, *, max_attempts=4, base_delay=0.5, factor=2.0):
    for attempt in range(1, max_attempts + 1):
        try:
            result = await fn(attempt)
            print(f"attempt {attempt}: success -> {result}")
            return result
        except TransientError as exc:
            if attempt == max_attempts:
                raise

            delay = base_delay * (factor ** (attempt - 1))
            jitter = random.uniform(0, delay)

            print(
                f"attempt {attempt}: {exc}."
                f"backoff ceiling={delay:.2f}s,"
                f"sleeping for={jitter:.2f}s"
            )
            await asyncio.sleep(jitter)


# Step 4
# Why exponential backoff with jitter beats a fixed 1-second retry
# when 50 workers all hit a rate limit at once:
# a fixed retry makes everyone hit the same moment again, causing a thundering
# herd and amplifying the rate-limit spike. Exponential backoff spreads retries
# out over time, and jitter adds randomness so workers do not synchronize and
# slam the same endpoint together.


async def main():
    result = await with_retry(flaky_call)
    print(f"final result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
