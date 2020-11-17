from arm.logicnode.arm_nodes import *

class SetDebugConsoleSettings(ArmLogicTreeNode):
    """Sets the debug console settings."""
    bl_idname = 'LNSetDebugConsoleSettings'
    bl_label = 'Set Debug Console Settings'
    arm_version = 1

    property0: EnumProperty(
        items = [('anchor left', 'Anchor Left', 'Anchor debug console in the top left'),
                 ('anchor center', 'Anchor Center', 'Anchor debug console in the top center'),
                 ('anchor right', 'Anchor Right', 'Anchor the debug console in the top right')],
        name='', default='anchor right')

    def init(self, context):  
        super(SetDebugConsoleSettings, self).init(context) 
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('NodeSocketBool', 'Visible')  
        self.add_input('NodeSocketFloat', 'Scale')  
        self.inputs[-1].default_value = 1.0

        self.add_output('ArmNodeSocketAction', 'Out')

    def draw_buttons(self, context, layout):
        layout.prop(self, 'property0')
