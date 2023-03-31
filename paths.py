class Path:
    def __init__(self, node, previous_path, start_node, to_node):
        self.node = node
        self.previous_path = previous_path
        self.start_node = start_node
        self.to_node = to_node

        self.distance_from_start = 0 
        self.distance_to_goal = 0
        self.total_distance = 0