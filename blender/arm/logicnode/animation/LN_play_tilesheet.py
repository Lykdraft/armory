import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class PlayTilesheetNode(ArmLogicTreeNode):
    '''Play tilesheet node'''
    bl_idname = 'LNPlayTilesheetNode'
    bl_label = 'Play Tilesheet'
    bl_icon = 'NONE'

    def init(self, context):
        self.inputs.new('ArmNodeSocketAction', 'In')
        self.inputs.new('ArmNodeSocketObject', 'Object')
        self.inputs.new('NodeSocketString', 'Action')
        self.outputs.new('ArmNodeSocketAction', 'Out')
        self.outputs.new('ArmNodeSocketAction', 'Done')

add_node(PlayTilesheetNode, category=MODULE_AS_CATEGORY, section='tilesheet')
