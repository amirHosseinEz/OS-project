from input_output import read_input
from base import Base


class RoundRobin(Base):
    def __init__(self, processes, time_quantum):
        super(RoundRobin, self).__init__(processes, "RoundRobin")
        self.q = time_quantum

    def select(self, processes):
        return min(processes, key=lambda a: a["arrival_time"])

    def get_cpu_burst(self, process):
        return self.q


RoundRobin(read_input('input.csv'), int(input())).show()
