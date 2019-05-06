package ec.app.tutorial4;

import ec.EvolutionState;
import ec.Problem;
import ec.gp.ADFStack;
import ec.gp.GPData;
import ec.gp.GPIndividual;
import ec.gp.GPNode;

public class Protect_Div extends GPNode {
    public String toString() {
        return "/";
    }

    /*
      public void checkConstraints(final EvolutionState state,
      final int tree,
      final GPIndividual typicalIndividual,
      final Parameter individualBase)
      {
      super.checkConstraints(state,tree,typicalIndividual,individualBase);
      if (children.length!=2)
      state.output.error("Incorrect number of children for node " +
      toStringForError() + " at " +
      individualBase);
      }
    */
    public int expectedChildren() {
        return 2;
    }

    public void eval(final EvolutionState state,
                     final int thread,
                     final GPData input,
                     final ADFStack stack,
                     final GPIndividual individual,
                     final Problem problem) {
        DoubleData rd = ((DoubleData) (input));
        //we first check the right hand node which is the denominator
        children[1].eval(state, thread, input, stack, individual, problem);
        // if the denominator is zero then return the result as 1
        if (rd.x == 0) rd.x = 1;
        else {
            double result;
            result = rd.x;
            //then we evaluate the left hand child and return the result which is the left child
            // div by the right hand child
            children[0].eval(state, thread, input, stack, individual, problem);
            rd.x = rd.x / result;
        }
    }
}