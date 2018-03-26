# Homework Three

## Implement the matrix chain multiple
language: java openJdk 1.82  
os: ubuntu  
specification: the input file should be located as the same folder with the Matrix class  
```
import java.io.File;
import java.io.FileNotFoundException;
import java.net.URISyntaxException;
import java.net.URL;
import java.util.Scanner;


public class Matrix {
    public static void main(String[] args) throws FileNotFoundException, URISyntaxException {
        Matrix matrix = new Matrix();
        matrix.matrixCalculation();
    }

    /**
     * multiple array of data for input。
     * the first number is the number of matrix
     * there are n line below, every line containing two number, row and column
     *
     * you should assume the data will not overflow
     * */

    private void matrixCalculation() throws URISyntaxException, FileNotFoundException {

        // get data input
        URL url = Matrix.class.getResource("matrixInput.txt");
        File file = new File(url.toURI());
        Scanner in = new Scanner(file);
        int matrixNum = in.nextInt();
        int[] size = new int[matrixNum + 1];
        for (int i = 0; i < matrixNum; i++) {
            int a = in.nextInt();
            int b = in.nextInt();

            if(size[i] != 0 && size[i] != a){
                throw new RuntimeException("the input data can not used as matrix calculation !");
            }

            if(size[i + 1] != 0 && size[i + 1] != b){
                throw new RuntimeException("the input data can not used as matrix calculation !");
            }
            size[i] = a;
            size[i + 1] = b;
        }

        // dp
        long [][] ijCal = new long[matrixNum + 1][matrixNum + 1];

        for (int i = 1; i <= matrixNum - 1; i++) { // the distance is as most n - 1
            for (int j = 1; j <= matrixNum - 1; j++) {  // start index between 1 and n -1
                if(i == 1){ // basic elements
                    ijCal[j][j + i] = (long)size[j - 1]  * (long)size[j] * (long)size[j + 1];
                }else{
                    if(i + j > matrixNum) continue;
                    long min = 0;

                    for (int k = j; k < j + i; k++) {
                        long t = ijCal[j][k] + ijCal[k + 1][j + i] +
                                (long)size[j - 1] * (long)size[k] * (long)size[i + j];
                        if (min == 0) {
                            min = t;
                        } else {
                            min = Math.min(min, t);
                        }
                    }
                    ijCal[j][j + i] = min;
                }
            }
        }
        System.out.println("minimum scalar multiplications:" + ijCal[1][matrixNum]);

    }
}
```

