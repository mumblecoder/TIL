```java
package ten;

public class Dfs {

    static int[] search = new int[10];
    static int[][] DFS = {
            {0,1,0,0,0,0,0,0,0,0},
            {1,0,1,1,0,0,0,0,0,0},
            {0,1,0,0,1,0,0,0,0,0},
            {0,1,0,0,1,1,0,0,0,0},
            {0,0,1,1,0,0,0,0,0,0},
            {0,0,0,1,0,0,1,1,0,0},
            {0,0,0,0,0,1,0,1,0,0},
            {0,0,0,0,0,1,1,0,1,1},
            {0,0,0,0,0,0,0,1,0,0},
            {0,0,0,0,0,0,0,1,0,0},
    };

    public static void DFS(int v) {
        search[v] = 1;
        for (int i = 0; i <= 9; i++) {
            if (search[i] != 1 && DFS[v][i] == 1 ) {
                System.out.println(v + "에서 " + i + "로 이동!");
                DFS(i);
            }
        }
    }

}

```