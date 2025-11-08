"""
Balanced Frame–Stewart data generator that enforces Equation (3) from the paper.
"""
from functools import lru_cache


def T3(n: int) -> int:
    """Optimal three-peg move count."""
    if n < 0:
        raise ValueError("T3 is defined for non-negative integers.")
    return (1 << n) - 1


@lru_cache(None)
def T4(n: int) -> int:
    """Optimal four-peg move count via the Frame–Stewart recurrence."""
    if n <= 1:
        return n
    best = float("inf")
    for split in range(1, n):
        cost = 2 * T4(n - split) + T3(split)
        if cost < best:
            best = cost
    return int(best)


def balanced_table(max_n: int = 30):
    """Return rows of (n, k, T4(n), FS_{floor(n/2)}(n), rho(n))."""
    rows = []
    for n in range(1, max_n + 1):
        k = n // 2
        fs = 2 * T4(k) + T3(n - k)
        opt = T4(n)
        rows.append((n, k, opt, fs, fs / opt))
    return rows


if __name__ == "__main__":
    header = " n  k  T4(n)  FS_bal  rho"
    print(header)
    print("-" * len(header))
    for n, k, opt, fs, ratio in balanced_table(20):
        print(f"{n:2d}  {k:2d}  {opt:5d}  {fs:6d}  {ratio:6.3f}")

