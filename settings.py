
import argparse

parser = argparse.ArgumentParser(description = 'Um programa de exemplo.')
parser.add_argument('--repository_uuid', required=True, type=str)
parser.add_argument('--auth_token', required=True, type=str)
arguments = parser.parse_args()

REPOSITORY_UUID = arguments.repository_uuid
LANGUAGE = 'pt_br'
AUTH_TOKEN = arguments.auth_token


