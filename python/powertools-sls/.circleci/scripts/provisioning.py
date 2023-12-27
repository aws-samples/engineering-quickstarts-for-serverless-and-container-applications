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
CIRCLECI_TOKEN = strip_spaces(creds.get('CIRCLECI_TOKEN'))
CIRCLECI_ORG_SLUG = strip_spaces(creds.get('CIRCLECI_ORG_SLUG'))
#CIRCLECI_VCS_USER = strip_spaces(creds.get('CIRCLECI_ORG_NAME'))
CIRCLECI_ORG_ID = strip_spaces(creds.get('CIRCLECI_ORG_ID'))
CIRCLECI_BASE_URL = strip_spaces('http://circleci.com/api/v2/')
CIRCLECI_CONTEXT_NAME = strip_spaces('IDT')

# Assign Variable the values from the respecive items in the toml file
GITGUARDIAN_API_KEY = strip_spaces(creds.get('GITGUARDIAN_API_KEY'))
SNYK_TOKEN = strip_spaces(creds.get('SNYK_TOKEN'))
AWS_DEFAULT_REGION = strip_spaces(creds.get('AWS_DEFAULT_REGION'))
#ANGEL_TEST = strip_spaces(creds.get('ANGEL_TEST'))

REQUEST_HEADER = {
  'content-type': "application/json",
  'Circle-Token': CIRCLECI_TOKEN
}

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
                'Context Name':context_name,
                'Environment Variable': env_var_name, 
                'Environment Value' : f'****{masked_env_value}'
              }
    return context

def add_circle_token_to_context(context_id, env_var_name, env_var_value):
  resp = put_circleci_api_request(f'context/{context_id}/environment-variable/{env_var_name}', { "value": env_var_value })
  return resp

# Get the context id to which we'll store env vars
def find_or_create_context_by_name(context_name):   # context name - CICD_WORKSHOP_docker etc...
  full_context_name = context_name
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

# Add Env vars to context
print(add_circle_token_to_context_with_name(CIRCLECI_CONTEXT_NAME, 'GITGUARDIAN_API_KEY', GITGUARDIAN_API_KEY))
print(add_circle_token_to_context_with_name(CIRCLECI_CONTEXT_NAME, 'SNYK_TOKEN', SNYK_TOKEN))
print(add_circle_token_to_context_with_name(CIRCLECI_CONTEXT_NAME, 'AWS_DEFAULT_REGION', AWS_DEFAULT_REGION))

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