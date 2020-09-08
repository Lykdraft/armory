import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class QuaternionNode(ArmLogicTreeNode):
    '''Quaternion node'''
    bl_idname = 'LNQuaternionNode'
    bl_label = 'Quaternion'
    bl_icon = 'NONE'

    def init(self, context):
        self.inputs.new('NodeSocketFloat', 'X')
        self.inputs.new('NodeSocketFloat', 'Y')
        self.inputs.new('NodeSocketFloat', 'Z')
        self.inputs.new('NodeSocketFloat', 'W')
        self.inputs[-1].default_value = 1.0

        self.outputs.new('NodeSocketVector', 'Quaternion')
        self.outputs.new('NodeSocketVector', 'XYZ')
        self.outputs.new('NodeSocketFloat', 'W')

add_node(QuaternionNode, category=MODULE_AS_CATEGORY, section='quaternions')
