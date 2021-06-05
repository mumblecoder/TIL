```java
package eleven;

import java.util.Arrays;

public class QuickSort {
    public static void main(String[] args) {
        int[] array = { 31, 19, 32, 33, 77, 85, 66, 53 };
        System.out.println("#### QuickSort");
        System.out.println("result = " + Arrays.toString(array));
        quickSort(array, 0, array.length - 1);
    }

    public static void quickSort(int[] arr, int start, int end) {
        if (start >= end) { 
            return;
        }

        int pivot = start;
        int temp, i, j;
        do {
            i = start + 1; // i++ (pivot 제외 = +1)
            j = end; // j--

            // --> 방향으로 피벗값보다 큰값 찾을때 까지
            while (arr[i] < arr[pivot]) {
                i++;
                if (i >= end) {
                    i = pivot;
                }
            }

            // <-- 방향으로 피벗값보다 작은 값 찾을때 까지
            while (arr[j] > arr[pivot]) {
                j--;
                if (j <= start) {
                    j = pivot;
                }
            }

            if (i < j) {
                temp = arr[j];
                arr[j] = arr[i];
                arr[i] = temp;
                System.out.println("result = " + Arrays.toString(arr));
            } else if (j != pivot) {
                temp = arr[j];
                arr[j] = arr[pivot];
                arr[pivot] = temp;
                System.out.println("result = " + Arrays.toString(arr));
            }
        } while (i < j);
        quickSort(arr, start, j - 1);
        quickSort(arr, j + 1, end);
    }

}
```