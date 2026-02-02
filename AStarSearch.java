import java.util.*;   

class AStarSearch {

    static class Node implements Comparable<Node> {
        String name;
        int gCost;
        int hCost;
        Node parent;

        Node(String name, int gCost, int hCost, Node parent) {
            this.name = name;
            this.gCost = gCost;
            this.hCost = hCost;
            this.parent = parent;
        }

        int fCost() {
            return gCost + hCost;
        }

        @Override
        public int compareTo(Node other) {
            return Integer.compare(this.fCost(), other.fCost());
        }
    }

    static class Edge {
        String to;
        int cost;

        Edge(String to, int cost) {
            this.to = to;
            this.cost = cost;
        }
    }

    static Map<String, List<Edge>> graph = new HashMap<>();

    static void addEdge(String from, String to, int cost) {
        graph.putIfAbsent(from, new ArrayList<>());
        graph.get(from).add(new Edge(to, cost));
    }

    static void aStarSearch(String start, String goal,
                            Map<String, Integer> heuristic) {

        PriorityQueue<Node> open = new PriorityQueue<>();
        Set<String> closed = new HashSet<>();

        open.add(new Node(start, 0, heuristic.get(start), null));

        while (!open.isEmpty()) {
            Node current = open.poll();

            if (current.name.equals(goal)) {
                System.out.println("Path Found:");
                printPath(current);
                System.out.println("\nTotal Cost = " + current.gCost);
                return;
            }

            closed.add(current.name);

            for (Edge e : graph.getOrDefault(current.name, new ArrayList<>())) {

                if (closed.contains(e.to)) continue;

                int g = current.gCost + e.cost;
                int h = heuristic.getOrDefault(e.to, Integer.MAX_VALUE);

                Node child = new Node(e.to, g, h, current);
                open.add(child);
            }
        }

        System.out.println("No Path Found");
    }

    static void printPath(Node node) {
        if (node == null) return;
        printPath(node.parent);
        System.out.print(node.name + " ");
    }

    public static void main(String[] args) {

        // Game Graph
        addEdge("1", "2", 2);
        addEdge("1", "3", 11);
        addEdge("1", "4", 1);
        addEdge("2", "5", 3);
        addEdge("3", "2", 2);
        addEdge("3", "6", 1);
        addEdge("3", "7", 1);
        addEdge("4", "3", 12);
        addEdge("4", "6", 15);
        addEdge("5", "3", 5);
        addEdge("5", "7", 7);
        addEdge("6", "7", 1);

        // Heuristic values
        Map<String, Integer> heuristic = Map.of(
            "1", 8,
            "2", 7,
            "3", 0,
            "4", 11,
            "5", 5,
            "6", 11,
            "7", 0
        );

        aStarSearch("1", "7", heuristic);
    }
}
/* OUTPUT 
admin1@Your:~$ javac AStarSearch.java
admin1@Your:~$ java AStarSearch
Path Found:
1 2 5 3 7 
Total Cost = 11
admin1@Your:~$ 
*/
