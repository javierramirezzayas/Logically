from logically_exe.logic_gate_modules import logicGateModules


def initDrawSchematic():
    return logicGateModules()


def rec_draw(s, ckt_list, lginput_xy=[], first=True, lsfactor=6.0):
    inputs = []
    stack = ckt_list
    while stack:
        out_lbl = "\n" + stack[0]
        lgatetype = stack[1]
        inputs = stack[2]
        Q = determineGate(s, first, inputs, lgatetype, out_lbl, lsfactor, lginput_xy)
        first = False
        for e in range(0, len(inputs)):
            if isinstance(inputs[e], list):
                rec_draw(s, inputs[e], Q[e], False, lsfactor/2.5)
            if e == len(inputs)-1:
                return inputs

def determineGate(s, first, inputs, lgatetype, out_lbl, lsfactor, lginput_xy):
    if first:
        if len(inputs) == 1:
            if isinstance(inputs[0], list):
                return determineGateType(s, lgatetype, out_lbl, lsfactor, False, 0, in_qty=1)
            else: # isinstance(inputs[0], str)
                return determineGateType(s, lgatetype, out_lbl, lsfactor, False, 0, in_qty=1, in1=inputs[0])
        elif len(inputs) == 2:
            if all(isinstance(x, list) for x in inputs):
                return determineGateType(s, lgatetype, out_lbl, lsfactor, False, 0, in_qty=2)
            elif all(isinstance(x, str) for x in inputs):
                return determineGateType(s, lgatetype, out_lbl, lsfactor, False, 0, in_qty=2, in1=inputs[0], in2=inputs[1])
            elif isinstance(inputs[0], str):
                return determineGateType(s, lgatetype, out_lbl, lsfactor, False, 0, in_qty=2, in1=inputs[0])
            elif isinstance(inputs[1], str):
                return determineGateType(s, lgatetype, out_lbl, lsfactor, False, 0, in_qty=2, in2=inputs[1])
        elif len(inputs) == 3:
            if all(isinstance(x, list) for x in inputs):
                return determineGateType(s, lgatetype, out_lbl, lsfactor, False, 0, in_qty=3)
            elif all(isinstance(x, str) for x in inputs):
                return determineGateType(s, lgatetype, out_lbl, lsfactor, False, 0, in_qty=3, in1=inputs[0], in2=inputs[1], in3=inputs[2])
            elif isinstance(inputs[0], str) and isinstance(inputs[1], str):
                return determineGateType(s, lgatetype, out_lbl, lsfactor, False, 0, in_qty=3, in1=inputs[0], in2=inputs[1])
            elif isinstance(inputs[1], str) and isinstance(inputs[2], str):
                return determineGateType(s, lgatetype, out_lbl, lsfactor, False, 0, in_qty=3, in2=inputs[1], in3=inputs[2])
            elif isinstance(inputs[0], str) and isinstance(inputs[2], str):
                return determineGateType(s, lgatetype, out_lbl, lsfactor, False, 0, in_qty=3, in1=inputs[0], in3=inputs[2])
            elif isinstance(inputs[0], str):
                return determineGateType(s, lgatetype, out_lbl, lsfactor, False, 0, in_qty=3, in1=inputs[0])
            elif isinstance(inputs[1], str):
                return determineGateType(s, lgatetype, out_lbl, lsfactor, False, 0, in_qty=3, in2=inputs[1])
            elif isinstance(inputs[2], str):
                return determineGateType(s, lgatetype, out_lbl, lsfactor, False, 0, in_qty=3, in3=inputs[2])
    else:
        if len(inputs) == 1:
            if isinstance(inputs[0], list):
                return determineGateType(s, lgatetype, out_lbl, lsfactor, True, lginput_xy, in_qty=1)
            else: # isinstance(inputs[0], str)
                return determineGateType(s, lgatetype, out_lbl, lsfactor, True, lginput_xy, in_qty=1, in1=inputs[0])
        elif len(inputs) == 2:
            if all(isinstance(x, list) for x in inputs):
                return determineGateType(s, lgatetype, out_lbl, lsfactor, True, lginput_xy, in_qty=2)
            elif all(isinstance(x, str) for x in inputs):
                return determineGateType(s, lgatetype, out_lbl, lsfactor, True, lginput_xy, in_qty=2, in1=inputs[0], in2=inputs[1])
            elif isinstance(inputs[0], str):
                return determineGateType(s, lgatetype, out_lbl, lsfactor, True, lginput_xy, in_qty=2, in2=inputs[0])
            elif isinstance(inputs[1], str):
                return determineGateType(s, lgatetype, out_lbl, lsfactor, True, lginput_xy, in_qty=2, in1=inputs[1])
        elif len(inputs) == 3:
            if all(isinstance(x, list) for x in inputs):
                return determineGateType(s, lgatetype, out_lbl, lsfactor, True, lginput_xy, in_qty=3)
            elif all(isinstance(x, str) for x in inputs):
                return determineGateType(s, lgatetype, out_lbl, lsfactor, True, lginput_xy, in_qty=3, in1=inputs[0], in2=inputs[1], in3=inputs[2])
            elif isinstance(inputs[0], str) and isinstance(inputs[1], str):
                return determineGateType(s, lgatetype, out_lbl, lsfactor, True, lginput_xy, in_qty=3, in3=inputs[0], in2=inputs[1])
            elif isinstance(inputs[1], str) and isinstance(inputs[2], str):
                return determineGateType(s, lgatetype, out_lbl, lsfactor, True, lginput_xy, in_qty=3, in2=inputs[1], in1=inputs[2])
            elif isinstance(inputs[0], str) and isinstance(inputs[2], str):
                return determineGateType(s, lgatetype, out_lbl, lsfactor, True, lginput_xy, in_qty=3, in3=inputs[0], in1=inputs[2])
            elif isinstance(inputs[0], str):
                return determineGateType(s, lgatetype, out_lbl, lsfactor, True, lginput_xy, in_qty=3, in3=inputs[0])
            elif isinstance(inputs[1], str):
                return determineGateType(s, lgatetype, out_lbl, lsfactor, True, lginput_xy, in_qty=3, in2=inputs[1])
            elif isinstance(inputs[2], str):
                return determineGateType(s, lgatetype, out_lbl, lsfactor, True, lginput_xy, in_qty=3, in1=inputs[2])



