package ec.app.push;

import ec.gp.push.PushInstruction;
import org.spiderland.Psh.Interpreter;
import org.spiderland.Psh.floatStack;

public class Atan extends PushInstruction {
    public void Execute(Interpreter interpeter) {
        floatStack stack = interpeter.floatStack();

        if (stack.size() >= 1) {
            // we're good
            float slope = stack.pop();
            stack.push((float) Math.atan(slope));
        } else stack.push(0);
    }
}
