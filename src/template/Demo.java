class Demo
{
    public static void main(String[] input)
    {
        Cal c = new Cal();
        int index = 0;
        int result = 0;
        while(index < 100) {
            result = c.add(3, result);
            index = index + 1;
            if(result % 2 == 1) {
                result = result * 2;
            }
            else {
                result = result / 2;
            }
        }
        System.out.println(result);
    }
}

class Cal
{
    public int add(int a, int b)
    {
        return a + b;
    }

    public int maxint()
    {
        int a = 222222;
        return a;
    }
}
