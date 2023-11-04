#!/usr/bin/env python3

'''
This script will provision CircelCI 3rd party API keys, tokens and secrets into Context Variables.
This script is customizable and must be used with and accompanying credentials.toml file
'''
import sys
import toml
import json
import requests

# Strip white spaces from data
def strip_spaces(obj):
  result = obj
  if type==None:
    result = 'No value found.'
  else:
    str(result).strip()
  return result

#Get data from toml file
creds = toml.load('credentials.toml').get('keys')
CIRCLE_TOKEN = strip_spaces(creds.get('circleci_token'))
CIRCLECI_ORG_SLUG = strip_spaces(creds.get('circleci_org_slug'))
CIRCLECI_VCS_USER = CIRCLECI_ORG_SLUG.rsplit('/',1)[1]  #Get the users vcs name from the slug
CIRCLECI_ORG_ID = strip_spaces(creds.get('circleci_org_id'))
CIRCLECI_BASE_URL = strip_spaces('http://circleci.com/api/v2/')
CIRCLECI_CONTEXT_NAME_PREFIX = strip_spaces('AWS_Demo')

# Assign Variable the values from the respecive items in the toml file
SNYK_TOKEN = strip_spaces(creds.get('snyk_token'))
AWS_ACCESS_KEY_ID = strip_spaces(creds.get('AWS_ACCESS_KEY_ID'))
AWS_SECRET_ACCESS_KEY = strip_spaces(creds.get('AWS_SECRET_ACCESS_KEY'))

## UnComment theses if you plan on using any of these 3rd party vendors in your project
# # Docker Hub 
# DOCKER_LOGIN = strip_spaces(creds.get('docker_login'))
# DOCKER_TOKEN = strip_spaces(creds.get('docker_token'))

# # TF cloud
# TF_CLOUD_API_HOST = 'https://app.terraform.io/api/v2'
# TF_CLOUD_TOKEN = strip_spaces(creds.get('tf_cloud_token'))
# TF_CLOUD_ORG_EMAIL = strip_spaces(creds.get('tf_cloud_org_email'))
# TF_CLOUD_ORG_NAME = strip_spaces(creds.get('tf_cloud_org_name'))
# TF_CLOUD_ORGANIZATION = f'{TF_CLOUD_ORG_NAME}-{CIRCLECI_VCS_USER}'   # Create a unique Org Name for TF Cloud
# TF_CLOUD_WORKSPACE = strip_spaces(creds.get('tf_cloud_workspace'))

# # Digital Ocean 
# DIGITAL_OCEAN_TOKEN = strip_spaces(creds.get('digital_ocean_token'))

REQUEST_HEADER = {
  'content-type': "application/json",
  'Circle-Token': CIRCLE_TOKEN
}

## TF Cloud
# TF_CLOUD_HEADERS = {
#   'Authorization' : f'Bearer {TF_CLOUD_TOKEN}',
#   'Content-Type': 'application/vnd.api+json'
# }

def get_circleci_api_request(endpoint, payload_dict):
  try:
    resp = requests.get(CIRCLECI_BASE_URL + endpoint, headers=REQUEST_HEADER)
    resp.raise_for_status()
    return resp.json()   
  except requests.exceptions.HTTPError as errh:
    print ("Http Error:",errh)
  except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)
  except requests.exceptions.Timeout as errt:
    print ("Timeout Error:",errt)
  except requests.exceptions.RequestException as err:
    print ("OOps: Something Else",err)

def post_circleci_api_request(endpoint, payload_dict):
  try:
    resp = requests.post(CIRCLECI_BASE_URL + endpoint, headers=REQUEST_HEADER,json=payload_dict)
    resp.raise_for_status()
    return resp.json()
  except requests.exceptions.HTTPError as errh:
    print ("Http Error:",errh)
  except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)
  except requests.exceptions.Timeout as errt:
    print ("Timeout Error:",errt)
  except requests.exceptions.RequestException as err:
    print ("OOps: Something Else",err)

def put_circleci_api_request(endpoint, payload_dict):
  try:
    resp = requests.put(CIRCLECI_BASE_URL + endpoint, headers=REQUEST_HEADER,json=payload_dict)
    resp.raise_for_status()
    return resp.json()    
  except requests.exceptions.HTTPError as errh:
    print ("Http Error:",errh)
  except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)
  except requests.exceptions.Timeout as errt:
    print ("Timeout Error:",errt)
  except requests.exceptions.RequestException as err:
    print ("OOps: Something Else",err)

def delete_circleci_api_request(endpoint, context_id):
  try:
    resp = requests.delete(CIRCLECI_BASE_URL + endpoint + context_id, headers=REQUEST_HEADER)
    resp.raise_for_status()
    return resp.json()   
  except requests.exceptions.HTTPError as errh:
    print ("Http Error:",errh)
  except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)
  except requests.exceptions.Timeout as errt:
    print ("Timeout Error:",errt)
  except requests.exceptions.RequestException as err:
    print ("OOps: Something Else",err)

