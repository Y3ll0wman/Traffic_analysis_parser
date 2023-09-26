class TrafficParser():
    def __init__(self):
        self.total_data_size = 0
        self.total_time = 0
        self.unique_nodes = set()

        with open("traf.txt", "r") as traffic_dump:
            for line in traffic_dump:
                self.fields = line.strip().split(";")
                data_size = int(self.fields[5])
                time = float(self.fields[6])
                self.total_data_size += data_size
                self.total_time += time

        source_ip_port, dest_ip_port = self.fields[0], self.fields[2]
        self.unique_nodes.add(source_ip_port)
        self.unique_nodes.add(dest_ip_port)

    def unique_nodes_in_the_network(self):
        """Выводит сколько уникальных узлов в наблюдаемой сети (штук)"""

        return f"Количество уникальных узлов в наблюдаемой сети: {len(self.unique_nodes)}"

    def average_data_rate(self):
        """Выводит среднюю скорость передачи данных все наблюдаемой сети (байт/сек)"""
        average_data_rate = self.total_data_size / self.total_time

        return f"Средняя скорость передачи данных всей наблюдаемой сети: {average_data_rate} байт/сек"


parser = TrafficParser()
unique_nodes_result = parser.unique_nodes_in_the_network()
average_data_rate = parser.average_data_rate()

print(f"_______________________________________________________________________________________\n{unique_nodes_result}")
print(f"_______________________________________________________________________________________\n{average_data_rate}")
