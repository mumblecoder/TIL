```java

package eleven;

import java.util.Arrays;

public class HeapSort {

    public static void main(String[] args) {
        int[] array = { 71, 49, 92, 55, 38, 82, 72, 53 };
        System.out.println("result = " + Arrays.toString(array));
        sort(array);
        // 최대 힙 : result = [92, 55, 82, 53, 38, 71, 72, 49]
    }

    public static void sort(int[] a) {
        sort(a, a.length);
    }

    private static void sort(int[] a, int size) {

        int parentIdx = getParent(size - 1);

        for(int i = parentIdx; i >= 0; i--) {
            heapify(a, i, size - 1);
        }

        for(int i = size - 1; i > 0; i--) {
            swap(a, 0, i);
            heapify(a, 0, i - 1);
        }

    }

    private static int getParent(int child) {
        return (child - 1) / 2;
    }

    private static void swap(int[] a, int i, int j) {
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
        System.out.println("result = " + Arrays.toString(a));
    }

    private static void heapify(int[] a, int parentIdx, int lastIdx) {

        int leftChildIdx = 2 * parentIdx + 1;
        int rightChildIdx = 2 * parentIdx + 2;
        int largestIdx = parentIdx;

        if(leftChildIdx <= lastIdx && a[largestIdx] < a[leftChildIdx]) {
            largestIdx = leftChildIdx;
        }

        if(rightChildIdx <= lastIdx && a[largestIdx] < a[rightChildIdx]) {
            largestIdx = rightChildIdx;
        }

        if(parentIdx != largestIdx) {
            swap(a, largestIdx, parentIdx);
            heapify(a, largestIdx, lastIdx);
        }
    }
}



```