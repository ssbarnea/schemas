# ajv errors

```json
[
  {
    "instancePath": "/0",
    "keyword": "required",
    "message": "must have required property 'ansible.builtin.import_playbook'",
    "params": {
      "missingProperty": "ansible.builtin.import_playbook"
    },
    "schemaPath": "#/$defs/ansible.builtin.import_playbook/oneOf/0/required"
  },
  {
    "instancePath": "/0",
    "keyword": "required",
    "message": "must have required property 'import_playbook'",
    "params": {
      "missingProperty": "import_playbook"
    },
    "schemaPath": "#/$defs/ansible.builtin.import_playbook/oneOf/1/required"
  },
  {
    "instancePath": "/0",
    "keyword": "oneOf",
    "message": "must match exactly one schema in oneOf",
    "params": {
      "passingSchemas": null
    },
    "schemaPath": "#/$defs/ansible.builtin.import_playbook/oneOf"
  },
  {
    "instancePath": "/0",
    "keyword": "additionalProperties",
    "message": "must NOT have additional properties",
    "params": {
      "additionalProperty": "hosts"
    },
    "schemaPath": "#/$defs/ansible.builtin.import_playbook/additionalProperties"
  },
  {
    "instancePath": "/0",
    "keyword": "additionalProperties",
    "message": "must NOT have additional properties",
    "params": {
      "additionalProperty": "tasks"
    },
    "schemaPath": "#/$defs/ansible.builtin.import_playbook/additionalProperties"
  },
  {
    "instancePath": "/0/tasks/0/failed_when",
    "keyword": "type",
    "message": "must be boolean",
    "params": {
      "type": "boolean"
    },
    "schemaPath": "#/$defs/complex_conditional/oneOf/0/type"
  },
  {
    "instancePath": "/0/tasks/0/failed_when",
    "keyword": "type",
    "message": "must be string",
    "params": {
      "type": "string"
    },
    "schemaPath": "#/$defs/complex_conditional/oneOf/1/type"
  },
  {
    "instancePath": "/0/tasks/0/failed_when",
    "keyword": "type",
    "message": "must be array",
    "params": {
      "type": "array"
    },
    "schemaPath": "#/$defs/complex_conditional/oneOf/2/type"
  },
  {
    "instancePath": "/0/tasks/0/failed_when",
    "keyword": "oneOf",
    "message": "must match exactly one schema in oneOf",
    "params": {
      "passingSchemas": null
    },
    "schemaPath": "#/$defs/complex_conditional/oneOf"
  },
  {
    "instancePath": "/0/tasks/0",
    "keyword": "required",
    "message": "must have required property 'block'",
    "params": {
      "missingProperty": "block"
    },
    "schemaPath": "#/required"
  },
  {
    "instancePath": "/0/tasks/0",
    "keyword": "anyOf",
    "message": "must match a schema in anyOf",
    "params": {},
    "schemaPath": "#/items/anyOf"
  },
  {
    "instancePath": "/0/tasks/2/failed_when",
    "keyword": "type",
    "message": "must be boolean",
    "params": {
      "type": "boolean"
    },
    "schemaPath": "#/$defs/complex_conditional/oneOf/0/type"
  },
  {
    "instancePath": "/0/tasks/2/failed_when",
    "keyword": "type",
    "message": "must be string",
    "params": {
      "type": "string"
    },
    "schemaPath": "#/$defs/complex_conditional/oneOf/1/type"
  },
  {
    "instancePath": "/0/tasks/2/failed_when",
    "keyword": "type",
    "message": "must be array",
    "params": {
      "type": "array"
    },
    "schemaPath": "#/$defs/complex_conditional/oneOf/2/type"
  },
  {
    "instancePath": "/0/tasks/2/failed_when",
    "keyword": "oneOf",
    "message": "must match exactly one schema in oneOf",
    "params": {
      "passingSchemas": null
    },
    "schemaPath": "#/$defs/complex_conditional/oneOf"
  },
  {
    "instancePath": "/0/tasks/2",
    "keyword": "required",
    "message": "must have required property 'block'",
    "params": {
      "missingProperty": "block"
    },
    "schemaPath": "#/required"
  },
  {
    "instancePath": "/0/tasks/2",
    "keyword": "anyOf",
    "message": "must match a schema in anyOf",
    "params": {},
    "schemaPath": "#/items/anyOf"
  },
  {
    "instancePath": "/0",
    "keyword": "oneOf",
    "message": "must match exactly one schema in oneOf",
    "params": {
      "passingSchemas": null
    },
    "schemaPath": "#/items/oneOf"
  }
]
```

# check-jsonschema

stdout:

```json
{
  "status": "fail",
  "errors": [
    {
      "filename": "negative_test/playbooks/invalid-failed-when.yml",
      "path": "$[0]",
      "message": "{'hosts': 'localhost', 'tasks': [{'debug': {'msg': 'failed_when should not accept numeric'}, 'failed_when': 123}, {'debug': {'msg': 'failed_when should not accept sequence'}, 'failed_when': ['foo', 'bar']}, {'debug': {'msg': 'failed_when should not accept map'}, 'failed_when': {}}]} is not valid under any of the given schemas",
      "has_sub_errors": true,
      "best_match": {
        "path": "$[0]",
        "message": "'hosts', 'tasks' do not match any of the regexes: '^(ansible\\\\.builtin\\\\.)?import_playbook$', 'name', 'vars'"
      }
    }
  ]
}
```