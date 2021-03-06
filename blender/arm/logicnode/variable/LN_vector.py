from arm.logicnode.arm_nodes import *

class VectorNode(ArmLogicTreeNode):
    """Stores a three-dimensional vector as a variable."""
    bl_idname = 'LNVectorNode'
    bl_label = 'Vector'
    arm_version = 1

    def init(self, context):
        super(VectorNode, self).init(context)
        self.add_input('NodeSocketFloat', 'X')
        self.add_input('NodeSocketFloat', 'Y')
        self.add_input('NodeSocketFloat', 'Z')

        self.add_output('NodeSocketVector', 'Vector', is_var=True)


add_node(VectorNode, category=PKG_AS_CATEGORY)
