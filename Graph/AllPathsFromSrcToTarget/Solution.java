package Medium.AllPathsFromSrcToTarget;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * Solution
 */
public class Solution {

    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        List<List<Integer>> paths = new ArrayList<>();      // result paths
        Queue<List<Integer>> queue = new LinkedList<>();    // path queue
        List<Integer> path = new ArrayList<>();             // path in queue
        // queue should have [[0]] in the beginning
        path.add(0);
        queue.add(path);
        while (!queue.isEmpty()) {
            // take one of paths so far
            List<Integer> currentPath = queue.poll();
            int currentNode = currentPath.get(currentPath.size()-1);
            if (currentNode == graph.length-1) {
                // if current node is destinatin, then stop and add path to resulting paths
                paths.add(currentPath);
            } else {
                // for each neighboring nodes, append it and construct new path (extend the path) and add to queue
                for (int next: graph[currentNode]) {
                    List<Integer> tempPath = new ArrayList<>(currentPath);
                    tempPath.add(next);
                    queue.add(tempPath);
                }
            }
        }
        return paths;
    }
    
}