from arm.logicnode.arm_nodes import *

class WriteFileNode(ArmLogicTreeNode):
    """Use to write a content inside a file.

    @seeNode Read File"""
    bl_idname = 'LNWriteFileNode'
    bl_label = 'Write File'
    arm_version = 1

    def init(self, context):
        super(WriteFileNode, self).init(context)
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('NodeSocketString', 'File')
        self.add_input('NodeSocketString', 'String')

add_node(WriteFileNode, category=PKG_AS_CATEGORY, section='file')
