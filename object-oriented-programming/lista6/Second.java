// Dawid Pawliczek 347081 lista 6 zadanie 4

import java.util.Arrays;
import java.util.Comparator;

class MergeSort {

    private static class MergeSortRunnable<T extends Comparable<T>> implements Runnable {
        private T[] array;
        private int left, right;
        private Comparator<? super T> comparator;

        public MergeSortRunnable(T[] array, int left, int right, Comparator<? super T> comparator) {
            this.array = array;
            this.left = left;
            this.right = right;
            this.comparator = comparator;
        }

        @Override
        public void run() {
            mergeSort(array, left, right, comparator);
        }
    }

    public static <T extends Comparable<T>> void parallelMergeSort(T[] array) {
        Comparator<T> comparator = Comparator.naturalOrder();
        mergeSort(array, 0, array.length - 1, comparator);
    }

    private static <T extends Comparable<T>> void mergeSort(T[] array, int left, int right,
            Comparator<? super T> comparator) {
        if (left < right) {
            int middle = (left + right) / 2;

            Thread leftSorter = new Thread(new MergeSortRunnable<>(array, left, middle, comparator));
            Thread rightSorter = new Thread(new MergeSortRunnable<>(array, middle + 1, right, comparator));

            leftSorter.start();
            rightSorter.start();

            try {
                leftSorter.join();
                rightSorter.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            merge(array, left, middle, right, comparator);
        }
    }

    private static <T extends Comparable<T>> void merge(T[] array, int left, int middle, int right,
            Comparator<? super T> comparator) {
        Object[] leftTempArray = new Object[middle - left + 1];
        Object[] rightTempArray = new Object[right - middle];

        for (int i = 0; i < leftTempArray.length; i++) {
            leftTempArray[i] = array[left + i];
        }
        for (int i = 0; i < rightTempArray.length; i++) {
            rightTempArray[i] = array[middle + 1 + i];
        }

        int leftIndex = 0, rightIndex = 0;
        int currentIndex = left;

        while (leftIndex < leftTempArray.length && rightIndex < rightTempArray.length) {
            if (comparator.compare((T) leftTempArray[leftIndex], (T) rightTempArray[rightIndex]) <= 0) {
                array[currentIndex++] = (T) leftTempArray[leftIndex++];
            } else {
                array[currentIndex++] = (T) rightTempArray[rightIndex++];
            }
        }

        while (leftIndex < leftTempArray.length) {
            array[currentIndex++] = (T) leftTempArray[leftIndex++];
        }
        while (rightIndex < rightTempArray.length) {
            array[currentIndex++] = (T) rightTempArray[rightIndex++];
        }
    }

    public static void main(String[] args) {

        // Sorting an array of integers
        Integer[] numbers = { 3, 60, 35, 2, 45, 320, 5 };
        System.out.println("Array before sort: " + Arrays.toString(numbers));
        parallelMergeSort(numbers);
        System.out.println("Array after sort: " + Arrays.toString(numbers));

        // Sorting an array of strings
        String[] names = { "John", "Alice", "Bob", "David", "Catherine" };
        System.out.println("Array before sort: " + Arrays.toString(names));
        parallelMergeSort(names);
        System.out.println("Array after sort: " + Arrays.toString(names));

    }
}