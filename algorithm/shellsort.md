```java

package eleven;

import java.util.Arrays;

public class ShellSort {

    public static void main(String[] args) {
        int[] array = {71, 49, 92, 55, 38, 82, 72, 53};
        System.out.println("result = " + Arrays.toString(array));
        shellSort(array);
    }

    public static void shellSort(int[] a) {
        shellSort(a, a.length);
    }

    private static int getGap(int length) {
        if (length > 1 && length % 2 == 1) {
            length++;
        }
        return length / 2;
    }

    private static void shellSort(int[] a, int size) {
        int gap = getGap(size);
        while(gap > 0) {
            for(int i = gap; i < size; i++) {
                for (int j = i; j >= gap && a[j] < a[j - gap]; j -= gap) {
                    swap(a, j, j - gap);
                    System.out.println("gap = "+ gap +", result = " + Arrays.toString(a));
                }
            }
            gap = getGap(gap);
        }
    }

    private static void swap(int[] a, int i, int j) {
        int swap = a[i];
        a[i] = a[j];
        a[j] = swap;
    }

}



```