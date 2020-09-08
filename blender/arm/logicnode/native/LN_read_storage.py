import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class ReadStorageNode(ArmLogicTreeNode):
    '''ReadStorage node'''
    bl_idname = 'LNReadStorageNode'
    bl_label = 'Read Storage'
    bl_icon = 'NONE'

    def init(self, context):
        self.inputs.new('NodeSocketString', 'Key')
        self.inputs.new('NodeSocketString', 'Default')
        self.outputs.new('NodeSocketShader', 'Value')

add_node(ReadStorageNode, category=MODULE_AS_CATEGORY, section='file')
