from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from graphix.clifford import Clifford
from graphix.sim.statevec import Statevec
from graphix.states import BasicStates

if TYPE_CHECKING:
    from pytest_benchmark import BenchmarkFixture


nqubits = range(1, 12)
nqubit = 20

class BenchTest:
    @pytest.mark.benchmark(max_time=1)
    def bench_evolve_single(
        self, benchmark: BenchmarkFixture) -> None:
        sv = Statevec(nqubit=nqubit, data=BasicStates.ZERO)
        op = Clifford.H.matrix
        def run():
            evol = sv.evolve_single
            for q in range(nqubit):
                evol(op, q)
        benchmark(run)
