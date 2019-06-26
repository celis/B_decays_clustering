#!/usr/bin/env python3

# std
from abc import abstractmethod

# ours
from clusterking.worker import AbstractWorker
from clusterking.result import AbstractResult
from clusterking.stability.fom import FOM


class StabilityTesterResult(AbstractResult):
    """ Result of a :class:`AbstractStabilityTester` """

    pass


class AbstractStabilityTester(AbstractWorker):
    """ Abstract baseclass to perform stability tests. This baseclass is
    a subclass of :class:`clusterking.worker.AbstractWorker` and thereby
    adheres to the Command design pattern: After initialization, several
    methods can be called to modify internal settings. Finally, the
    :meth:`run` method is called to perform the actual test.

    All current stability tests perform the task at hand (clustering,
    benchmarking, etc.) for multiple, slightly varied datasets or worker
    parameters (these runs are called 'experiments'). For each of these (for
    each experiment), figures of merit (FOMs) are calculated that compare the
    outcome with the original outcome (e.g. how many points still lie in the
    same cluster, or how far the benchmark points are diverging). These FOMs
    are then written out to a :class:`StabilityTesterResult` object,
    which provides methods for visualization and further analyses (e.g.
    histograms, etc.).
    """

    def __init__(self):
        super().__init__()
        self._foms = {}

    def add_fom(self, fom: FOM) -> None:
        """ Add a figure of merit (FOM).

        Args:
            fom: :class:`~clusterking.stability.fom.FOM` object

        Returns:
            None
        """
        if fom.name in self._foms:
            # todo: do with log
            print(
                "Warning: FOM with name {} already existed. Replacing.".format(
                    fom.name
                )
            )
        self._foms[fom.name] = fom

    @abstractmethod
    def run(self, *args, **kwargs) -> StabilityTesterResult:
        """ Run the stability test.

        Args:
            *args: Positional arguments
            **kwargs: Key word arguments

        Returns:
            :class:`~StabilityTesterResult`
            object
        """
        pass
