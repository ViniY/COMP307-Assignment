/*
  Copyright 2012 by Luca Manzoni
  Licensed under the Academic Free License version 3.0
  See the file "LICENSE" for more information
*/

package ec.app.klandscapes.func;

import ec.EvolutionState;
import ec.Problem;
import ec.gp.ADFStack;
import ec.gp.GPData;
import ec.gp.GPIndividual;
import ec.gp.GPNode;

public abstract class KLandscapeTree extends GPNode {
    public abstract char value();

    public String toString() {
        return "" + value();
    }

    public void eval(final EvolutionState state,
                     final int thread,
                     final GPData input,
                     final ADFStack stack,
                     final GPIndividual individual,
                     final Problem problem) {
    }
}
