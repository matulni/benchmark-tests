from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from graphix.clifford import Clifford
from graphix.sim.statevec import Statevec
from graphix.states import BasicStates

if TYPE_CHECKING:
    from pytest_benchmark import BenchmarkFixture


nqubits = range(1, 12)


class BenchTest:
    # @pytest.mark.skip(reason="debug")
    @pytest.mark.parametrize("nqubit, q", [(n, q) for n in nqubits for q in range(n)])
    @pytest.mark.benchmark(max_time=1)
    def bench_expectation_single(
        self, benchmark: BenchmarkFixture, nqubit: int, q: int
    ) -> None:
        sv = Statevec(nqubit=nqubit, data=BasicStates.ZERO)
        op = Clifford.H.matrix
        benchmark(lambda: sv.expectation_single(op, q))

    @pytest.mark.parametrize("nqubit, q", [(n, q) for n in nqubits for q in range(n)])
    @pytest.mark.benchmark(max_time=1)
    def bench_evolve_single(
        self, benchmark: BenchmarkFixture, nqubit: int, q: int
    ) -> None:
        sv = Statevec(nqubit=nqubit, data=BasicStates.ZERO)
        op = Clifford.H.matrix
        benchmark(lambda: sv.evolve_single(op, q))
