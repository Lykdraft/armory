import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class BooleanNode(ArmLogicTreeNode):
    '''Bool node'''
    bl_idname = 'LNBooleanNode'
    bl_label = 'Boolean'
    bl_icon = 'NONE'

    def init(self, context):
        self.inputs.new('NodeSocketBool', 'Value')
        self.outputs.new('NodeSocketBool', 'Bool')

add_node(BooleanNode, category=MODULE_AS_CATEGORY)
