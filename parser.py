class TrafficParser():
    def __init__(self):
        with open("traf.txt", "r") as traffic_dump:
            for line in traffic_dump:
                self.fields = line.strip().split(";")

    def unique_nodes_in_the_network(self):
        """Выводит сколько уникальных узлов в наблюдаемой сети"""
        unique_nodes = set()

        source_ip_port, source_mac, dest_ip_port, dest_mac, is_udp, data_size, time = self.fields[:7]

        unique_nodes.add(source_ip_port)
        unique_nodes.add(dest_ip_port)

        return f"Количество уникальных узлов в наблюдаемой сети: {len(unique_nodes)}"

    def average_data_rate(self):
        pass


parser = TrafficParser()
unique_nodes_result = parser.unique_nodes_in_the_network()
print(f"_______________________________________________________________________________________\n{unique_nodes_result}")
