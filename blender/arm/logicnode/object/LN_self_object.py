from arm.logicnode.arm_nodes import *

class SelfObjectNode(ArmLogicTreeNode):
    """Use to get the object that owns the current trait."""
    bl_idname = 'LNSelfNode'
    bl_label = 'Self Object'
    arm_version = 1

    def init(self, context):
        super(SelfObjectNode, self).init(context)
        self.add_output('ArmNodeSocketObject', 'Object')

add_node(SelfObjectNode, category=PKG_AS_CATEGORY)
