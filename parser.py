class TrafficParser():
    def __init__(self):
        self.total_data_size = 0
        self.total_time = 0
        self.unique_nodes = set()
        self.average_udp_speed = 0
        self.average_tcp_speed = 0

        with open("traf.txt", "r") as traffic_dump:
            for line in traffic_dump:
                fields = line.strip().split(";")
                is_udp = fields[4]
                data_size = int(fields[5])
                time = float(fields[6])

            if is_udp == 'true':
                self.average_udp_speed += data_size / time
            else:
                self.average_tcp_speed += data_size / time

            source_ip_port, dest_ip_port = fields[0], fields[2]
            self.unique_nodes.add(source_ip_port)
            self.unique_nodes.add(dest_ip_port)

            self.total_data_size += data_size
            self.total_time += time

    def unique_nodes_in_the_network(self):
        """Выводит сколько уникальных узлов в наблюдаемой сети (штук)"""

        return f"Количество уникальных узлов в наблюдаемой сети: {len(self.unique_nodes)}"

    def average_data_rate(self):
        """Выводит среднюю скорость передачи данных все наблюдаемой сети (байт/сек)"""
        average_data_rate = self.total_data_size / self.total_time

        return f"Средняя скорость передачи данных всей наблюдаемой сети: {average_data_rate} байт/сек"

    def compare_udp_tcp_speed(self):
        """Проверяет верно-ли утверждение,
        что 'UDP используется для передачи данных с максимальной пиковой скоростью'"""
        if self.average_udp_speed > self.average_tcp_speed:
            return "Да, UDP используется для передачи данных с максимальной пиковой скоростью."
        else:
            return "Нет, UDP не используется для передачи данных с максимальной пиковой скоростью."


parser = TrafficParser()
unique_nodes_result = parser.unique_nodes_in_the_network()
average_data_rate = parser.average_data_rate()
udp_tcp_speed = parser.compare_udp_tcp_speed()

print(f"_______________________________________________________________________________________\n{unique_nodes_result}")
print(f"_______________________________________________________________________________________\n{average_data_rate}")
print(f"_______________________________________________________________________________________\n{udp_tcp_speed}")