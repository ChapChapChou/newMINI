class Inheritance {
    public static void main(String[] args) {
        System.out.println(0);
    }
}

class A extends B {}
class B extends A {}
class C extends D {}
class D extends C {}
class E extends B {}
