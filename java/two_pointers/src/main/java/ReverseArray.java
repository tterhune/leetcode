package main.java;

class ReverseArray {

    private static void print(int[] array) {
        for (int i = 0; i < array.length; i++) {
            System.out.printf("array[%d] = %d\n", i, array[i]);
        }
    }
    private static void reverse(int[] array) {
        int j = array.length - 1;
        int i = 0;
        while (i < j) {
            int tmp = array[i];
            array[i++] = array[j];
            array[j--] = tmp;
        }

    }

    public static void main(String[] args) {
        int [] arr = {-1, 10, 13, 15, 23, 54, 88, 97, 153};
        print(arr);
        reverse(arr);
        print(arr);
    }


}
