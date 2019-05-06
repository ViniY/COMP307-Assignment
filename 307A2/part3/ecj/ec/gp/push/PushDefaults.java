
package ec.gp.push;

import ec.DefaultsForm;
import ec.util.Parameter;

public final class PushDefaults implements DefaultsForm {
    public static final String P_PUSH = "push";

    /**
     * Returns the default base.
     */
    public static final Parameter base() {
        return new Parameter(P_PUSH);
    }
}
