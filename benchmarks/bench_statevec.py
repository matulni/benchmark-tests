from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from graphix.clifford import Clifford
from graphix.sim.statevec import Statevec
from graphix.states import BasicStates

if TYPE_CHECKING:
    from pytest_benchmark import BenchmarkFixture


nqubits = (2, 3)

class BenchTest:
    #@pytest.mark.skip(reason="debug")
    @pytest.mark.parametrize("q", range(max(nqubits)))
    @pytest.mark.parametrize("nqubit", nqubits)
    @pytest.mark.benchmark(group="exp_single", max_time=1, min_rounds=3, warmup=True)
    def bench_expectation(self, benchmark: BenchmarkFixture, nqubit: int, q: int) -> None:
        if q < nqubit:
            sv = Statevec(nqubit=nqubit, data=BasicStates.ZERO)
            op = Clifford.H.matrix

            def run():
                return sv.expectation_single(op, q)

            benchmark(run)