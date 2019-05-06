/*
  Copyright 2006 by Sean Luke
  Licensed under the Academic Free License version 3.0
  See the file "LICENSE" for more information
*/


/*
 * Created on Apr 17, 2005 8:30:36 PM
 *
 * By: spaus
 */
package ec.display.portrayal;

import ec.EvolutionState;
import ec.Individual;
import ec.Setup;

import javax.swing.*;
import java.awt.*;

/**
 * @author spaus
 */
public abstract class IndividualPortrayal
        extends JPanel
        implements Setup {
    IndividualPortrayal(LayoutManager layout) {
        super(layout);
    }

    public abstract void portrayIndividual(EvolutionState state, Individual individual);
}
