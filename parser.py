class TrafficParser:
    @staticmethod
    def unique_nodes_in_the_network():
        """Выводит сколько уникальных узлов в наблюдаемой сети"""
        unique_nodes = set()
        with open("traf.txt", "r") as traffic_dump:
            for line in traffic_dump:
                fields = line.strip().split(";")

            source_ip_port, source_mac, dest_ip_port, dest_mac, is_udp, data_size, time = fields[:7]

            unique_nodes.add(source_ip_port)
            unique_nodes.add(dest_ip_port)

        print(f"Количество уникальных узлов в наблюдаемой сети: {len(unique_nodes)}")

TrafficParser.unique_nodes_in_the_network()
