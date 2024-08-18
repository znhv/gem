def generate_report(subschema: map, line: str):
    # print(f'{Analyzing} configuration files...', '\n')
    
    # print(f"FAIL: {message} {recommendation}")
    print("{level}: {message} {recommendation} (line {line})".format(
            level=subschema['level'].upper(),
            message=subschema['message'],
            recommendation=subschema['recommendation'],
            line=line
        ),
    )
    
  

    
   # print(f"Message: {subschema['message']}")
    # if subschema['level'] == 'error':
    #     print(f"Recommendation: {subschema['recommendation']}")