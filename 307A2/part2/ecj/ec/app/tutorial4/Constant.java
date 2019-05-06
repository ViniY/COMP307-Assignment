package ec.app.tutorial4;

import ec.EvolutionState;
import ec.Problem;
import ec.gp.ADFStack;
import ec.gp.GPData;
import ec.gp.GPIndividual;
import ec.gp.GPNode;
//import ec.util.*;
import ec.util.Parameter;

public class Constant extends GPNode {
    public double constant;
    @Override
    public String toString() {
        return String.format("%2f",constant);
    }
    public int expectedChildren() {
        return 0;
    }

    public void checkConstraints(final EvolutionState state, final int tree, final GPIndividual typicalIndividual,
                                 final Parameter individualBase) {
        super.checkConstraints(state, tree, typicalIndividual, individualBase);

        if (children.length != 0)
            state.output.error("Incorrect number of children for node " + toStringForError() + " at " + individualBase);
    }

    @Override
    public void eval(final EvolutionState state, final int thread, final GPData input, final ADFStack stack,
                     final GPIndividual individual, final Problem problem) {
        DoubleData rd = ((DoubleData) (input));
        rd.x = state.random[thread].nextDouble();//((MultiValuedRegression) problem).constVal;

        // System.out.println(rd.x);
        constant = rd.x;
    }
}
