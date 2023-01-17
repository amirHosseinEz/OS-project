from input_output import *


class Base:
    def __init__(self, processes, title="RoundRobin"):
        self.procs = {}
        for p in processes:
            self.procs[p["process_id"]] = get_instance(p["process_id"], start=-1, waiting_time=0, turn_around_time=0)
            self.procs[p["process_id"]].update(**p)
            self.procs[p["process_id"]]["is_ended"] = False
            self.procs[p["process_id"]]["a_b"] = self.procs[p["process_id"]]["arrival_time"]
        self.t = 0
        self.q = 1
        self.idle = 0
        self.title = title

    def select(self, processes):
        return processes[0]

    def run(self):
        p_old = None
        s = 0
        while True:
            ps = [i for i in self.procs.values() if not i["is_ended"] and i["arrival_time"] <= self.t]
            if ps:
                p = self.select(ps)
            else:
                ps = [i for i in self.procs.values() if not i["is_ended"]]
                if ps:
                    p = min(ps, key=lambda a: a["arrival_time"])
                else:
                    break
            if p_old is not None and p_old != p:
                pass
                # print(f'P{p_old["process_id"]}: {s} -> {self.t}, queue: {p_old["queue"]}')
            if self.t < p["arrival_time"]:
                self.idle += p["arrival_time"] - self.t
                self.t = p["arrival_time"]
            else:
                p["waiting_time"] += self.t - p["arrival_time"]
            # if p_old is None or p_old != p:
            s = self.t
            self.q = self.get_cpu_burst(p)
            if self.q > p["cpu_time1"]:
                exe = p["cpu_time1"]
            else:
                exe = self.q
            if p["start"] == -1:
                p["start"] = self.t
                p["response_time"] = p["start"] - p["arrival_time"]
            if p["cpu_time1"]:
                self.t += exe
                p["cpu_time1"] -= exe
                if p["cpu_time1"]:
                    p["arrival_time"] = self.t
                    self.on_cpu(p)
                else:
                    p["arrival_time"] = self.t + p["io_time"]
                    self.on_io(p)
                    if not p["cpu_time2"]:
                        p["end"] = self.t
                        p["turn_around_time"] = p["end"] - p["a_b"]
                        p["is_ended"] = True
            else:
                if self.q > p["cpu_time2"]:
                    exe = p["cpu_time2"]
                else:
                    exe = self.q
                self.t += exe
                p["cpu_time2"] -= exe
                if p["cpu_time2"]:
                    p["arrival_time"] = self.t
                    self.on_cpu(p)
                else:
                    p["end"] = self.t
                    p["turn_around_time"] = p["end"] - p["a_b"]
                    p["is_ended"] = True
            p_old = p
            print(f'P{p_old["process_id"]}: {s} -> {self.t}')

    def show(self):
        self.run()
        print_output(self.title, self.procs.values(), total_time=self.t, idle_time=self.idle)

    def on_io(self, process):
        pass

    def on_cpu(self, process):
        pass

    def get_cpu_burst(self, process):
        return self.cpu_burst_proc(process)

    def cpu_burst_proc(self, process):
        if process["cpu_time1"]:
            return process["cpu_time1"]
        else:
            return process["cpu_time2"]
