from django.shortcuts import render

# Create your views here.
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
import boto3
import time

def post_reqiest():
 import requests, json 
 tmpData = { "train" :  "True"} ,
 jsonData = json.dumps(tmpData) 
 header = {
     'Content-type': "application/json"
 }
 print("POST")
 r = requests.post("http://15.164.17.5:8000/list/", data=jsonData, headers=header, verify=False)


@api_view(["GET", "POST"])
def list_users(request):
    instance_id = 'i-00aae7b8f56ff4118'
    print(request)
    data = request.data .get('train')
    print(data)
    print(data==1)
    if (data == 1):
        ec2 = boto3.client('ec2',region_name='ap-northeast-2')
        response = ec2.describe_instances(InstanceIds=[
                    instance_id
                ],)
        state = response['Reservations'][0]['Instances'][0]['State']['Name']
        print(state)
        if state != "running": 
            print("START")   
            responses = ec2.start_instances(
                    InstanceIds=[
                        instance_id
                    ],

                    DryRun=False # Make it False to test
                )
            print(responses)

        time.sleep(10)
        post_reqiest()
        time.sleep(10)
        """print("END")
        response = ec2.describe_instances(InstanceIds=[
                    instance_id
                ],)
        state = response['Reservations'][0]['Instances'][0]['State']['Name']
        print(state)
        if state == "running":
            responses = ec2.stop_instances(
                    InstanceIds=[
                        instance_id
                    ],
                )
            print(responses)"""

        print("TERMINATE")
        #responses = ec2.stop_instances(
        #            InstanceIds=[
        #                'i-081f5d458bb9f9a6f'
        #            ],
        #        )
        #print(responses)

    return Response({'MESSAGE':'SUCCESS'}, status=201)


"""def snippet_detail(request, pk):
    
    #?????? ?????? ??????, ????????????, ??????
    
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)"""