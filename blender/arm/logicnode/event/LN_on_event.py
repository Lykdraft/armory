from arm.logicnode.arm_nodes import *

class OnEventNode(ArmLogicTreeNode):
    """Activates the output when the given event is received.

    @seeNode Send Event To Object
    @seeNode Send Event"""
    bl_idname = 'LNOnEventNode'
    bl_label = 'On Event'
    arm_version = 1
    property0: StringProperty(name='', default='')

    def init(self, context):
        super(OnEventNode, self).init(context)
        self.add_output('ArmNodeSocketAction', 'Out')

    def draw_buttons(self, context, layout):
        layout.prop(self, 'property0')

add_node(OnEventNode, category=PKG_AS_CATEGORY, section='custom')
