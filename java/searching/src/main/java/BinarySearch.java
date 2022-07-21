
class BinarySearch {
    private static int search(int[] numbers, int num) {
        int start = 0;
        int end = numbers.length - 1;

        while (start <= end) {
            int mid = start + (end - start)/2;
            if (num < numbers[mid]) {
                end = mid -1;
            } else if (num > numbers[mid]) {
                start = mid + 1;
            }
            else {
                return mid;
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        int [] arr = {-1, 10, 13, 15, 23, 54, 88, 97, 153};
        int [] testArray = {20, -1, 23, 200, 88, 2, 54, -2, 97};

        for (int i = 0; i < arr.length; i++) {
            System.out.printf("array[%d] = %d\n", i, arr[i]);
        }

        for (int searchValue : testArray) {
            int index = search(arr, searchValue);
            if (index >= 0){
                System.out.printf("FOUND: %d, at index: %d\n", searchValue, index);
            }
            else {
                System.out.printf("NOT FOUND: %d\n", searchValue);
            }
        }
    }


}
