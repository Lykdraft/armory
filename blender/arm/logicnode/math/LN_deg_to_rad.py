import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class DegToRadNode(ArmLogicTreeNode):
    '''Degrees to radians node'''
    bl_idname = 'LNDegToRadNode'
    bl_label = 'Deg to Rad'
    bl_icon = 'NONE'

    def init(self, context):
        self.inputs.new('NodeSocketFloat', 'Degrees')
        self.outputs.new('NodeSocketFloat', 'Radians')

add_node(DegToRadNode, category=MODULE_AS_CATEGORY, section='angle')
