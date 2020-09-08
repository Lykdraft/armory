from arm.logicnode.arm_nodes import *

class GetContactsNode(ArmLogicTreeNode):
    """Get contacts node"""
    bl_idname = 'LNGetContactsNode'
    bl_label = 'Get Contacts'
    bl_icon = 'NONE'

    def init(self, context):
        self.add_input('ArmNodeSocketObject', 'Object')
        self.add_output('ArmNodeSocketArray', 'Array')

add_node(GetContactsNode, category=MODULE_AS_CATEGORY, section='contact')
