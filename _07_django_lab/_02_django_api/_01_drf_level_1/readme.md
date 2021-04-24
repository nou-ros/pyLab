-> we have to add 'rest_framwork' in settings.py file
-> auto.now.add - set automatically when an instance is created, auto.now - set automatically each time instance is saved.

## Serializers
Use to convert complex data such as querysets and model instances to native python data types which can easily be rendered to JSON format with Serializer and ModelSerializer classes (same as Form and ModelForm). With deserialization we can get back the complex data again.

- It is better to create a separate directory for api works for a specific app.
- We will create a serializers.py file and import important modules.
- read_only means we will not modify the field.
- If we want to return complete object instances based on the validated data we have to implement create and update method.

## API VIEW - wrappers
- function based api view: @api_view
- class based api view: APIView 
- we can create a seperate views.py file in api direcotry

## Serializer Validation
- we have some prebuild validation methods
- we can also create custom validation

## Nested Relationship handling
- we have to handle fields with foreignkey field seprately.