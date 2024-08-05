import json
import os
import requests
from ConfigFiles import zephyr_config



class zephyr_utils:

    def __init__(self):
        self.token_url = "https://prod-vortexapi.zephyr4jiracloud.com/api/v1/jwt/generate"
        self.create_automation_job_url = "https://prod-vortexapi.zephyr4jiracloud.com/api/v1/automation/job/create"
        self.execute_automation_job_url = "https://prod-vortexapi.zephyr4jiracloud.com/api/v1/automation/job/execute"
        self.zephyrcfg = zephyr_config.dh_zephyr_config
        #self.zephyrcfg = zephyr_config.service_name[service_name]

    def jwt_token_generation(self):
        payload = json.dumps({
            "accessKey": self.zephyrcfg['accessKey'],
            "secretKey": self.zephyrcfg['secretKey'],
            "accountId":  self.zephyrcfg['accountId'],
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", self.token_url, headers=headers, data=payload, verify=False)
        return response.text

    def create_automation_job(self, jwt_token, folder_name):
        file_path = os.getcwd() + "/result.xml"

        payload = {'jobName': self.zephyrcfg['jobName'],
                   'automationFramework': 'Junit',
                   'cycleName': self.zephyrcfg['cycleName'],
                   'folderName': folder_name,
                   'appendDateTimeInCycleName': 'false',
                   'appendDateTimeInFolderName': 'false',
                   'versionName': self.zephyrcfg['releaseCycle'],
                   'projectKey': self.zephyrcfg['projectKey'],
                   'cycleStartingDate': '',
                   'cycleEndingDate': '',
                   'createNewCycle': 'false',
                   'createNewFolder': 'True',
                   'assigneeUser': self.zephyrcfg['assigneeUser'],
                   'jobDescription': self.zephyrcfg['jobDescription']}
        files = [
            ('file', ('result.xml', open(file_path, 'rb'), 'text/xml'))
        ]
        headers = {
            'accessKey': self.zephyrcfg['accessKey'],
            'jwt': jwt_token
        }

        response = requests.request("POST", self.create_automation_job_url,
                                    headers=headers, data=payload, files=files, verify=False)
        return response

    def execute_automation_task(self, job_id, jwt_token):
        payload = {'jobId': job_id}
        files = [

        ]
        headers = {
            'accessKey': self.zephyrcfg['accessKey'],
            'jwt': jwt_token
        }

        response = requests.request("POST", self.execute_automation_job_url, headers=headers, data=payload, files=files,
                                    verify=False)

        return response
