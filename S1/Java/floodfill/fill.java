package floodfill;

import java.util.Scanner;
import java.util.Arrays;
public class fill {
    private void fillGrid(char[][] arr, int r, int c)
    {
        if (arr[r][c] == '1'){
            arr[r][c] = '2';
            fillGrid(arr, r + 1, c);
            fillGrid(arr, r - 1, c);
            fillGrid(arr, r, c + 1);
            fillGrid(arr, r, c - 1);
        }


    }
    private void display(char[][] arr)
    {
        System.out.println("\nGrid : ");
        for (int i = 1; i < arr.length - 1; i++)
        {
            for (int j = 1; j < arr[i].length - 1; j++)
                System.out.print(arr[i][j] +" ");
            System.out.println();
        }
    }
    public static void main(String[] args)
    {
        Scanner scan = new Scanner( System.in );
        System.out.println("Flood Fill Test\n");
        System.out.println("Enter dimensions of grid");
        int M = scan.nextInt();
        int N = scan.nextInt();
        char[][] arr = new char[M + 2][N + 2];
        for (int i = 0; i < M + 2; i++)
            Arrays.fill(arr[i], 'O');
        System.out.println("Enter grid with '1' for passage and '0' for obstacle");
        for (int i = 1; i < M + 1; i++)
            for (int j = 1; j < N + 1; j++)
                arr[i][j] = scan.next().charAt(0);
        System.out.println("Enter coordinates to start ");
        int sr = scan.nextInt();
        int sc = scan.nextInt();
        if (arr[sr][sc] != '1')
        {
            System.out.println("Invalid coordinates");
            System.exit(0);
        }
        fill ff = new fill();
        ff.display(arr);
        ff.fillGrid(arr, sr, sc);
        ff.display(arr);
    }
}

