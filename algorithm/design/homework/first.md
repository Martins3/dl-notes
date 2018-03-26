# Homework One
胡学仕
## Analyze
1. Tiling Problem
    1. 算法: 二分图最大匹配
    2. 复杂度: 假定 V 为定点的个数, E 为 边的个数, 对于 V / 2 的顶点进行遍历, 每一次遍历的
    对于最坏所有的边处理, 所以复杂度为O(V * E)
2. Interval scheduling problem 1
    1. 算法: 优先添加最先结束
    2. 复杂度: 排序 O(n * log(n)), 遍历为O(n), 所以总的复杂度为O(n * log(n))
3. Interval scheduling problem 2
    1. 算法: 首先按照结束的时间排序, 然后使用动态规划为: 前面 i 个权重之和为包括第 i 个权重
    之和 和 不包括第 i 个权重之和
    2. 复杂度: 排序 O(n * log(n)), 求解所有 interval 前面的最大的区间号需要 O(n * n)
    然后进行动态规划的遍历, 需要O(n), 所以总的时间为 O(n * n)

## 伪代码
1. Tiling Problem
```
去除二分图的一个子集S

对于 S 的每一个元素 a:
    如果dfs(a)结果为否, 结束返回, 否则继续
    
定义函数: dfs(a)
    对于a的所有未访问的邻居 n:
        标记n已经被访问
        如果n为匹配或者 n未被访问:
            n的匹配为 a
            返回是
    返回否
```

2. Interval scheduling problem 1
```
按照结束时间对于interval 排序
依次添加和之前的interval 没有冲突的interval, 直到结束
```

