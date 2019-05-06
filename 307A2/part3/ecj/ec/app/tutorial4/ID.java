/*
  Copyright 2006 by Sean Luke
  Licensed under the Academic Free License version 3.0
  See the file "LICENSE" for more information
*/


package ec.app.tutorial4;

import ec.EvolutionState;
import ec.Problem;
import ec.app.regression.Benchmarks;
import ec.gp.ADFStack;
import ec.gp.GPData;
import ec.gp.GPIndividual;
import ec.gp.GPNode;

/*
 * X.java
 *
 * Created: Wed Nov  3 18:26:37 1999
 * By: Sean Luke
 */

/**
 * @author Sean Luke
 * @version 1.0
 */

public class ID extends GPNode {
    public String toString() {
        return "ID";
    }

    /*
      public void checkConstraints(final EvolutionState state,
      final int tree,
      final GPIndividual typicalIndividual,
      final Parameter individualBase)
      {
      super.checkConstraints(state,tree,typicalIndividual,individualBase);
      if (children.length!=0)
      state.output.error("Incorrect number of children for node " +
      toStringForError() + " at " +
      individualBase);
      }
    */
    public int expectedChildren() {
        return 0;
    }

    public void eval(final EvolutionState state,
                     final int thread,
                     final GPData input,
                     final ADFStack stack,
                     final GPIndividual individual,
                     final Problem problem) {
        DoubleData rd = ((DoubleData) (input));
        double[] c = ((Benchmarks) problem).currentValue;
        if (c.length >= 5)
            rd.x = ((Benchmarks) problem).currentValue[4];
        else rd.x = 0;
    }
}



