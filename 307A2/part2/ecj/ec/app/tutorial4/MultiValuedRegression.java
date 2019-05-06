/*
  Copyright 2006 by Sean Luke
  Licensed under the Academic Free License version 3.0
  See the file "LICENSE" for more information
*/


package ec.app.tutorial4;
import ec.util.*;
import ec.*;
import ec.gp.*;
import ec.gp.koza.*;
import ec.simple.*;

public class MultiValuedRegression extends GPProblem implements SimpleProblemForm
    {
    private static final long serialVersionUID = 1;

    public double currentX;
//    public double currentY;
    public double[] Y =  {37.00000, 24.16016, 15.06250, 8.91016, 5.00000, 2.72266, 1.56250,
        1.09766, 1.00000, 1.03516, 1.06250, 1.03516, 1.00000, 1.09766, 1.56250,
        2.72266, 5.00000, 8.91016, 15.06250, 24.16016};

    public void setup(final EvolutionState state,
        final Parameter base)
        {
        super.setup(state, base);
        
        // verify our input is the right class (or subclasses from it)
        if (!(input instanceof DoubleData))
            state.output.fatal("GPData class must subclass from " + DoubleData.class,
                base.push(P_DATA), null);
        }
        
    public void evaluate(final EvolutionState state, 
        final Individual ind, 
        final int subpopulation,
        final int threadnum)
        {
        if (!ind.evaluated)  // don't bother reevaluating
            {
            DoubleData input = (DoubleData)(this.input);
        
            int hits = 0;
            double sum = 0.0;
            double expectedResult;
            double result;
            int length = this.Y.length;
            for (int y=0;y<length;y++)
                {
//                currentX = state.random[threadnum].nextDouble();
//                currentY = state.random[threadnum].nextDouble();
                    currentX = -2 + 0.25 * y;
                    expectedResult = Y[y];
//                expectedResult = currentX*currentX*currentY + currentX*currentY + currentY;
                ((GPIndividual)ind).trees[0].child.eval(
                    state,threadnum,input,stack,((GPIndividual)ind),this);

//                result = Math.abs(expectedResult - input.x);
                  result = Math.pow((expectedResult - input.x),2) /20;
                if (result <= 0.005) hits++;
                sum += result;                  
                }

            // the fitness better be KozaFitness!
            KozaFitness f = ((KozaFitness)ind.fitness);
            f.setStandardizedFitness(state, sum);
            f.hits = hits;
            ind.evaluated = true;
            }
        }
    }

