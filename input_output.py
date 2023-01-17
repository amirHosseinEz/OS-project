import csv


def read_input(input_file):
    processes = []
    with open(input_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                processes.append({"process_id": int(row[0]),
                                  "arrival_time": int(row[1]),
                                  "cpu_time1": int(row[2]),
                                  "io_time": int(row[3]),
                                  "cpu_time2": int(row[4])}
                                 )
            line_count += 1
    return processes


def tab(s, n=19, d='c'):
    if s is not str:
        if type(s) is float:
            s = "{:.2f}".format(s)
        else:
            s = str(s)
    l = len(s)
    if d == 'l':
        return s + " " * (n - l)
    elif d == 'c':
        return (n - l - (n - l) // 2) * " " + s + ((n - l) // 2) * " "
    elif d == 'r':
        return " " * (n - l) + s


def print_output(title, processes, total_time=0, idle_time=0):
    print()
    t = ("+" + "=" * 19) * 5 + '+'
    t2 = ("+" + "-" * 19) * 5 + '+'
    l = len(t)
    print(t)
    print(f'''|{tab(title, l - 2, "c")}|''')
    print(t)
    print(
        f'''|{tab("Process ID")}|{tab("Start-End")}|{tab("Turn Around Time")}|{tab("Response Time")}|{tab("Waiting Time")}|''')
    print(t2)

    for p in processes:
        print(
            f'''|{tab("P" + tab(p["process_id"], 0))}|{tab(tab(p["start"], 3, 'l') + '-' + tab(p["end"], 3, 'r'))}|{tab(p["turn_around_time"])}|{tab(p["response_time"])}|{tab(p["waiting_time"])}|''')

        print(t2)

    print(f'''|{tab("Average",39)}|{tab(sum([p["turn_around_time"] for p in processes]) / len(processes)):}|{tab(sum([p["response_time"] for p in processes]) / len(processes))}|{tab(sum([p["waiting_time"] for p in processes]) / len(processes))}|''')
    print(t2[:20] + '-' + t2[21:])
    print()
    print(f'Total Time: {total_time}')
    print(f'Idle Time: {idle_time}')
    print(f'CPU Utilization: {((total_time - idle_time) / total_time):.2f}')
    print(f'Throughput: {(len(processes)/ total_time):.2f}')


def get_instance(pid="", start="", end="", turn_around_time="", response_time="", waiting_time=""):
    return {"process_id": pid,
            "start": start,
            "end": end,
            "turn_around_time": turn_around_time,
            "response_time": response_time,
            "waiting_time": waiting_time
            }