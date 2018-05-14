import SchemDraw as schem
import SchemDraw.elements as e
import SchemDraw.logic as l

class logicGateModules:

    def __init__(self):
        self.d = schem.Drawing(unit=.5)

    def addOR2(self, in1_lbl='', in2_lbl='', out_lbl='', reverse=False, depth=2, connectTo=0):
        if reverse:
            S = self.d.add(l.OR2, rgtlabel=out_lbl, reverse=True, xy=connectTo)
            l1 = self.d.add(e.LINE, d="down", xy=S.in1, l=(self.d.unit * depth))
            l2 = self.d.add(e.LINE, d="up", xy=S.in2, l=(self.d.unit * depth))
            l3 = self.d.add(e.LINE, d="left", xy=l1.end, l=(self.d.unit * depth), lftlabel=in1_lbl)
            l4 = self.d.add(e.LINE, d="left", xy=l2.end, l=(self.d.unit * depth), lftlabel=in2_lbl)
            return [l4.end, l3.end]
        else:
            S = self.d.add(l.OR2, rgtlabel=out_lbl, xy=connectTo)
            l1 = self.d.add(e.LINE, d="up", xy=S.in1, l=(self.d.unit * depth))
            l2 = self.d.add(e.LINE, d="down", xy=S.in2, l=(self.d.unit * depth))
            l3 = self.d.add(e.LINE, d="left", xy=l1.end, l=(self.d.unit * depth), lftlabel=in1_lbl)
            l4 = self.d.add(e.LINE, d="left", xy=l2.end, l=(self.d.unit * depth), lftlabel=in2_lbl)
            return [l3.end, l4.end]

    def addOR3(self, in1_lbl='', in2_lbl='', in3_lbl='', out_lbl='', reverse=False, depth=2, connectTo=0):
        if reverse:
            S = self.d.add(l.OR3, rgtlabel=out_lbl, reverse=True, xy=connectTo)
            l1 = self.d.add(e.LINE, d="down", xy=S.in1, l=(self.d.unit * depth * 1.75))
            l2 = self.d.add(e.LINE, d="left", xy=S.in2, l=(self.d.unit * depth), lftlabel=in2_lbl)
            l3 = self.d.add(e.LINE, d="up", xy=S.in3, l=(self.d.unit * depth * 1.75))
            l4 = self.d.add(e.LINE, d="left", xy=l1.end, l=(self.d.unit * depth), lftlabel=in1_lbl)
            # l5 = self.d.add(e.LINE, d="left", xy=l2.end, l=(self.d.unit * depth), lftlabel=in2_lbl)
            l6 = self.d.add(e.LINE, d="left", xy=l3.end, l=(self.d.unit * depth), lftlabel=in3_lbl)
            return [l6.end, l2.end, l4.end]
        else:
            S = self.d.add(l.OR3, rgtlabel=out_lbl, xy=connectTo)
            l1 = self.d.add(e.LINE, d="up", xy=S.in1, l=(self.d.unit * depth * 1.75))
            l2 = self.d.add(e.LINE, d="left", xy=S.in2, l=(self.d.unit * depth), lftlabel=in2_lbl)
            l3 = self.d.add(e.LINE, d="down", xy=S.in3, l=(self.d.unit * depth *1.75))
            l4 = self.d.add(e.LINE, d="left", xy=l1.end, l=(self.d.unit * depth), lftlabel=in1_lbl)
            # l5 = self.d.add(e.LINE, d="left", xy=l2.end, l=(self.d.unit * depth), lftlabel=in2_lbl)
            l6 = self.d.add(e.LINE, d="left", xy=l3.end, l=(self.d.unit * depth), lftlabel=in3_lbl)
            return [l4.end, l2.end, l6.end]

    def addNOR2(self, in1_lbl='', in2_lbl='', out_lbl='', reverse=False, depth=2, connectTo=0):
        if reverse:
            S = self.d.add(l.NOR2, rgtlabel=out_lbl, reverse=True, xy=connectTo)
            l1 = self.d.add(e.LINE, d="down", xy=S.in1, l=(self.d.unit * depth))
            l2 = self.d.add(e.LINE, d="up", xy=S.in2, l=(self.d.unit * depth))
            l3 = self.d.add(e.LINE, d="left", xy=l1.end, l=(self.d.unit * depth), lftlabel=in1_lbl)
            l4 = self.d.add(e.LINE, d="left", xy=l2.end, l=(self.d.unit * depth), lftlabel=in2_lbl)
            return [l4.end, l3.end]
        else:
            S = self.d.add(l.NOR2, rgtlabel=out_lbl, xy=connectTo)
            l1 = self.d.add(e.LINE, d="up", xy=S.in1, l=(self.d.unit * depth))
            l2 = self.d.add(e.LINE, d="down", xy=S.in2, l=(self.d.unit * depth))
            l3 = self.d.add(e.LINE, d="left", xy=l1.end, l=(self.d.unit * depth), lftlabel=in1_lbl)
            l4 = self.d.add(e.LINE, d="left", xy=l2.end, l=(self.d.unit * depth), lftlabel=in2_lbl)
            return [l3.end, l4.end]

    def addNOR3(self, in1_lbl='', in2_lbl='', in3_lbl='', out_lbl='', reverse=False, depth=2, connectTo=0):
        if reverse:
            S = self.d.add(l.NOR3, rgtlabel=out_lbl, reverse=True, xy=connectTo)
            l1 = self.d.add(e.LINE, d="down", xy=S.in1, l=(self.d.unit * depth * 1.75))
            l2 = self.d.add(e.LINE, d="left", xy=S.in2, l=(self.d.unit * depth), lftlabel=in2_lbl)
            l3 = self.d.add(e.LINE, d="up", xy=S.in3, l=(self.d.unit * depth * 1.75))
            l4 = self.d.add(e.LINE, d="left", xy=l1.end, l=(self.d.unit * depth), lftlabel=in1_lbl)
            # l5 = self.d.add(e.LINE, d="left", xy=l2.end, l=(self.d.unit * depth), lftlabel=in2_lbl)
            l6 = self.d.add(e.LINE, d="left", xy=l3.end, l=(self.d.unit * depth), lftlabel=in3_lbl)
            return [l6.end, l2.end, l4.end]
        else:
            S = self.d.add(l.NOR3, rgtlabel=out_lbl, xy=connectTo)
            l1 = self.d.add(e.LINE, d="up", xy=S.in1, l=(self.d.unit * depth * 1.75))
            l2 = self.d.add(e.LINE, d="left", xy=S.in2, l=(self.d.unit * depth), lftlabel=in2_lbl)
            l3 = self.d.add(e.LINE, d="down", xy=S.in3, l=(self.d.unit * depth *1.75))
            l4 = self.d.add(e.LINE, d="left", xy=l1.end, l=(self.d.unit * depth), lftlabel=in1_lbl)
            # l5 = self.d.add(e.LINE, d="left", xy=l2.end, l=(self.d.unit * depth), lftlabel=in2_lbl)
            l6 = self.d.add(e.LINE, d="left", xy=l3.end, l=(self.d.unit * depth), lftlabel=in3_lbl)
            return [l4.end, l2.end, l6.end]

    def addXOR2(self, in1_lbl='', in2_lbl='', out_lbl = '', reverse = False, depth = 2, connectTo = 0):
        if reverse:
            S = self.d.add(l.XOR2, rgtlabel=out_lbl, reverse=True, xy=connectTo)
            l1 = self.d.add(e.LINE, d="down", xy=S.in1, l=(self.d.unit * depth))
            l2 = self.d.add(e.LINE, d="up", xy=S.in2, l=(self.d.unit * depth))
            l3 = self.d.add(e.LINE, d="left", xy=l1.end, l=(self.d.unit * depth), lftlabel=in1_lbl)
            l4 = self.d.add(e.LINE, d="left", xy=l2.end, l=(self.d.unit * depth), lftlabel=in2_lbl)
            return [l4.end, l3.end]
        else:
            S = self.d.add(l.XOR2, rgtlabel=out_lbl, xy=connectTo)
            l1 = self.d.add(e.LINE, d="up", xy=S.in1, l=(self.d.unit * depth))
            l2 = self.d.add(e.LINE, d="down", xy=S.in2, l=(self.d.unit * depth))
            l3 = self.d.add(e.LINE, d="left", xy=l1.end, l=(self.d.unit * depth), lftlabel=in1_lbl)
            l4 = self.d.add(e.LINE, d="left", xy=l2.end, l=(self.d.unit * depth), lftlabel=in2_lbl)
            return [l3.end, l4.end]

    def addXOR3(self, in1_lbl='', in2_lbl='', in3_lbl='', out_lbl='', reverse=False, depth=2, connectTo=0):
        if reverse:
            S = self.d.add(l.XOR3, rgtlabel=out_lbl, reverse=True, xy=connectTo)
            l1 = self.d.add(e.LINE, d="down", xy=S.in1, l=(self.d.unit * depth * 1.75))
            l2 = self.d.add(e.LINE, d="left", xy=S.in2, l=(self.d.unit * depth), lftlabel=in2_lbl)
            l3 = self.d.add(e.LINE, d="up", xy=S.in3, l=(self.d.unit * depth * 1.75))
            l4 = self.d.add(e.LINE, d="left", xy=l1.end, l=(self.d.unit * depth), lftlabel=in1_lbl)
            # l5 = self.d.add(e.LINE, d="left", xy=l2.end, l=(self.d.unit * depth), lftlabel=in2_lbl)
            l6 = self.d.add(e.LINE, d="left", xy=l3.end, l=(self.d.unit * depth), lftlabel=in3_lbl)
            return [l6.end, l2.end, l4.end]
        else:
            S = self.d.add(l.XOR3, rgtlabel=out_lbl, xy=connectTo)
            l1 = self.d.add(e.LINE, d="up", xy=S.in1, l=(self.d.unit * depth * 1.75))
            l2 = self.d.add(e.LINE, d="left", xy=S.in2, l=(self.d.unit * depth), lftlabel=in2_lbl)
            l3 = self.d.add(e.LINE, d="down", xy=S.in3, l=(self.d.unit * depth *1.75))
            l4 = self.d.add(e.LINE, d="left", xy=l1.end, l=(self.d.unit * depth), lftlabel=in1_lbl)
            # l5 = self.d.add(e.LINE, d="left", xy=l2.end, l=(self.d.unit * depth), lftlabel=in2_lbl)
            l6 = self.d.add(e.LINE, d="left", xy=l3.end, l=(self.d.unit * depth), lftlabel=in3_lbl)
            return [l4.end, l2.end, l6.end]

    def addXNOR2(self, in1_lbl='', in2_lbl='', out_lbl = '', reverse = False, depth = 2, connectTo = 0):
        if reverse:
            S = self.d.add(l.XNOR2, rgtlabel=out_lbl, reverse=True, xy=connectTo)
            l1 = self.d.add(e.LINE, d="down", xy=S.in1, l=(self.d.unit * depth))
            l2 = self.d.add(e.LINE, d="up", xy=S.in2, l=(self.d.unit * depth))
            l3 = self.d.add(e.LINE, d="left", xy=l1.end, l=(self.d.unit * depth), lftlabel=in1_lbl)
            l4 = self.d.add(e.LINE, d="left", xy=l2.end, l=(self.d.unit * depth), lftlabel=in2_lbl)
            return [l4.end, l3.end]
        else:
            S = self.d.add(l.XNOR2, rgtlabel=out_lbl, xy=connectTo)
            l1 = self.d.add(e.LINE, d="up", xy=S.in1, l=(self.d.unit * depth))
            l2 = self.d.add(e.LINE, d="down", xy=S.in2, l=(self.d.unit * depth))
            l3 = self.d.add(e.LINE, d="left", xy=l1.end, l=(self.d.unit * depth), lftlabel=in1_lbl)
            l4 = self.d.add(e.LINE, d="left", xy=l2.end, l=(self.d.unit * depth), lftlabel=in2_lbl)
            return [l3.end, l4.end]

    def addXNOR3(self, in1_lbl='', in2_lbl='', in3_lbl='', out_lbl='', reverse=False, depth=2, connectTo=0):
        if reverse:
            S = self.d.add(l.XNOR3, rgtlabel=out_lbl, reverse=True, xy=connectTo)
            l1 = self.d.add(e.LINE, d="down", xy=S.in1, l=(self.d.unit * depth * 1.75))
            l2 = self.d.add(e.LINE, d="left", xy=S.in2, l=(self.d.unit * depth), lftlabel=in2_lbl)
            l3 = self.d.add(e.LINE, d="up", xy=S.in3, l=(self.d.unit * depth * 1.75))
            l4 = self.d.add(e.LINE, d="left", xy=l1.end, l=(self.d.unit * depth), lftlabel=in1_lbl)
            # l5 = self.d.add(e.LINE, d="left", xy=l2.end, l=(self.d.unit * depth), lftlabel=in2_lbl)
            l6 = self.d.add(e.LINE, d="left", xy=l3.end, l=(self.d.unit * depth), lftlabel=in3_lbl)
            return [l6.end, l2.end, l4.end]
        else:
            S = self.d.add(l.XNOR3, rgtlabel=out_lbl, xy=connectTo)
            l1 = self.d.add(e.LINE, d="up", xy=S.in1, l=(self.d.unit * depth * 1.75))
            l2 = self.d.add(e.LINE, d="left", xy=S.in2, l=(self.d.unit * depth), lftlabel=in2_lbl)
            l3 = self.d.add(e.LINE, d="down", xy=S.in3, l=(self.d.unit * depth *1.75))
            l4 = self.d.add(e.LINE, d="left", xy=l1.end, l=(self.d.unit * depth), lftlabel=in1_lbl)
            # l5 = self.d.add(e.LINE, d="left", xy=l2.end, l=(self.d.unit * depth), lftlabel=in2_lbl)
            l6 = self.d.add(e.LINE, d="left", xy=l3.end, l=(self.d.unit * depth), lftlabel=in3_lbl)
            return [l4.end, l2.end, l6.end]

    def addAND2(self, in1_lbl='', in2_lbl='', out_lbl = '', reverse = False, depth = 2, connectTo = 0):
        if reverse:
            S = self.d.add(l.AND2, rgtlabel=out_lbl, reverse=True, xy=connectTo)
            l1 = self.d.add(e.LINE, d="down", xy=S.in1, l=(self.d.unit * depth))
            l2 = self.d.add(e.LINE, d="up", xy=S.in2, l=(self.d.unit * depth))
            l3 = self.d.add(e.LINE, d="left", xy=l1.end, l=(self.d.unit * depth), lftlabel=in1_lbl)
            l4 = self.d.add(e.LINE, d="left", xy=l2.end, l=(self.d.unit * depth), lftlabel=in2_lbl)
            return [l4.end, l3.end]
        else:
            S = self.d.add(l.AND2, rgtlabel=out_lbl, xy=connectTo)
            l1 = self.d.add(e.LINE, d="up", xy=S.in1, l=(self.d.unit * depth))
            l2 = self.d.add(e.LINE, d="down", xy=S.in2, l=(self.d.unit * depth))
            l3 = self.d.add(e.LINE, d="left", xy=l1.end, l=(self.d.unit * depth), lftlabel=in1_lbl)
            l4 = self.d.add(e.LINE, d="left", xy=l2.end, l=(self.d.unit * depth), lftlabel=in2_lbl)
            return [l3.end, l4.end]

    def addAND3(self, in1_lbl='', in2_lbl='', in3_lbl='', out_lbl='', reverse=False, depth=2, connectTo=0):
        if reverse:
            S = self.d.add(l.AND3, rgtlabel=out_lbl, reverse=True, xy=connectTo)
            l1 = self.d.add(e.LINE, d="down", xy=S.in1, l=(self.d.unit * depth * 1.75))
            l2 = self.d.add(e.LINE, d="left", xy=S.in2, l=(self.d.unit * depth), lftlabel=in2_lbl)
            l3 = self.d.add(e.LINE, d="up", xy=S.in3, l=(self.d.unit * depth * 1.75))
            l4 = self.d.add(e.LINE, d="left", xy=l1.end, l=(self.d.unit * depth), lftlabel=in1_lbl)
            # l5 = self.d.add(e.LINE, d="left", xy=l2.end, l=(self.d.unit * depth), lftlabel=in2_lbl)
            l6 = self.d.add(e.LINE, d="left", xy=l3.end, l=(self.d.unit * depth), lftlabel=in3_lbl)
            return [l6.end, l2.end, l4.end]
        else:
            S = self.d.add(l.AND3, rgtlabel=out_lbl, xy=connectTo)
            l1 = self.d.add(e.LINE, d="up", xy=S.in1, l=(self.d.unit * depth * 1.75))
            l2 = self.d.add(e.LINE, d="left", xy=S.in2, l=(self.d.unit * depth), lftlabel=in2_lbl)
            l3 = self.d.add(e.LINE, d="down", xy=S.in3, l=(self.d.unit * depth *1.75))
            l4 = self.d.add(e.LINE, d="left", xy=l1.end, l=(self.d.unit * depth), lftlabel=in1_lbl)
            # l5 = self.d.add(e.LINE, d="left", xy=l2.end, l=(self.d.unit * depth), lftlabel=in2_lbl)
            l6 = self.d.add(e.LINE, d="left", xy=l3.end, l=(self.d.unit * depth), lftlabel=in3_lbl)
            return [l4.end, l2.end, l6.end]

    def addNAND2(self, in1_lbl='', in2_lbl='', out_lbl = '', reverse = False, depth = 2, connectTo = 0):
        if reverse:
            S = self.d.add(l.NAND2, rgtlabel=out_lbl, reverse=True, xy=connectTo)
            l1 = self.d.add(e.LINE, d="down", xy=S.in1, l=(self.d.unit * depth))
            l2 = self.d.add(e.LINE, d="up", xy=S.in2, l=(self.d.unit * depth))
            l3 = self.d.add(e.LINE, d="left", xy=l1.end, l=(self.d.unit * depth), lftlabel=in1_lbl)
            l4 = self.d.add(e.LINE, d="left", xy=l2.end, l=(self.d.unit * depth), lftlabel=in2_lbl)
            return [l4.end, l3.end]
        else:
            S = self.d.add(l.NAND2, rgtlabel=out_lbl, xy=connectTo)
            l1 = self.d.add(e.LINE, d="up", xy=S.in1, l=(self.d.unit * depth))
            l2 = self.d.add(e.LINE, d="down", xy=S.in2, l=(self.d.unit * depth))
            l3 = self.d.add(e.LINE, d="left", xy=l1.end, l=(self.d.unit * depth), lftlabel=in1_lbl)
            l4 = self.d.add(e.LINE, d="left", xy=l2.end, l=(self.d.unit * depth), lftlabel=in2_lbl)
            return [l3.end, l4.end]

    def addNAND3(self, in1_lbl='', in2_lbl='', in3_lbl='', out_lbl='', reverse=False, depth=2, connectTo=0):
        if reverse:
            S = self.d.add(l.NAND3, rgtlabel=out_lbl, reverse=True, xy=connectTo)
            l1 = self.d.add(e.LINE, d="down", xy=S.in1, l=(self.d.unit * depth * 1.75))
            l2 = self.d.add(e.LINE, d="left", xy=S.in2, l=(self.d.unit * depth), lftlabel=in2_lbl)
            l3 = self.d.add(e.LINE, d="up", xy=S.in3, l=(self.d.unit * depth * 1.75))
            l4 = self.d.add(e.LINE, d="left", xy=l1.end, l=(self.d.unit * depth), lftlabel=in1_lbl)
            # l5 = self.d.add(e.LINE, d="left", xy=l2.end, l=(self.d.unit * depth), lftlabel=in2_lbl)
            l6 = self.d.add(e.LINE, d="left", xy=l3.end, l=(self.d.unit * depth), lftlabel=in3_lbl)
            return [l6.end, l2.end, l4.end]
        else:
            S = self.d.add(l.NAND3, rgtlabel=out_lbl, xy=connectTo)
            l1 = self.d.add(e.LINE, d="up", xy=S.in1, l=(self.d.unit * depth * 1.75))
            l2 = self.d.add(e.LINE, d="left", xy=S.in2, l=(self.d.unit * depth), lftlabel=in2_lbl)
            l3 = self.d.add(e.LINE, d="down", xy=S.in3, l=(self.d.unit * depth *1.75))
            l4 = self.d.add(e.LINE, d="left", xy=l1.end, l=(self.d.unit * depth), lftlabel=in1_lbl)
            # l5 = self.d.add(e.LINE, d="left", xy=l2.end, l=(self.d.unit * depth), lftlabel=in2_lbl)
            l6 = self.d.add(e.LINE, d="left", xy=l3.end, l=(self.d.unit * depth), lftlabel=in3_lbl)
            return [l4.end, l2.end, l6.end]

    def addNOT(self, in1_lbl='', out_lbl='', reverse=False, connectTo = 0):
        if reverse:
            S = self.d.add(l.NOT, lftlabel=in1_lbl, rgtlabel=out_lbl, reverse=True, xy=connectTo)
        else:
            S = self.d.add(l.NOT, lftlabel=in1_lbl, rgtlabel=out_lbl, xy=connectTo)
        return [S.end]

    def addBUFFER(self, in1_lbl='', out_lbl='', reverse=False, connectTo = 0):
        if reverse:
            S = self.d.add(l.BUF, lftlabel=in1_lbl, rgtlabel=out_lbl, reverse=True, xy=connectTo)
        else:
            S = self.d.add(l.BUF, lftlabel=in1_lbl, rgtlabel=out_lbl, xy=connectTo)
        return [S.end]



    def drawSchematic(self):
        self.d.draw()

