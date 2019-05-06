/*
  Copyright 2006 by Sean Luke
  Licensed under the Academic Free License version 3.0
  See the file "LICENSE" for more information
*/


package ec.app.twobox.func;

import ec.EvolutionState;
import ec.Problem;
import ec.app.twobox.TwoBoxData;
import ec.gp.ADFStack;
import ec.gp.GPData;
import ec.gp.GPIndividual;
import ec.gp.GPNode;

/*
 * Add.java
 *
 * Created: Wed Nov  3 18:26:37 1999
 * By: Sean Luke
 */

/**
 * @author Sean Luke
 * @version 1.0
 */

public class Add extends GPNode {
    public String toString() {
        return "+";
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
        double result;
        TwoBoxData rd = ((TwoBoxData) (input));

        children[0].eval(state, thread, input, stack, individual, problem);
        result = rd.x;

        children[1].eval(state, thread, input, stack, individual, problem);
        rd.x = result + rd.x;
    }
}



