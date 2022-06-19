from common import const

schema_delete_employee = {
    "type": "object",
    "properties": {
        "eid": {"type": "string"}
    },
    "required": ["eid"]
}

schema_list_employees = {
    "type": "object",
    "properties": {
        "start": {"type": "integer", "minimum": 0},
        "limit": {"type": "integer", "minimum": 1, "maximum": 100},
        "sort": {"type": "string", "enum": list(const.EmployeeAttributes.sortable_attrs())},
        "direct": {"type": "string", "enum": [const.ASC, const.DESC]},
        "search": {"type": ["null", "string"]},
    },
    "required": ["start", "limit", "sort", "direct", "search"]
}

schema_get_employee = {
    "type": "object",
    "properties": {
        "eid": {"type": "string"}
    },
    "required": ["eid"]
}

schema_add_employee = {
    "type": "object",
    "properties": {
        "eid": {"type": "string"},
        "name": {"type": "string"},
        "department": {"type": "string"},
        "position": {"type": "string"},
        "entry_time": {}
    },
    "required": ["eid", "name", "department", "position", "entry_time"]
}

schema_mod_employee = {
    "type": "object",
    "properties": {
        "eid": {"type": "string"},
        "name": {"type": ["null", "string"]},
        "department": {"type": ["null", "string"]},
        "position": {"type": ["null", "string"]},
        "entry_time": {}
    },
    "required": ["eid"]
}
