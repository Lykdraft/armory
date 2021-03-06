from arm.logicnode.arm_nodes import *

class AnimationStateNode(ArmLogicTreeNode):
    """Get information about the current animation of an object."""
    bl_idname = 'LNAnimationStateNode'
    bl_label = 'Animation State'
    arm_version = 1

    def init(self, context):
        super(AnimationStateNode, self).init(context)
        self.add_input('ArmNodeSocketObject', 'Object')
        self.add_output('NodeSocketBool', 'Is Playing')
        self.add_output('NodeSocketString', 'Action')
        self.add_output('NodeSocketInt', 'Frame')

add_node(AnimationStateNode, category=PKG_AS_CATEGORY)
