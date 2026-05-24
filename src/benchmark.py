from __future__ import annotations

from collections import deque
from statistics import median
from timeit import Timer
from typing import Callable


# =========================
# CHANGE THIS IMPORT
# =========================
from my_ds_lib import Deque as MyDeque


SIZES = [100, 1_000, 10_000, 100_000]
REPEAT = 7
BULK_SIZE = 100


# =========================
# Benchmark core
# =========================
def bench(fn: Callable[[], None], repeat_count: int = REPEAT) -> tuple[int, float, float]:
    timer = Timer(fn)
    loops, _ = timer.autorange()
    samples = timer.repeat(repeat=repeat_count, number=loops)
    per_loop = [sample / loops for sample in samples]
    return loops, min(per_loop), median(per_loop)


def print_header(title: str) -> None:
    print(f"\n=== {title} ===")
    print(f"{'N':>10} | {'structure':>12} | {'loops':>10} | {'best/op (s)':>14} | {'median/op (s)':>16}")
    print("-" * 74)


def print_row(n: int, structure: str, loops: int, best: float, med: float) -> None:
    print(f"{n:>10} | {structure:>12} | {loops:>10} | {best:>14.9f} | {med:>16.9f}")


# =========================
# Builders
# =========================
def build_list(n: int) -> list[int]:
    return list(range(n))


def build_deque(n: int) -> deque[int]:
    return deque(range(n))


def build_mydeque(n: int) -> MyDeque:
    d = MyDeque()
    d.extend(range(n))
    return d


# =========================
# Operation factories
# Every benchmarked callable:
# 1) mutates the structure
# 2) rolls it back
# So each iteration starts from same state
# =========================

# ---- append ----
def make_list_append(n: int) -> Callable[[], None]:
    data = build_list(n)

    def run() -> None:
        data.append(-1)
        data.pop()

    return run


def make_deque_append(n: int) -> Callable[[], None]:
    data = build_deque(n)

    def run() -> None:
        data.append(-1)
        data.pop()

    return run


def make_mydeque_append(n: int) -> Callable[[], None]:
    data = build_mydeque(n)

    def run() -> None:
        data.append(-1)
        data.pop()

    return run


# ---- appendleft ----
def make_list_appendleft(n: int) -> Callable[[], None]:
    data = build_list(n)

    def run() -> None:
        data.insert(0, -1)
        data.pop(0)

    return run


def make_deque_appendleft(n: int) -> Callable[[], None]:
    data = build_deque(n)

    def run() -> None:
        data.appendleft(-1)
        data.popleft()

    return run


def make_mydeque_appendleft(n: int) -> Callable[[], None]:
    data = build_mydeque(n)

    def run() -> None:
        data.appendleft(-1)
        data.popleft()

    return run


# ---- pop ----
def make_list_pop(n: int) -> Callable[[], None]:
    data = build_list(n)

    def run() -> None:
        value = data.pop()
        data.append(value)

    return run


def make_deque_pop(n: int) -> Callable[[], None]:
    data = build_deque(n)

    def run() -> None:
        value = data.pop()
        data.append(value)

    return run


def make_mydeque_pop(n: int) -> Callable[[], None]:
    data = build_mydeque(n)

    def run() -> None:
        value = data.pop()
        data.append(value)

    return run


# ---- popleft ----
def make_list_popleft(n: int) -> Callable[[], None]:
    data = build_list(n)

    def run() -> None:
        value = data.pop(0)
        data.insert(0, value)

    return run


def make_deque_popleft(n: int) -> Callable[[], None]:
    data = build_deque(n)

    def run() -> None:
        value = data.popleft()
        data.appendleft(value)

    return run


def make_mydeque_popleft(n: int) -> Callable[[], None]:
    data = build_mydeque(n)

    def run() -> None:
        value = data.popleft()
        data.appendleft(value)

    return run


# ---- extend ----
def make_list_extend(n: int, k: int = BULK_SIZE) -> Callable[[], None]:
    data = build_list(n)
    items = list(range(k))

    def run() -> None:
        data.extend(items)
        del data[-k:]

    return run


def make_deque_extend(n: int, k: int = BULK_SIZE) -> Callable[[], None]:
    data = build_deque(n)
    items = list(range(k))

    def run() -> None:
        data.extend(items)
        for _ in range(k):
            data.pop()

    return run


def make_mydeque_extend(n: int, k: int = BULK_SIZE) -> Callable[[], None]:
    data = build_mydeque(n)
    items = list(range(k))

    def run() -> None:
        data.extend(items)
        for _ in range(k):
            data.pop()

    return run


# ---- extendleft ----
# For list we emulate deque.extendleft semantics:
# for x in items: insert(0, x)
def make_list_extendleft(n: int, k: int = BULK_SIZE) -> Callable[[], None]:
    data = build_list(n)
    items = list(range(k))

    def run() -> None:
        for x in items:
            data.insert(0, x)
        del data[:k]

    return run


def make_deque_extendleft(n: int, k: int = BULK_SIZE) -> Callable[[], None]:
    data = build_deque(n)
    items = list(range(k))

    def run() -> None:
        data.extendleft(items)
        for _ in range(k):
            data.popleft()

    return run


def make_mydeque_extendleft(n: int, k: int = BULK_SIZE) -> Callable[[], None]:
    data = build_mydeque(n)
    items = list(range(k))

    def run() -> None:
        data.extendleft(items)
        for _ in range(k):
            data.popleft()

    return run


# =========================
# Runner
# =========================
def run_case(
    title: str,
    list_factory: Callable[[int], Callable[[], None]],
    deque_factory: Callable[[int], Callable[[], None]],
    my_factory: Callable[[int], Callable[[], None]],
) -> None:
    print_header(title)

    for n in SIZES:
        for name, factory in (
            ("list", list_factory),
            ("deque", deque_factory),
            ("my_deque", my_factory),
        ):
            fn = factory(n)
            loops, best, med = bench(fn)
            print_row(n, name, loops, best, med)


def main() -> None:
    run_case("append", make_list_append, make_deque_append, make_mydeque_append)
    run_case("appendleft", make_list_appendleft, make_deque_appendleft, make_mydeque_appendleft)
    run_case("pop", make_list_pop, make_deque_pop, make_mydeque_pop)
    run_case("popleft", make_list_popleft, make_deque_popleft, make_mydeque_popleft)
    run_case("extend", make_list_extend, make_deque_extend, make_mydeque_extend)
    run_case("extendleft", make_list_extendleft, make_deque_extendleft, make_mydeque_extendleft)


if __name__ == "__main__":
    main()