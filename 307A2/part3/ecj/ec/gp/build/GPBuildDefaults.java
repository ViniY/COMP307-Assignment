/*
  Copyright 2006 by Sean Luke
  Licensed under the Academic Free License version 3.0
  See the file "LICENSE" for more information
*/


package ec.gp.build;

import ec.DefaultsForm;
import ec.gp.GPDefaults;
import ec.util.Parameter;

/*
 * GPBuildDefaults.java
 *
 * Created: Thu Jan 20 17:22:22 2000
 * By: Sean Luke
 */

/**
 * @author Sean Luke
 * @version 1.0
 */

public class GPBuildDefaults implements DefaultsForm {
    public static final String P_BUILD = "build";

    /**
     * Returns the default base.
     */
    public static final Parameter base() {
        return GPDefaults.base().push(P_BUILD);
    }
}
