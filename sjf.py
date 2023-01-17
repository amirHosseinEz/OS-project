from input_output import read_input
from base import Base


class SJF(Base):
    def __init__(self, processes):
        super(SJF, self).__init__(processes, title="SJF")

    def select(self, processes):
        return min(processes, key=self.cpu_burst_proc)


SJF(read_input('input.csv')).show()
