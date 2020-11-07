from arm.logicnode.arm_nodes import *

class VectorMathNode(ArmLogicTreeNode):
    """Mathematical operations on vectors."""
    bl_idname = 'LNVectorMathNode'
    bl_label = 'Vector Math'
    arm_section = 'vector'
    arm_version = 1
    min_outputs = 2
    max_outputs = 5

    def get_bool(self):
        return self['property1']

    def set_bool(self, value):
        self['property1'] = value
        if value:
            if (self.property0 == 'Length') or (self.property0 == 'Distance') or (self.property0 == 'Dot Product'):
                self.outputs.remove(self.outputs.values()[-1]) # Distance/Length/Scalar
            self.add_output('NodeSocketFloat', 'X') # Result X
            self.add_output('NodeSocketFloat', 'Y') # Result Y
            self.add_output('NodeSocketFloat', 'Z') # Result Z
            if (self.property0 == 'Length'):
                self.add_output('NodeSocketFloat', 'Length') # Length
            if (self.property0 == 'Distance'):
                self.add_output('NodeSocketFloat', 'Distance') # Distance
            if (self.property0 == 'Dot Product'):
                self.add_output('NodeSocketFloat', 'Scalar') # Scalar

        else:
            if (self.property0 == 'Length') or (self.property0 == 'Distance') or (self.property0 == 'Dot Product'):
                self.outputs.remove(self.outputs.values()[-1]) # Distance/Length/Scalar
            self.outputs.remove(self.outputs.values()[-1]) # Result X
            self.outputs.remove(self.outputs.values()[-1]) # Result Y
            self.outputs.remove(self.outputs.values()[-1]) # Result Z
            if (self.property0 == 'Length'):
                self.add_output('NodeSocketFloat', 'Length') # Length
            if (self.property0 == 'Distance'):
                self.add_output('NodeSocketFloat', 'Distance') # Distance
            if (self.property0 == 'Dot Product'):
                self.add_output('NodeSocketFloat', 'Scalar') # Scalar

    property1: BoolProperty(name='Separator Out', default=False, set=set_bool, get=get_bool)

    @staticmethod
    def get_enum_id_value(obj, prop_name, value):
        return obj.bl_rna.properties[prop_name].enum_items[value].identifier

    @staticmethod
    def get_count_in(operation_name):
        return {
            'Add': 0,
            'Subtract': 0,
            'Average': 0,
            'Dot Product': 0,
            'Cross Product': 0,
            'Multiply': 0,
            'MultiplyFloats': 0,
            'Distance': 2,
            'Reflect': 2,
            'Normalize': 1,
            'Length': 1
        }.get(operation_name, 0)

    def get_enum(self):   
        return self['property0']

    def set_enum(self, value):
        # Checking the selection of another operation
        select_current = self.get_enum_id_value(self, 'property0', value)
        select_prev = self.property0
        if select_prev != select_current:
            if (select_prev == 'Distance') or (select_prev == 'Length') or (self.property0 == 'Dot Product'):
                self.outputs.remove(self.outputs.values()[-1])
            # Many arguments: Add, Subtract, Average, Dot Product, Cross Product, Multiply, MultiplyFloats
            if (self.get_count_in(select_current) == 0):
                if (select_current == "MultiplyFloats") or (select_prev == "MultiplyFloats"):
                    while (len(self.inputs) > 1):
                        self.inputs.remove(self.inputs.values()[-1])
                if (select_current == "MultiplyFloats"):
                    self.add_input('NodeSocketFloat', 'Value ' + str(len(self.inputs)))
                else:
                    while (len(self.inputs) < 2):
                        self.add_input('NodeSocketVector', 'Value ' + str(len(self.inputs)))
                if (select_current == 'Dot Product'):
                    self.add_output('NodeSocketFloat', 'Scalar')
            # 2 arguments: Distance, Reflect
            if (self.get_count_in(select_current) == 2):
                count = 2
                if (select_prev == "MultiplyFloats"):
                    count = 1
                while (len(self.inputs) > count):
                    self.inputs.remove(self.inputs.values()[-1])
                while (len(self.inputs) < 2):
                    self.add_input('NodeSocketVector', 'Value ' + str(len(self.inputs)))
                if (select_current == 'Distance'):
                    self.add_output('NodeSocketFloat', 'Distance')
            # 1 argument: Normalize, Length
            if (self.get_count_in(select_current) == 1):
                while (len(self.inputs) > 1):
                    self.inputs.remove(self.inputs.values()[-1])
                if (select_current == 'Length'):
                    self.add_output('NodeSocketFloat', 'Length')
        self['property0'] = value

    property0: EnumProperty(
        items = [('Add', 'Add', 'Add'),
                 ('Dot Product', 'Dot Product', 'Dot Product'),
                 ('Multiply', 'Multiply', 'Multiply'),
                 ('MultiplyFloats', 'Multiply (Floats)', 'Multiply (Floats)'),
                 ('Normalize', 'Normalize', 'Normalize'),
                 ('Subtract', 'Subtract', 'Subtract'),
                 ('Average', 'Average', 'Average'),
                 ('Cross Product', 'Cross Product', 'Cross Product'),
                 ('Length', 'Length', 'Length'),
                 ('Distance', 'Distance', 'Distance'),
                 ('Reflect', 'Reflect', 'Reflect')],
        name='', default='Add', set=set_enum, get=get_enum)

    def __init__(self):
        array_nodes[str(id(self))] = self

    def init(self, context):
        super(VectorMathNode, self).init(context)
        self['property0'] = 0
        self['property1'] = False
        self.add_input('NodeSocketVector', 'Value 0', default_value=[0.0, 0.0, 0.0])
        self.add_input('NodeSocketVector', 'Value 1', default_value=[0.0, 0.0, 0.0])
        self.add_output('NodeSocketVector', 'Result')

    def draw_buttons(self, context, layout):
        layout.prop(self, 'property1') # Separator Out
        layout.prop(self, 'property0') # Operation
        # Buttons
        if (self.get_count_in(self.property0) == 0):
            row = layout.row(align=True)
            column = row.column(align=True)
            op = column.operator('arm.node_add_input', text='Add Value', icon='PLUS', emboss=True)
            op.node_index = str(id(self))
            op.name_format = 'Value {0}'
            if (self.property0 == "MultiplyFloats"):
                op.socket_type = 'NodeSocketFloat'
            else:
                op.socket_type = 'NodeSocketVector'
            column = row.column(align=True)
            op = column.operator('arm.node_remove_input', text='', icon='X', emboss=True)
            op.node_index = str(id(self))
            if len(self.inputs) == 2:
                column.enabled = False