def add_circle_token_to_context_with_name(context_name, env_var_name, env_var_value):
    context_id = find_or_create_context_by_name(context_name)
    add_circle_token_to_context(context_id=context_id, env_var_name=env_var_name, env_var_value=env_var_value)
    
    #Mask the secret values 
    masked_env_value = env_var_value[-4:] if len(env_var_value) > 4 else "***********"
    context = {
                'Context Name':CIRCLECI_CONTEXT_NAME_PREFIX + context_name,
                'Environment Variable': env_var_name, 
                'Environment Value' : f'****{masked_env_value}'
              }
    return context

def add_circle_token_to_context(context_id, env_var_name, env_var_value):
  resp = put_circleci_api_request(f'context/{context_id}/environment-variable/{env_var_name}', { "value": env_var_value })
  return resp

# Get the context id to which we'll store env vars
def find_or_create_context_by_name(context_name):   # context name - CICD_WORKSHOP_docker etc...
  full_context_name = CIRCLECI_CONTEXT_NAME_PREFIX + context_name
  contexts = get_circleci_api_request(f'context?owner-id={CIRCLECI_ORG_ID}&owner-type=organization', None).get('items')
  context = next((ctx for ctx in contexts if ctx.get('name') == full_context_name), None)
  # print(f'Full Context Name: {context}')
  if context == None:
  # Context doesn't exist so we create it   
    context_payload = {
      "name": full_context_name,
        "owner": {
          "id": CIRCLECI_ORG_ID,
          "type": "organization"
        }
    }
    context = post_circleci_api_request('context', context_payload) 
  circleci_context_id = context.get('id')
  return circleci_context_id

# # Terraform Cloud code blocks
# def get_tf_cloud_org(end_point, tfc_headers, org_name):
#   try:
#     req = f'{end_point}/organizations/{org_name}'
#     resp = requests.get(req, headers=tfc_headers)
#     status_code =resp.status_code
#     resp = resp.json()
#     resp['status_code'] = status_code
#     return resp 
#   except requests.exceptions.HTTPError as errh:
#     print ("Http Error:",errh)
#   except requests.exceptions.ConnectionError as errc:
#     print ("Error Connecting:",errc)
#   except requests.exceptions.Timeout as errt:
#     print ("Timeout Error:",errt)
#   except requests.exceptions.RequestException as err:
#     print ("OOps: Something Else",err)

# def post_tf_cloud_org(end_point, tfc_headers, org_name, email):
#   try:
#     req = f'{end_point}/organizations'
#     pay_load = {
#       'data': {
#         'type': 'organizations',
#         'attributes': {
#           'name': f'{org_name}',
#           'email': f'{email}'}
#         }
#     }
#     resp = requests.post(req, headers=tfc_headers, json=pay_load)
#     status_code =resp.status_code
#     resp = resp.json()
#     resp['status_code'] = status_code
#     return resp 
#   except requests.exceptions.HTTPError as errh:
#     print ("Http Error:",errh)
#   except requests.exceptions.ConnectionError as errc:
#     print ("Error Connecting:",errc)
#   except requests.exceptions.Timeout as errt:
#     print ("Timeout Error:",errt)
#   except requests.exceptions.RequestException as err:
#    print ("OOps: Something Else",err)

# def get_tf_workspace(end_point, tfc_headers, org_name, workspace_name):
#   try:
#     req = f'{end_point}/organizations/{org_name}/workspaces/{workspace_name}'
#     resp = requests.get(req, headers=tfc_headers)
#     status_code =resp.status_code
#     resp = resp.json()
#     resp['status_code'] = status_code
#     return resp 
#   except requests.exceptions.HTTPError as errh:
#     print ("Http Error:",errh)
#   except requests.exceptions.ConnectionError as errc:
#     print ("Error Connecting:",errc)
#   except requests.exceptions.Timeout as errt:
#     print ("Timeout Error:",errt)
#   except requests.exceptions.RequestException as err:
#     print ("OOps: Something Else",err)

# def post_tf_workspaces(end_point, tfc_headers, org_name, workspace_name, execution_mode):
#   try:
#     req = f'{end_point}/organizations/{org_name}/workspaces'
#     pay_load = {
#       'data': {
#         'type': 'workspaces',
#         'attributes': {
#           'name': workspace_name,
#           'execution-mode':execution_mode
#         }
#       }
#     }
#     resp = requests.post(req, headers=tfc_headers, json=pay_load)
#     status_code =resp.status_code
#     resp = resp.json()
#     resp['status_code'] = status_code
#     return resp 
#   except requests.exceptions.HTTPError as errh:
#     print ("Http Error:",errh)
#   except requests.exceptions.ConnectionError as errc:
#     print ("Error Connecting:",errc)
#   except requests.exceptions.Timeout as errt:
#     print ("Timeout Error:",errt)
#   except requests.exceptions.RequestException as err:
#    print ("OOps: Something Else",err)  