## Sequence Alignment
environment is same as above  
Here is the code  
```
import java.io.File;
import java.io.FileNotFoundException;
import java.net.URISyntaxException;
import java.net.URL;
import java.util.Scanner;
/**
 * todo: merge the input to a function !
 *
 * */

public class SequenceAlignment {
    public static void main(String[] args) throws FileNotFoundException, URISyntaxException {
//        sequenceAlignmentDp();
        sequenceAlignmentSP();
    }

    /**
     * there is multiple input line
     * for convenience, character are replace with integer number !
     *   */
    private static void sequenceAlignmentDp() throws URISyntaxException, FileNotFoundException {

        URL url = Matrix.class.getResource("SA.txt");
        File file = new File(url.toURI());
        Scanner in = new Scanner(file);

        int alphaSetSize = in.nextInt();
        int[] alphaCost = new int[alphaSetSize];
        int[][] differenceCost = new int[alphaSetSize][alphaSetSize];

        int s1Length;
        int s2Length;

        int[] s1;
        int[] s2;

        for (int i = 0; i < alphaSetSize; i++) {
            alphaCost[i] = in.nextInt();
        }

        for (int i = 0; i < alphaSetSize; i++) {
            for (int j = 0; j < alphaSetSize; j++) {
                differenceCost[i][j] = in.nextInt();
            }
        }

        s1Length = in.nextInt();
        s1 = new int[s1Length + 1];
        for (int i = 1; i < s1Length + 1; i++) {
            s1[i] = in.nextInt();
        }

        s2Length = in.nextInt();
        s2 = new int[s2Length + 1];
        for (int i = 1; i < s2Length + 1; i++) {
            s2[i] = in.nextInt();
        }

        int[][] costs = new int[s1Length + 1][s2Length + 1];
        // query table for the cost i and j is costs[i][j]

        // init the table, costs[0][0] = 0
        for (int j = 0; j <= s2Length; j++) {
            costs[0][j] = 0;
            for (int i = 1; i <= j; i++) {
                costs[0][j] += alphaCost[s2[i]];
            }
        }

        for (int i = 0; i <= s1Length; i++) {
            costs[i][0] = 0;
            for (int j = 1; j <= i ; j++) {
                costs[i][0] += alphaCost[s1[j]];
            }
        }

        // pave the table
        // the direction is up then left
        for (int i = 1; i < s1Length + 1; i++) {
            for (int j = 1; j < s2Length + 1    ; j++) {
                int a = costs[i][j - 1] + alphaCost[s2[j]];
                int b = costs[i - 1][j] + alphaCost[s1[i]];
                int c = costs[i - 1][j - 1] + differenceCost[s1[i]][s2[j]];
                costs[i][j] = Math.min(a, Math.min(b, c));
            }
        }
        System.out.println(costs[s1Length][s2Length]);
    }

    private static void sequenceAlignmentSP() throws URISyntaxException, FileNotFoundException {
        URL url = Matrix.class.getResource("SA.txt");
        File file = new File(url.toURI());
        Scanner in = new Scanner(file);

        int alphaSetSize = in.nextInt();
        int[] alphaCost = new int[alphaSetSize];
        int[][] differenceCost = new int[alphaSetSize][alphaSetSize];

        int s1Length;
        int s2Length;

        int[] s1;
        int[] s2;

        for (int i = 0; i < alphaSetSize; i++) {
            alphaCost[i] = in.nextInt();
        }

        for (int i = 0; i < alphaSetSize; i++) {
            for (int j = 0; j < alphaSetSize; j++) {
                differenceCost[i][j] = in.nextInt();
            }
        }

        s1Length = in.nextInt();
        s1 = new int[s1Length + 1];
        for (int i = 1; i < s1Length + 1; i++) {
            s1[i] = in.nextInt();
        }

        s2Length = in.nextInt();
        s2 = new int[s2Length + 1];
        for (int i = 1; i < s2Length + 1; i++) {
            s2[i] = in.nextInt();
        }

        int[][] costs = new int[s1Length + 1][s2Length + 1];


        for (int i = 0; i < s1Length + 1; i++) {
            for (int j = 0; j < s2Length + 1; j++) {
                costs[i][j] = Integer.MAX_VALUE;
            }
        }
        costs[0][0] = 0;

        int[][][] edge = new int[s1Length + 1][s2Length + 1][3];
        for (int i = 0; i < s1Length + 1; i++) {
            for (int j = 0; j < s2Length + 1; j++) {

                if(j < s2Length) edge[i][j][0] = alphaCost[s2[j + 1]];

                if(i < s1Length) edge[i][j][2] = alphaCost[s1[i + 1]];

                if(i < s1Length && j < s2Length)
                    edge[i][j][1] = differenceCost[s1[i + 1]][s2[j + 1]];
            }
        }

        // relax the edge
        int vertexNum = (1 + s1Length) * (s2Length + 1);

        for (int k = 0; k < vertexNum; k++) {
            for (int i = 0; i < s1Length + 1; i++) {
                for (int j = 0; j < s2Length + 1; j++) {
                    // for every valid edge relax
                    // caution : overflow
                    if(j < s2Length) {
                        costs[i][j + 1] = Math.min(edge[i][j][0] + costs[i][j], costs[i][j + 1]);
                    }


                    if(i < s1Length) {
                        costs[i + 1][j] = Math.min(edge[i][j][2] + costs[i][j], costs[i + 1][j]);
                    }

                    if(i < s1Length && j < s2Length){
                        costs[i + 1][j + 1] =
                                Math.min(edge[i][j][1] + costs[i][j], costs[i + 1][j + 1]);
                    }
                }
            }
        }

        System.out.println(costs[s1Length][s2Length]);
    }
}

```
3. 最短路径实现的方法有 Dijsktra 和 Bellman-Ford的方法, 代码的实现的为Bellman-Ford 的方法,测试显示
Shorest Path的方法要远远慢与 DP. DP 的算法的复杂度为 O(n ^ 2), 采用Bellman-Ford算法的复杂度为O(n^ 4)
而采用Dijkstra 算法的复杂度为近似为O(n^2 *log(n^2))

注: 本次实验采用测试样例均为[@EAirPeter](https://github.com/EAirPeter)提供
