from arm.logicnode.arm_nodes import *


class InverseNode(ArmLogicTreeNode):
    """Activates the output if the input is not active."""
    bl_idname = 'LNInverseNode'
    bl_label = 'Invert Output'
    arm_version = 1

    def init(self, context):
        super(InverseNode, self).init(context)
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_output('ArmNodeSocketAction', 'Out')


add_node(InverseNode, category=PKG_AS_CATEGORY, section='flow')
