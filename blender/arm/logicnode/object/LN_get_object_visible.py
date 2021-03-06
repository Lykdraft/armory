from arm.logicnode.arm_nodes import *

class GetVisibleNode(ArmLogicTreeNode):
    """Returns whether a given object or its visual components are
    visible.

    @seeNode Set Object Visible"""
    bl_idname = 'LNGetVisibleNode'
    bl_label = 'Get Object Visible'
    arm_version = 1

    def init(self, context):
        super(GetVisibleNode, self).init(context)
        self.add_input('ArmNodeSocketObject', 'Object')
        self.add_output('NodeSocketBool', 'Is Object Visible')
        self.add_output('NodeSocketBool', 'Is Mesh Visible')
        self.add_output('NodeSocketBool', 'Is Shadow Visible')

add_node(GetVisibleNode, category=PKG_AS_CATEGORY, section='props')
