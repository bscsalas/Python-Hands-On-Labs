import sys
import io
import json
import os

# Tutorials Dojo Python Labs
def lambda_handler(event, context):
    
    tutorialsDojoCode =json.loads(event['body'])['code']
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout

    try:
        exec_globals = {}
        exec_locals = {}
        exec(tutorialsDojoCode, exec_globals, exec_locals)
        output = new_stdout.getvalue().strip()
        if not output:  # If exec does not print anything, indicate successful execution
            output = 'Code executed successfully.'
    except Exception as e:
        print(e)
        output = str(e)
    finally:
        # Reset standard output
        sys.stdout = old_stdout

    return {
        'statusCode': 200,
        'body': json.dumps({
            'output': output
        })
    }
