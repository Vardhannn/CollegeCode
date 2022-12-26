package threads;

public class Test extends Thread {
    public void run() {
        try {
            Thread.sleep(1000);
            System.out.println("the current method is: " + Thread.currentThread().getName());
        } catch (Exception e) {
            System.out.println("exception occured");
        }
    }

    public static void main(String[] args) {
        Test t = new Test();
        Main m = new Main();
        Thread t1 = new Thread();
        Thread t2 = new Thread();
        Thread t3 = new Thread();
        t1.run();
        try {
            m.first();
            t1.join();
        } catch (Exception e) {
        }
        try {
            m.second();
            t2.join();
        } catch (Exception e) {
        }
        try {
            m.third();
            t3.join();
        } catch (Exception e) {
        }
    }
}
