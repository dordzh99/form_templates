import json

from fastapi import FastAPI, HTTPException

from validators import determine_field_type, validate_field

app = FastAPI()


@app.post('/get_form')
async def get_form(data: dict[str, str]):

    with open('../db/form_templates.json') as json_file:
        templates_data = json.load(json_file)['_default']

    best_counts = 0
    best_template_name = None

    for template_id, template in templates_data.items():
        try:
            if all(key in data for key in template if key != "name"):
                count_fields = 0
                for field, value in data.items():
                    if field in template:
                        field_type = template[field]
                        validate_field(value, field_type)
                        count_fields += 1
                if count_fields > best_counts:
                    best_counts = count_fields
                    best_template_name = template['name']

        except HTTPException as e:
            raise HTTPException(status_code=e.status_code, detail=f"Validation error: {e.detail}")
    if best_template_name:
        return best_template_name
    else:
        fields_without_tmp = {}
        for field, value in data.items():
            field_type = determine_field_type(value)
            fields_without_tmp[field] = field_type
        return fields_without_tmp
