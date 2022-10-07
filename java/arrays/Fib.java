public class Fib {

    public static int fib(int n) {
        if (n == 0 || n == 1) {
            return n;
        }

        int f2 = 0;
        int f1 = 1;

        int sum = f2 + f1;
        for (int i = 2; i < i++) {
            f2 = f1;
            f1 = sum;

            System.out.printf("F2: %d F1: %d Sum: %d\n", f2, f1, sum);
        }

        return sum;
    }

    public static void main(String[] args) {
        int [] fibs = {0, 1, 1, 2, 3, 5, 8, 14, 22, 36};

        for (int i = 0; i < 9; i++) {
            int result = fib(i);
            assert (result == fibs[i]);
            System.out.println("Fib of " + i + " Result = " + result);
        }
    }
}
