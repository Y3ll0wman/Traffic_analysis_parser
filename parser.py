class TrafficParser():
    def __init__(self):
        self.total_data_size = 0
        self.total_time = 0
        self.unique_nodes = set()
        self.average_udp_speed = 0
        self.average_tcp_speed = 0
        self.node_speeds = {} # Словарь для хранения скоростей передачи данных для каждого узла

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

            # Обновляем скорость передачи данных для каждого узла в словаре
            if source_ip_port in self.node_speeds:
                self.node_speeds[source_ip_port] += data_size / time
            else:
                self.node_speeds[source_ip_port] = data_size / time

            if dest_ip_port in self.node_speeds:
                self.node_speeds[dest_ip_port] += data_size / time
            else:
                self.node_speeds[dest_ip_port] = data_size / time

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

    def top_10_nodes_by_speed(self):
        """Возвращает 10 узлов с самой высокой средней скоростью передачи данных (байт/сек)"""
        sorted_nodes = sorted(self.node_speeds.items(), key=lambda x: x[1], reverse=True)
        top_10 = sorted_nodes[:10]
        return top_10


parser = TrafficParser()
unique_nodes_result = parser.unique_nodes_in_the_network()
average_data_rate = parser.average_data_rate()
udp_tcp_speed = parser.compare_udp_tcp_speed()
top_10_nodes = parser.top_10_nodes_by_speed()

print(f"_______________________________________________________________________________________\nQ1: {unique_nodes_result}")
print(f"_______________________________________________________________________________________\nQ2: {average_data_rate}")
print(f"_______________________________________________________________________________________\nQ3: {udp_tcp_speed}")
print(f"_______________________________________________________________________________________\nQ4: Топ 10 узлов по скорости передачи данных: {top_10_nodes}")
