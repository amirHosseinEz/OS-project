from input_output import read_input
from base import Base


class FCFS(Base):
    def __init__(self, processes):
        super(FCFS, self).__init__(processes, title="FCFS")

    def select(self, processes):
        return min(processes, key=lambda a: a["arrival_time"])


FCFS(read_input('input.csv')).show()
