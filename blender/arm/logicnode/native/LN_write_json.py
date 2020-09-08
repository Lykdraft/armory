import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class WriteJsonNode(ArmLogicTreeNode):
    '''Write JSON node'''
    bl_idname = 'LNWriteJsonNode'
    bl_label = 'Write JSON'
    bl_icon = 'NONE'

    def init(self, context):
        self.inputs.new('ArmNodeSocketAction', 'In')
        self.inputs.new('NodeSocketString', 'File')
        self.inputs.new('NodeSocketShader', 'Dynamic')

add_node(WriteJsonNode, category=MODULE_AS_CATEGORY, section='file')
