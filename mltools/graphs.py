from statistics import mean, stdev


class Graphlist:
    def __init__(self, graphs=None):
        self._graphs = graphs or []
        self._num_nodes = []
        self._num_edges = []

        for G in self._graphs:
            num_nodes = G.number_of_nodes()
            num_edges = G.number_of_edges()
            self._num_nodes.append(num_nodes)
            self._num_edges.append(num_edges)

    def __iter__(self):
        return iter(self._graphs)

    def __len__(self):
        return len(self._graphs)

    def __getitem__(self, index):
        return self._graphs[index]

    def __setitem__(self, index, G):
        self._graphs[index] = G
        self._num_nodes[index] = G.number_of_nodes()
        self._num_edges[index] = G.number_of_edges()

    def __contains__(self, graph):
        return graph in self._graphs

    def avg_num_nodes(self):
        return mean(self._num_nodes)

    def std_num_nodes(self):
        return stdev(self._num_nodes)

    def min_num_nodes(self):
        return min(self._num_nodes)

    def max_num_nodes(self):
        return max(self._num_nodes)

    def avg_num_edges(self):
        return mean(self._num_edges)

    def std_num_edges(self):
        return stdev(self._num_edges)

    def min_num_edges(self):
        return min(self._num_edges)

    def max_num_edges(self):
        return max(self._num_edges)

    def filter(self, fn):
        graphs = [G for G in self if fn(G)]
        return Graphlist(graphs)

    def iternodes(self, data=False):
        for G in self._graphs:
            yield G.nodes(data=data)

    def iteredges(self, data=False):
        for G in self._graphs:
            yield G.edges(data=data)

    def append(self, G):
        self._graphs.append(G)
        self._num_nodes.append(G.number_of_nodes())
        self._num_edges.append(G.number_of_edges())

    def remove(self, G):
        index = self._graphs.index(G)
        self._graphs.pop(index)
        self._num_nodes.pop(index)
        self._num_edges.pop(index)

    def __repr__(self):
        return f"Graphlist[{len(self)}]" \
            f"(Vmax={self.max_num_nodes()}, " \
            f"Vmin={self.min_num_nodes()}, " \
            f"Emax={self.max_num_edges()}, " \
            f"Emin={self.min_num_edges()})"
