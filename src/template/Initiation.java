class Initiation {
    public static void main(String[] args) {
        System.out.println(new I().run(0));
    }
}

class I {
    public int run(int i) {
        int x;
        int y;
        y = x;

        while (i < 0) {
            x = 1;
            y = i - 1;
        }

        if (i < 0) {
            x = 1;
        } else {
            y = i - 1;
        }

        return x + y;
    }
}
