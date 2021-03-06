from arm.logicnode.arm_nodes import *

class RotateObjectAroundAxisNode(ArmLogicTreeNode):
    """Deprecated. It is recommended to use the 'Rotate Object' node instead."""
    bl_idname = 'LNRotateObjectAroundAxisNode'
    bl_label = 'Rotate Object Around Axis (Deprecated)'
    bl_description = "Please use the \"Rotate Object\" node instead"
    bl_icon = 'ERROR'
    arm_version=2

    def init(self, context):
        super(RotateObjectAroundAxisNode, self).init(context)
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('ArmNodeSocketObject', 'Object')
        self.add_input('NodeSocketVector', 'Axis', default_value=[0, 0, 1])
        self.add_input('NodeSocketFloat', 'Angle')
        self.add_output('ArmNodeSocketAction', 'Out')

    def get_replacement_node(self, node_tree: bpy.types.NodeTree):
        if self.arm_version not in (0, 1):
            raise LookupError()

        return NodeReplacement(
            'LNRotateObjectAroundAxisNode', self.arm_version, 'LNRotateObjectNode', 1,
            in_socket_mapping = {0:0, 1:1, 2:2, 3:3}, out_socket_mapping={0:0},
            property_defaults={'property0': "Angle Axies (Radians)"}
        )


add_node(RotateObjectAroundAxisNode, category='transform', section='rotation', is_obsolete=True)
