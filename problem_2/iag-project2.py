import json
from datetime import datetime
import boto3

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    sourceKey = event['Records'][0]['s3']['object']['key']
    #print the name of file
    print(sourceKey)
    extension=sourceKey.split('.')
    #verify if pdf extension
    if extension[-1] == 'pdf':
        print('validation successful')
        newFileName=extension[0]+'-'+datetime.now().strftime("%Y%m%d-%H%M%S")
        newPath='final-file'+'/'+newFileName
        #move to new folder by copying and deleting it
        s3.Object('iag-project2',newPath).copy_from(CopySource='iag-project2'+'/'+sourceKey)
        s3.Object('iag-project2', sourceKey).delete()
    #remove file without pdf extension
    print('removing the key with invalid extension')
    s3.Object('iag-project2', sourceKey).delete()