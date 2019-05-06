package ec.app.tutorial4;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;


public class Reader {
    private ArrayList<Instance> data;
    private String file_path;

    public Reader(String path) {
        this.file_path = path;
        this.data = reading(file_path);
    }

    private static ArrayList<Instance> reading(String file_path) {

        ArrayList<Instance> data = new ArrayList<>();
        try {
            BufferedReader fr = new BufferedReader(new FileReader(file_path));
            String line = fr.readLine();
            while (line != null) {
                String[] tokens = line.split(" ");
                int att1 = Integer.parseInt(tokens[0]);
                int att2 = Integer.parseInt(tokens[1]);
                int att3 = Integer.parseInt(tokens[2]);
                int att4 = Integer.parseInt(tokens[3]);
                int att5 = Integer.parseInt(tokens[4]);
                int att6 = Integer.parseInt(tokens[5]);
                int att7 = Integer.parseInt(tokens[6]);
                int att8 = Integer.parseInt(tokens[7]);
                int att9 = Integer.parseInt(tokens[8]);
                int label = Integer.parseInt(tokens[9]);
                Instance instance = new Instance(att1, att2, att3, att4, att5, att6, att7, att8, att9, label);
                data.add(instance);
                line = fr.readLine();
            }
            fr.close();

        } catch (FileNotFoundException e) {
            System.out.println(e.getMessage() + "Notfoundfile");
        } catch (IOException ei) {
            System.out.println(ei.getMessage() + "iofailed");
        } catch (NumberFormatException gg) {
            System.out.println(gg.getMessage() + "number formation problem");
        } catch (NullPointerException n) {
            System.out.println(n.getMessage() + "Nullpointer problem");
        }


        return data;


    }

    public void print() {
        for (Instance o : data) {
            if (o == null) {
                System.out.println("print null attr");
            } else {
                System.out.println(o.toString());
            }
        }
    }

    public ArrayList<Instance> getData() {
        return this.data;
    }
}
