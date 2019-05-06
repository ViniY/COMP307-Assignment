/*
  Copyright 2013 by Sean Luke
  Licensed under the Academic Free License version 3.0
  See the file "LICENSE" for more information
*/

package ec.app.majority.func;

import ec.EvolutionState;
import ec.Problem;
import ec.app.majority.MajorityData;
import ec.gp.ADFStack;
import ec.gp.GPData;
import ec.gp.GPIndividual;
import ec.gp.GPNode;

public class Nand extends GPNode {
    public String toString() {
        return "nand";
    }

    public int expectedChildren() {
        return 2;
    }

    public void eval(final EvolutionState state,
                     final int thread,
                     final GPData input,
                     final ADFStack stack,
                     final GPIndividual individual,
                     final Problem problem) {
        children[0].eval(state, thread, input, stack, individual, problem);

        MajorityData md = (MajorityData) input;
        long y0 = md.data0;
        long y1 = md.data1;

        children[1].eval(state, thread, input, stack, individual, problem);

        md.data0 = ~(md.data0 & y0);
        md.data1 = ~(md.data1 & y1);
    }
}



