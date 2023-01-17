from input_output import read_input
from base import Base


class MLFQ(Base):
    def __init__(self, processes):
        for p in processes:
            p["queue"] = 0
        super(MLFQ, self).__init__(processes, title="MLFQ")

    def select(self, processes):
        return min(processes, key=lambda a: a['queue'] * 1000000 + a["arrival_time"])

    def on_cpu(self, process):
        process['queue'] += 1

    def on_io(self, process):
        process['queue'] = 0

    def get_cpu_burst(self, process):
        if process['queue'] == 0:
            return 4
        elif process['queue'] == 1:
            return 16
        else:
            return self.cpu_burst_proc(process)


MLFQ(read_input('input.csv')).show()
