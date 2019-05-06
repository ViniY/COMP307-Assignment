/*
  Copyright 2006 by Sean Luke
  Licensed under the Academic Free License version 3.0
  See the file "LICENSE" for more information
*/


package ec.app.tutorial4;

import ec.EvolutionState;
import ec.Individual;
import ec.gp.GPIndividual;
import ec.gp.GPProblem;
import ec.gp.koza.KozaFitness;
import ec.simple.SimpleProblemForm;
import ec.util.Parameter;

import java.util.ArrayList;

public class MultiValuedRegression extends GPProblem implements SimpleProblemForm {
    private static final long serialVersionUID = 1;

    //    public double currentX;
    public ArrayList<Integer> training_label = new ArrayList<>();
    public double x1, x2, x3, x4, x5, x6, x7, x8, x9;


    public void setup(final EvolutionState state,
                      final Parameter base) {
        super.setup(state, base);

        // verify our input is the right class (or subclasses from it)
        if (!(input instanceof DoubleData))
            state.output.fatal("GPData class must subclass from " + DoubleData.class,
                    base.push(P_DATA), null);
    }

    public void evaluate(final EvolutionState state,
                         final Individual ind,
                         final int subpopulation,
                         final int threadnum) {
        ArrayList<Instance> data_training = new ArrayList<>();

        String training_path = "/home/yuyong1/307A2/part3/training.txt";

        Reader r_training = new Reader(training_path);
        data_training = r_training.getData();
//            System.out.println("There are "+ data_training.size() + " data in the set");

        for (int i = 0; i < data_training.size(); i++) {
            Instance temp = data_training.get(i);
            int label = temp.getLabel();
            training_label.add(label);
        }

        if (!ind.evaluated)  // don't bother reevaluating
        {
            DoubleData input = (DoubleData) (this.input);

            int hits = 0;
            double sum = 0.0;
            double expectedResult;
            double result;
            int length = data_training.size();
            for (int y = 0; y < data_training.size(); y++) {
                x1 = (double) data_training.get(y).getFeature1();
                x2 = (double) data_training.get(y).getFeature2();
                x3 = (double) data_training.get(y).getFeature3();
                x4 = (double) data_training.get(y).getFeature4();
                x5 = (double) data_training.get(y).getFeature5();
                x6 = (double) data_training.get(y).getFeature6();
                x7 = (double) data_training.get(y).getFeature7();
                x8 = (double) data_training.get(y).getFeature8();
                x9 = (double) data_training.get(y).getFeature9();
                expectedResult = (double) data_training.get(y).getLabel();

                //compute input.x
                ((GPIndividual) ind).trees[0].child.eval(
                        state, threadnum, input, stack, ((GPIndividual) ind), this);

                //result = Math.abs(expectedResult - input.x);
//                    System.out.println(input.x);
//                    System.out.println(expectedResult);
                if ((input.x <= 0 && expectedResult == 2.00) || (input.x > 0 && expectedResult == 4.00)) hits++;
                //sum += result;
            }

            // the fitness better be KozaFitness!
            KozaFitness f = ((KozaFitness) ind.fitness);
            sum = ((double) data_training.size() - hits) / data_training.size();
            f.setStandardizedFitness(state, sum);
            f.hits = hits;
            ind.evaluated = true;
            data_training.clear();
        }
    }

    @SuppressWarnings("Duplicates")
    public void describe(EvolutionState state, Individual ind, int subpopulation, int threadnum, int log) {
        DoubleData input = (DoubleData) (this.input);

        // we do the testing set here
        String test_path = "/home/yuyong1/307A2/part3/test.txt";
        Reader r_test = new Reader(test_path);
        ArrayList<Instance> data_test = new ArrayList<>();
        data_test = r_test.getData();


        state.output.println("\n\nPerformance of Best Individual on Testing Set:\n", log);

        int hits = 0;
        double sum = 0.0;
        double expectedResult;

        for (int y = 0; y < data_test.size(); y++) {
            x1 = (double) data_test.get(y).getFeature1();
            x2 = (double) data_test.get(y).getFeature2();
            x3 = (double) data_test.get(y).getFeature3();
            x4 = (double) data_test.get(y).getFeature4();
            x5 = (double) data_test.get(y).getFeature5();
            x6 = (double) data_test.get(y).getFeature6();
            x7 = (double) data_test.get(y).getFeature7();
            x8 = (double) data_test.get(y).getFeature8();
            x9 = (double) data_test.get(y).getFeature9();
            expectedResult = (double) data_test.get(y).getLabel();


            ((GPIndividual) ind).trees[0].child.eval(
                    state, threadnum, input, stack, ((GPIndividual) ind), this);

            if ((input.x < 0 && expectedResult == 2.00) || (input.x > 0 && expectedResult == 4.00)) hits++;


        }

        // the fitness better be KozaFitness!

        KozaFitness f = (KozaFitness) (ind.fitness.clone());     // make a copy, we're just printing it out
        sum = (double) (data_test.size() - hits) / data_test.size();
        f.setStandardizedFitness(state, sum);
        f.hits = hits;


        f.printFitnessForHumans(state, log);
    }


}

