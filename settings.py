
import argparse

parser = argparse.ArgumentParser(description = 'Um programa de exemplo.')
parser.add_argument('--repository_uuid', required=True, type=str)
parser.add_argument('--auth_token', required=True, type=str)
arguments = parser.parse_args()

REPOSITORY_UUID = arguments.repository_uuid
LANGUAGE = 'pt_br'
AUTH_TOKEN = arguments.auth_token


'''
REPOSITORY_UUID = '1f86ecdf-4659-4a98-84bf-78d0ef9d3512'
LANGUAGE = 'pt_br'
AUTH_TOKEN = 'Token 5ef90351e1b8bb19761e98e03773f0d20f3f94de'
'''