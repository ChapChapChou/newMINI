class MissingSymbol {
    public static void main(String[] args) {
        Cal cal = new Cal();
        System.out.println(new MS().run());
    }
}

class MS {
    public int run() {
        x = y + 1;
        return z;
    }
}
