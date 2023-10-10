#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import boto3

s3=boto3.resource(‘s3’)
def lambda_handler(event, context):
    for buckets in s3.buckets.all():
        print(buckets.name)

