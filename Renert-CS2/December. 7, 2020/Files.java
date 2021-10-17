import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Files {
    public static void main(String[] args) 
    {
        writeToFile();
    }

    public static void writeToFile() 
    {
        try {
            // If you give a filename that doesn't exist, it creates the file
            FileWriter myWriter = new FileWriter("test.txt", true); // 2nd argument specifies whether we append to file

            myWriter.write("This text has been appended\n");

            // Convert to string before writing to files
            myWriter.write(Integer.toString(25));
            myWriter.write("\n");
            myWriter.write(Double.toString(25.312453));
            myWriter.write("\n");

            myWriter.close();
            System.out.println("Successfully wrote to file");
        }
        catch(IOException e) {
            System.out.println("Could not write to file.");
            e.printStackTrace();
        }
    }

    public static void readFromFile() {
        try {
            File my_file = new File("test.txt");
            // Reads data from our file
            Scanner sc = new Scanner(my_file);

            while (sc.hasNextLine()) {
                String data = sc.nextLine();
                System.out.println(data);
            }
            sc.close();
    
            System.out.println(my_file.getAbsolutePath());
            System.out.println(my_file.length());
            System.out.println(my_file.canWrite());
            System.out.println(my_file.canRead());

        }
        catch (FileNotFoundException e) {
            System.out.println("File not found");
            e.printStackTrace();
        }
    }
}