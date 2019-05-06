/*
  Copyright 2012 by James McDermott
  Licensed under the Academic Free License version 3.0
  See the file "LICENSE" for more information
*/


package ec.app.ordertree.func;

import ec.EvolutionState;
import ec.Problem;
import ec.gp.ADFStack;
import ec.gp.GPData;
import ec.gp.GPIndividual;
import ec.gp.GPNode;

/*
 * OrderTreeNode.java
 *
 */

/**
 * @author James McDermott
 */

public abstract class OrderTreeNode extends GPNode {
    public abstract int value();

    public String toString() {
        return "" + value();
    }

    public void eval(final EvolutionState state,
                     final int thread,
                     final GPData input,
                     final ADFStack stack,
                     final GPIndividual individual,
                     final Problem problem) {
        // no need to do anything here
    }
}