3. Interval scheduling problem 2
```
按照结束时间对于interval 排序
计算所有interval 前面的 最大index, 得到数组MAX
初始化数组 Value
对于第 i 个interval, 依次计算:
    设 w = i的权重
    Value[i] = max(value[i - 1], value(MAX[i]) + w)
    
初始化容器C
定义函数 find(j) 参数为interval的序号:
find(j):
    如果 j 是 0, 结束
    如果 value[i - 1] > value(p[i] + w)
        调用 find(i - 1)
    否则
        向C中间添加 j
        调用find(Max[j]))

```
## Code
```
package a;

import java.io.File;
import java.io.FileNotFoundException;
import java.net.URISyntaxException;
import java.net.URL;
import java.util.LinkedList;
import java.util.Scanner;
import java.util.Vector;

/**
 * Created by martin on 17-10-29.
 */
public class Chess {
    private Graph graph;
    private int[] match; // match chain
    private boolean[] visited;
    private LinkedList<Integer> oneSideNodes;

    private boolean inBoundry(int length, int depth, int i, int j){
        return j >= 0 && j < length && i >= 0 && i < depth;
    }

    private boolean isGrid(Vector<String> vector, int i, int j){
        return vector.get(i).charAt(j) == 'a';
    }


    private void benchmark() throws URISyntaxException, FileNotFoundException {
        URL url = ISMP.class.getResource("chess.txt");
        File file = new File(url.toURI());
        Scanner in = new Scanner(file); // submit , just change to System.in

        // mutiple example to test
        // for hole
        Vector<String> vector = new Vector<>();
        while (in.hasNextLine()){
            String s = in.nextLine();
            System.out.println(s);
            if(s.length() != 0){
                vector.add(s);
            }else{
                oneSideNodes = new LinkedList<>();
                int length = vector.get(0).length();
                int depth = vector.size();
                graph = new Graph(length * depth);

                for (int i = 0; i < depth; i++) {
                    for (int j = 0; j < length; j++) {
                        // throw the hole
                        if(vector.get(i).charAt(j) == 'b')
                            continue;
                        
                        int vertex = i * length + j;
                        
                        if((i + j) % 2 == 0)
                            oneSideNodes.add(vertex);
                        
                        // 询问上下左右是否越界 和 洞
                        if(inBoundry(length, depth, i + 1, j) && isGrid(vector, i + 1 ,j))
                            graph.addEdge(new Edge(vertex, (length * (i + 1)  + j)));

                        if(inBoundry(length, depth, i, j + 1) && isGrid(vector, i ,j + 1))
                            graph.addEdge(new Edge(vertex, (length * (i)  + (j + 1))));

                        if(inBoundry(length, depth, i - 1, j) && isGrid(vector, i - 1 ,j))
                            graph.addEdge(new Edge(vertex, (length * (i - 1)  + j)));

                        if(inBoundry(length, depth, i, j - 1) && isGrid(vector, i ,j - 1))
                            graph.addEdge(new Edge(vertex, (length * (i)  + (j - 1))));
                    }
                }
                if(check()){
                    System.out.println("YES");
                    System.out.println("the match is");
                    for (int i = 0; i < match.length; i++) {
                        if(match[i] != -1){
                            System.out.print("(" + i + "  " + match[i] + ")");
                        }
                    }
                    System.out.println();
                }else{
                    System.out.println("NO");
                }
                vector = new Vector<>();

            }

        }
    }


    private boolean check() {
        // init match for every example
        match = new int[graph.getV()];
        for (int i = 0; i < match.length; i++) {
            match[i] = -1;
        }


        for (int j: oneSideNodes) {
            // every time need a new visited array to indicate
            visited = new boolean[graph.getV()];
            if(!findMatch(j)){
                return false;
            }
        }
        return true;
    }

    private boolean findMatch(int s){
        // 询问所有的邻居
        for(int i: graph.getNeighbors(s)){
            if(!visited[i]) {
                visited[i] = true;
                if (match[i] == -1 || findMatch(match[i])){
                    match[i] = s;
                    return true;
                }
            }
        }
        return false;
    }

    public static void main(String[] args) throws FileNotFoundException, URISyntaxException {
        Chess a = new Chess();
        a.benchmark();
    }
}


class Edge {
    private int x;
    private int y;

    public Edge(int x, int y) {
        this.x = x;
        this.y = y;
    }
    int getX() {
        return x;
    }

    void setX(int x) {
        this.x = x;
    }

    int getY() {
        return y;
    }

    void setY(int y) {
        this.y = y;
    }
}


class Graph {
    private int V;
    private LinkedList<Integer> adjListArray[];

    // constructor
    Graph(int V) {
        this.V = V;
        // define the size of array as
        // number of vertices
        adjListArray = new LinkedList[V];

        // Create a new list for each vertex
        // such that adjacent nodes can be stored
        for(int i = 0; i < V ; i++){
            adjListArray[i] = new LinkedList<>();
        }
    }

    void addEdge(Edge e){
        // this code is really unsecure
        // can be remove by reduant check !
        adjListArray[e.getX()].add(e.getY());
    }

    int getV() {
        return V;
    }

    LinkedList<Integer> getNeighbors(int s){
        return adjListArray[s];
    }
}



package a;


import java.io.File;
import java.io.FileNotFoundException;
import java.net.URISyntaxException;
import java.net.URL;
import java.util.*;

/**
 * Created by martin on 17-10-29.
 *
 */
public class ISMP {
    static class Task implements Comparable<Task>{
        double start;
        double end;

        Task(double start, double end) {
            assert start < end;
            this.start = start;
            this.end = end;
        }


        @Override
        public String toString() {
            return start + "  " + end;
        }

        @Override
        public int compareTo(Task o) {
            if(o.end > this.end){
                return -1;
            }else {
                return 1;
            }
        }


    }




    private static LinkedList<Task> findISMP(LinkedList<Task> allTasks){
        Collections.sort(allTasks);
        LinkedList<Task> res = new LinkedList<>();
        while (!allTasks.isEmpty()){
            Task task = allTasks.removeFirst();
            res.add(task);
            LinkedList<Task> purge = new LinkedList<>();
            for(Task t:allTasks){
                if(!isOverlap(t, task)){
                    purge.add(t);
                }
            }
            allTasks = purge;
        }
        return res;
    }

    private static boolean isOverlap(Task a, Task b){
        return !(a.end < b.start || a.start > b.end);
    }

    private static LinkedList<Task> taskGenerator(int num , int seed){
        Random generator = new Random(seed);
        LinkedList<Task> tasks = new LinkedList<>();
        for (int i = 0; i < num; i++) {
            double start_ = generator.nextDouble();
            double end_ = generator.nextDouble();

            double start = Math.min(start_, end_);
            double end = Math.max(start_, end_);
            Task task = new Task(start, end);
            tasks.add(task);
        }
        Collections.sort(tasks);
        for(Task task:tasks){
            System.out.println(task.toString());
        }
        return tasks;
    }


    public static void main(String[] args) throws URISyntaxException, FileNotFoundException {
        // 第一行为测试样例总数
        // 之后的第一行为tasks 的数目, 之后为tasks
        URL url = ISMP.class.getResource("ISMP.txt");
        File file = new File(url.toURI());
        Scanner in = new Scanner(file); // submit , just change to System.in
        int examples = in.nextInt();
        for (int i = 0; i < examples ; i++) {
            System.out.println(i + " epoch");
            int taskNumber = in.nextInt();
            LinkedList<Task> tasks = new LinkedList<>();
            for (int j = 0; j < taskNumber; j++) {
                double a = in.nextDouble();
                double b = in.nextDouble();
                Task task = new Task(a, b);
                tasks.add(task);
            }
            tasks = findISMP(tasks);
            for(Task t:tasks){
                System.out.println(t.toString());
            }
            System.out.println();
        }

        taskGenerator(10, 4);
    }
}




package a;

import java.io.File;
import java.io.FileNotFoundException;
import java.net.URISyntaxException;
import java.net.URL;
import java.util.Collections;
import java.util.Scanner;
import java.util.Vector;

/**
 * Created by martin on 17-10-29.
 * weighted interval scheduling
 * 3
 */
public class WIS {

    private Vector<Task> tasks;
    private Vector<Task> res;
    private int[] values;
    private int[] compatible;

    class Task implements Comparable<Task>{
        double start;
        double end;
        int weight;

        Task(double start, double end, int weight) {
            assert start < end;
            this.start = start;
            this.end = end;
            this.weight = weight;
        }


        @Override
        public String toString() {
            return start + "  " + end + "  " + weight;
        }

        @Override
        public int compareTo(Task o) {
            if(o.end > this.end){
                return -1;
            }else {
                return 1;
            }
        }
    }

    private void findWIS(Vector<Task> inputTask){
        this.tasks = inputTask;
        Collections.sort(tasks);

        // calculate the largest compatible
        compatible = new int[tasks.size()];
        for (int i = 0; i < compatible.length; i++) {
            double start = tasks.get(i).start;
            // need optmize
            for (int j = 0; j < i; j++) {
                if(tasks.get(j).end < start){
                    compatible[i] = j;
                }else {
                    break;
                }
            }
        }


        values = new int[tasks.size() + 1];
        // by dyanmic programing
        for (int i = 0; i < tasks.size(); i++) {
            values[i + 1] = Math.max(values[compatible[i]] + tasks.get(i).weight, values[i]);
        }

        find(tasks.size() - 1);
    }


    private void find(int j){
        if(j != 0){
            if(tasks.get(j).weight + values[compatible[j]] > values[j]){
                res.add(tasks.get(j));
                find(compatible[j]);
            }else{
                find(j - 1);
            }
        }
    }

    private void doTest() throws URISyntaxException, FileNotFoundException {
        URL url = ISMP.class.getResource("WIS.txt");
        File file = new File(url.toURI());
        Scanner in = new Scanner(file); // submit , just change to System.in
        int examples = in.nextInt();
        for (int i = 0; i < examples ; i++) {
            System.out.println(i + " epoch");
            int taskNumber = in.nextInt();
            res = new Vector<>();
            Vector<Task> tasks = new Vector<>();
            for (int j = 0; j < taskNumber; j++) {
                double a = in.nextDouble();
                double b = in.nextDouble();
                int c = in.nextInt();
                Task task = new Task(a, b, c);
                tasks.add(task);
            }
            findWIS(tasks);
            for(Task t:res){
                System.out.println(t.toString());
            }
            System.out.println();
        }
    }




    public static void main(String[] args) throws URISyntaxException, FileNotFoundException {
        // 第一行为测试样例总数
        // 之后的第一行为tasks 的数目, 之后为tasks
        new WIS().doTest();
    }
}
```
# Instance
1. 
```
abab
aaaa
aaaa
aaaa

aaaaaa
aaaaaa
aaaaaa
aaaaaa

aaaaaaaaaaaaaa
aaaaaaaaaaaaab
aaaaaaaaaaaaaa
aaaaaaaaaaaaab
aaaaaaaaaaaaaa
```
2. 
```
3
3
0.1 0.3
0.2 0.4
0.31 0.5
5
0.07099203475193139  0.731057369148862
0.06712000939049956  0.768156984078079
0.22733466107144407  0.6603196166875382
0.029817676716547004  0.806673557557068
0.8111701180817663  0.9454162249694203
10
0.7306094602878371  0.9187140138555101
0.6795571637816596  0.9186071189908658
0.02481356043541838  0.07838777450255496
0.6992516934753201  0.8049369643305346
0.15123210213417404  0.9245810422363743
0.0033807088945944086  0.7638354259288844
0.7364231848789149  0.9562200971497884
0.18868296808848295  0.8236490954363953
0.3260987760207651  0.7515484122780622
0.23011387269136807  0.2804195352063912
```
3. 
```
3
3
0.1 0.3 3
0.2 0.4 4
0.31 0.5 5
5
0.07099203475193139  0.731057369148862 4
0.06712000939049956  0.768156984078079 6
0.22733466107144407  0.6603196166875382 7
0.029817676716547004  0.806673557557068 78
0.8111701180817663  0.9454162249694203 1
10
0.7306094602878371  0.9187140138555101 1
0.6795571637816596  0.9186071189908658 2
0.02481356043541838  0.07838777450255496 3
0.6992516934753201  0.8049369643305346 100
0.15123210213417404  0.9245810422363743 1
0.0033807088945944086  0.7638354259288844 3
0.7364231848789149  0.9562200971497884 3
0.18868296808848295  0.8236490954363953 4
0.3260987760207651  0.7515484122780622 5
0.23011387269136807  0.2804195352063912 6
```