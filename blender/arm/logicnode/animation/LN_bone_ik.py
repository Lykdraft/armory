from arm.logicnode.arm_nodes import *

class BoneIKNode(ArmLogicTreeNode):
    """Apply inverse kinematics in an object bone."""
    bl_idname = 'LNBoneIKNode'
    bl_label = 'Bone IK'
    arm_version = 1

    def init(self, context):
        super(BoneIKNode, self).init(context)
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('ArmNodeSocketObject', 'Object')
        self.add_input('NodeSocketString', 'Bone')
        self.add_input('NodeSocketVector', 'Goal')
        self.add_output('ArmNodeSocketAction', 'Out')

add_node(BoneIKNode, category=PKG_AS_CATEGORY, section='armature')