# Add Env vars to context

print(add_circle_token_to_context_with_name('AWS', 'AWS_ACCESS_KEY_ID', AWS_ACCESS_KEY_ID))
print(add_circle_token_to_context_with_name('AWS', 'AWS_SECRET_ACCESS_KEY', AWS_SECRET_ACCESS_KEY))
print(add_circle_token_to_context_with_name('SNYK', 'SNYK_TOKEN', SNYK_TOKEN))

## Uncoment if you plan on using any of the 3rd party vendors listed below
# print(add_circle_token_to_context_with_name('TERRAFORM_CLOUD', 'TF_CLOUD_TOKEN', TF_CLOUD_TOKEN))
# print(add_circle_token_to_context_with_name('TERRAFORM_CLOUD', 'TF_CLOUD_ORG_EMAIL', TF_CLOUD_ORG_EMAIL))
# print(add_circle_token_to_context_with_name('TERRAFORM_CLOUD', 'TF_CLOUD_ORGANIZATION', TF_CLOUD_ORGANIZATION))
# print(add_circle_token_to_context_with_name('TERRAFORM_CLOUD', 'TF_CLOUD_WORKSPACE', TF_CLOUD_WORKSPACE))
# print(add_circle_token_to_context_with_name('DOCKER', 'DOCKER_LOGIN', DOCKER_LOGIN))
# print(add_circle_token_to_context_with_name('DIGITAL_OCEAN', 'DIGITAL_OCEAN_TOKEN', DIGITAL_OCEAN_TOKEN))
# print(add_circle_token_to_context_with_name('DOCKER', 'DOCKER_PASSWORD', DOCKER_TOKEN))


## Uncoment these code blocks if you intend to use TF Cloud 

# #Create Terraform Cloud Assets
# tf_response = get_tf_cloud_org(TF_CLOUD_API_HOST, TF_CLOUD_HEADERS, TF_CLOUD_ORGANIZATION)
# print(f'Creating the new Terraform Cloud Organization: {TF_CLOUD_ORGANIZATION}')
# if tf_response.get('status_code') == 200:
#   org_name = tf_response['data']['attributes'].get('name')
#   print(f'The {org_name} already exists no further action taken.')
#   # print(f'The {TF_CLOUD_ORGANIZATION} already exists.')
# else:  # Create the org
#   resp = post_tf_cloud_org(TF_CLOUD_API_HOST, TF_CLOUD_HEADERS, TF_CLOUD_ORGANIZATION, TF_CLOUD_ORG_EMAIL)
#   if resp.get('status_code') == 201:
#       org_name = resp['data']['attributes'].get('name')
#       print(f'Successfully created the {org_name} organization in Terraform cloud')
#   else:
#     print(f'Error: {resp.json()}')

# org_exists = get_tf_cloud_org(TF_CLOUD_API_HOST, TF_CLOUD_HEADERS, TF_CLOUD_ORGANIZATION)
# if org_exists.get('status_code') == 200:
#   # create workspaces
#   org_name = org_exists['data']['attributes'].get('name')

#   ws = [TF_CLOUD_WORKSPACE, f'{TF_CLOUD_WORKSPACE}-deployment']
#   for w in ws:
#       print(f'Creating workspace: {w}')
#       resp = post_tf_workspaces(TF_CLOUD_API_HOST,TF_CLOUD_HEADERS,org_name,w,'local')
#       if resp.get('status_code') == 201:
#         print(f'Successfully created workspace: {w} in the {org_name} organization')
#       elif resp.get('status_code') == 422:
#         print(f'Workspace name: {w} already exists in the {org_name} organization.')
#       else:
#         print(f'{resp}')
# else:
#   print(f'Error: The {org_name} does not exist.')
      

# # Warning uncommenting the code block below will delete all the contexts created above
# # To delete the values from CircleCI contexts uncomment the lines below
#
# def delete_contexts():
#   context_ids = get_circleci_api_request(F'context?owner-id={CIRCLECI_ORG_ID}&owner-type=organization', None).get('items')
#   for ctx in context_ids:
#     if ctx == None:
#       #Do nothing
#       print('-----\n')
#     else:
#       #delete the context
#       message = delete_circleci_api_request(f'context/', ctx.get('id')).get('message')
#       print(f"Context ID: {ctx.get('id')} Name: {ctx.get('name')} {message}") 
#
# # execute the delete context call
# delete_contexts()