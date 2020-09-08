import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class PlaySpeakerNode(ArmLogicTreeNode):
    '''Play speaker node'''
    bl_idname = 'LNPlaySoundNode'
    bl_label = 'Play Speaker'
    bl_icon = 'NONE'

    def init(self, context):
        self.inputs.new('ArmNodeSocketAction', 'In')
        self.inputs.new('ArmNodeSocketObject', 'Speaker')
        self.outputs.new('ArmNodeSocketAction', 'Out')

add_node(PlaySpeakerNode, category=MODULE_AS_CATEGORY)
