```java
package ten;

import java.util.LinkedList;
import java.util.Queue;

public class Bfs {

    static int[] search = new int[10];
    static int[][] BFS = {
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

    static void bfs(int v) {
        Queue<Integer> q = new LinkedList<>();
        search[v] = 1;
        q.offer(v);

        while(!q.isEmpty()){
            int x = q.poll();
            for(int i=0; i<=9; i++){
                if(search[i] != 1 && BFS[x][i] == 1){
                    search[i] = 1;
                    q.offer(i);
                    System.out.println(x + "에서 " + i + "로 이동!");
                }
            }
        }
    }


}

```