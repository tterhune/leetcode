class DuplicateZeros {

    public static void main(String[] args) {
        int [] arr = {1,0,2,3,0,4,5,0};
        duplicateZeros(arr);
        for (int i : arr) {
            System.out.println(i);
        }
    }

    private static void duplicateZeros(int[] arr) {
        int numZeros = 0;
        for (int num : arr) {
            if (num == 0) {
                numZeros++;
            }
        }
        if (numZeros == 0) {
            return;
        }
        int newIdx = arr.length + numZeros - 1;
        System.out.println("newIdx = " + newIdx);
        for (int oldIdx = arr.length - 1; oldIdx >= 0; oldIdx--) {
            if (newIdx < arr.length) {
                arr[newIdx] = arr[oldIdx];
            }
            newIdx--;
            if (arr[oldIdx] == 0) {
                if (newIdx < arr.length) {
                    arr[newIdx] = arr[oldIdx];
                }
                newIdx--;
            }
        }
    }
}
