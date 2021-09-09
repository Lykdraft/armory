from arm.logicnode.arm_nodes import *

class TweenVectorNode( ArmLogicTreeNode):
    '''Tween a vector value'''
    bl_idname = 'LNTweenVectorNode'
    bl_label = 'Tween Vector'
    arm_version = 1
    
    property0: HaxeEnumProperty(
        'property0',
        items = [('Linear', 'Linear', 'Linear'),
                ('SineIn', 'SineIn', 'SineIn'),
                ('SineOut', 'SineOut', 'SineOut'),
                ('SineInOut', 'SineInOut', 'SineInOut'),
                ('QuadIn', 'QuadIn', 'QuadIn'),
                ('QuadOut', 'QuadOut', 'QuadOut'),
                ('QuadInOut', 'QuadInOut', 'QuadInOut'),
                ('CubicIn', 'CubicIn', 'CubicIn'),
                ('CubicOut', 'CubicOut', 'CubicOut'),
                ('CubicInOut', 'CubicInOut', 'CubicInOut'),
                ('QuartIn', 'QuartIn', 'QuartIn'),
                ('QuartOut', 'QuartOut', 'QuartOut'),
                ('QuartInOut', 'QuartInOut', 'QuartInOut'),
                ('QuintIn', 'QuintIn', 'QuintIn'),
                ('QuintOut', 'QuintOut', 'QuintOut'),
                ('QuintInOut', 'QuintInOut', 'QuintInOut'),
                ('ExpoIn', 'ExpoIn', 'ExpoIn'),
                ('ExpoOut', 'ExpoOut', 'ExpoOut'),
                ('ExpoInOut', 'ExpoInOut', 'ExpoInOut'),
                ('CircIn', 'CircIn', 'CircIn'),
                ('CircOut', 'CircOut', 'CircOut'),
                ('CircInOut', 'CircInOut', 'CircInOut'),
                ('BackIn', 'BackIn', 'BackIn'),
                ('BackOut', 'BackOut', 'BackOut'),
                ('BackInOut', 'BackInOut', 'BackInOut')],
        name='', default='Linear')

    def init(self, context):
        self.add_input('ArmNodeSocketAction', 'Start')
        self.add_input('ArmNodeSocketAction', 'Stop')
        self.add_input('ArmVectorSocket', 'From')
        self.add_input('ArmVectorSocket', 'To')
        self.add_input('ArmFloatSocket', 'Time', default_value = 1.0)
        
        self.add_output('ArmVectorSocket', 'Tween')
        self.add_output('ArmNodeSocketAction', 'Out')
        self.add_output('ArmNodeSocketAction', 'Tick')
        self.add_output('ArmNodeSocketAction', 'Done')

    def draw_buttons(self, context, layout):
        layout.prop(self, 'property0')
    
    def draw_label(self) -> str:
        return f'{self.bl_label}: {self.property0}'