def determineGateType(s, gate, out_label,depth, reverse, connectTo, in_qty=2, in1='', in2='', in3=''):
    if in_qty == 1:
        if gate == 'NOT':
            return s.addNOT(out_lbl=out_label, in1_lbl=in1, connectTo=connectTo, reverse=reverse)
        elif gate == 'BUFFER':
            return s.addBUFFER(out_lbl=out_label, in1_lbl=in1, connectTo=connectTo, reverse=reverse)
    elif in_qty == 2:
        if gate == 'XOR':
            return s.addXOR2(out_lbl=out_label, in1_lbl=in1, in2_lbl=in2, connectTo=connectTo, depth=depth, reverse=reverse)
        elif gate == 'XNOR':
            return s.addXNOR2(out_lbl=out_label, in1_lbl=in1, in2_lbl=in2, connectTo=connectTo, depth=depth, reverse=reverse)
        elif gate == 'AND':
            return s.addAND2(out_lbl=out_label, in1_lbl=in1, in2_lbl=in2, connectTo=connectTo, depth=depth, reverse=reverse)
        elif gate == 'NAND':
            return s.addNAND2(out_lbl=out_label, in1_lbl=in1, in2_lbl=in2, connectTo=connectTo, depth=depth, reverse=reverse)
        elif gate == 'OR':
            return s.addOR2(out_lbl=out_label, in1_lbl=in1, in2_lbl=in2, connectTo=connectTo, depth=depth, reverse=reverse)
        elif gate == 'NOR':
            return s.addNOR2(out_lbl=out_label, in1_lbl=in1, in2_lbl=in2, connectTo=connectTo, depth=depth, reverse=reverse)
    elif in_qty == 3:
        if gate == 'XOR':
            return s.addXOR3(out_lbl=out_label, in1_lbl=in1, in2_lbl=in2, in3_lbl=in3, connectTo=connectTo, depth=depth, reverse=reverse)
        elif gate == 'XNOR':
            return s.addXNOR3(out_lbl=out_label, in1_lbl=in1, in2_lbl=in2, in3_lbl=in3, connectTo=connectTo, depth=depth, reverse=reverse)
        elif gate == 'AND':
            return s.addAND3(out_lbl=out_label, in1_lbl=in1, in2_lbl=in2, in3_lbl=in3, connectTo=connectTo, depth=depth, reverse=reverse)
        elif gate == 'NAND':
            return s.addNAND3(out_lbl=out_label, in1_lbl=in1, in2_lbl=in2, in3_lbl=in3, connectTo=connectTo, depth=depth, reverse=reverse)
        elif gate == 'OR':
            return s.addOR3(out_lbl=out_label, in1_lbl=in1, in2_lbl=in2, in3_lbl=in3, connectTo=connectTo, depth=depth, reverse=reverse)
        elif gate == 'NOR':
            return s.addNOR3(out_lbl=out_label, in1_lbl=in1, in2_lbl=in2, in3_lbl=in3, connectTo=connectTo, depth=depth, reverse=reverse)

def drawSchematic(s):
    s.drawSchematic()
