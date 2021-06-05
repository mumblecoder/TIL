### 재귀사용
```java

package eleven;

import java.util.Arrays;

public class MergeSort {

    private static int[] sorted;

    public static void main(String[] args) {
        int[] array = {71, 49, 92, 55, 38, 82, 72, 53};
        System.out.println("result = " + Arrays.toString(array));
        mergeSort(array);
    }

    public static void mergeSort(int[] a) {
        sorted = new int[a.length];
        mergeSort(a, 0, a.length - 1);
        sorted = null;
    }

    private static void mergeSort(int[] a, int left, int right) {
        if(left == right) {
            return;
        }
        int mid = (left + right) / 2;

        mergeSort(a, left, mid);
        mergeSort(a, mid + 1, right);
        merge(a, left, mid, right);
    }

    private static void merge(int[] a, int left, int mid, int right) {
        int l = left;
        int r = mid + 1;
        int idx = left;

        while(l <= mid && r <= right) {
            if(a[l] <= a[r]) {
                sorted[idx] = a[l++];
            } else {
                sorted[idx] = a[r++];
            }
            idx++;
        }

        if(l > mid) {
            while(r <= right) {
                sorted[idx] = a[r++];
                idx++;
            }
        } else {
            while(l <= mid) {
                sorted[idx] = a[l++];
                idx++;
            }
        }

        for(int i = left; i <= right; i++) {
            a[i] = sorted[i];
        }
        System.out.println("result = " + Arrays.toString(a));
    }

}


```

### 반복사용
```java

package five;

import java.util.Arrays;

public class MergeSort {

    private static int[] sorted;

    public static void main(String[] args) {
        int[] array2 = { 71, 49, 92, 55, 38, 82, 72, 53 };
        System.out.println("#### MergeSort ");
        merge_sort(array2);
        System.out.println("result = " + Arrays.toString(array2));
    }

    public static void merge_sort(int[] a) {
        sorted = new int[a.length];
        int right = a.length - 1;
        for(int size = 1; size <= right; size += size) {
            for(int l = 0; l <= right - size; l += (2 * size)) {
                int low = l;
                int mid = l + size - 1;
                int high = Math.min(l + (2 * size) - 1, right);
                merge(a, low, mid, high);		// 병합작업
            }
        }
        sorted = null;
    }

    private static void merge(int[] a, int left, int mid, int right) {
        int l = left;
        int r = mid + 1;
        int idx = left;

        while(l <= mid && r <= right) {
            if(a[l] <= a[r]) {
                sorted[idx] = a[l++];
            } else {
                sorted[idx] = a[r++];
            }
            idx++;
        }

        if(l > mid) {
            while(r <= right) {
                sorted[idx] = a[r++];
                idx++;
            }
        } else {
            while(l <= mid) {
                sorted[idx] = a[l++];
                idx++;
            }
        }

        for(int i = left; i <= right; i++) {
            a[i] = sorted[i];
        }
    }

}

```