import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class MaskNode(ArmLogicTreeNode):
    '''Mask node'''
    bl_idname = 'LNMaskNode'
    bl_label = 'Mask'
    bl_icon = 'NONE'

    def init(self, context):
        for i in range(1, 21):
            label = 'Group {:02d}'.format(i)
            self.inputs.new('NodeSocketBool', label)

        self.outputs.new('NodeSocketInt', 'Mask')

add_node(MaskNode, category=MODULE_AS_CATEGORY)
