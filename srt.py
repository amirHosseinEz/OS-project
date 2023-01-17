from input_output import read_input
from base import Base


class SRT(Base):
    def __init__(self, processes):
        super(SRT, self).__init__(processes, title="SRT")

    def select(self, processes):
        return min(processes, key=self.cpu_burst_proc)


SRT(read_input('input.csv')).show()
