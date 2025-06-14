import requests
from logger_config import logger
from requests.auth import HTTPDigestAuth
from datetime import datetime, timezone
import json
class HikVision():
    def __init__(self, api_url,username, password):
        self.user = username
        self.password = password
        self.api_url = api_url

    
    def enroll_user(self,user):
        userData = self.format_user_data(user)
        url_enroll = f"{self.api_url}/ISAPI/AccessControl/UserInfo/Record?format=json"
        try:
            response_enroller = requests.post(
                url_enroll,
                headers={},
                data= json.dumps(userData),
                auth=HTTPDigestAuth(self.user, self.password),
                verify=False
            )
            if response_enroller.status_code == 200:
                return True
            else:
                logger.error(f"Error al enviar solicitud de inscripcion: {response_enroller.status_code} - {response_enroller.text}")
                return False
        except requests.exceptions.RequestException as e:
            logger.error(f"Error al enviar solicitud de inscripcion: {e}")
            return False
    
    def update_days(self,user):
        userData = self.format_user_data(user)
        url_enroll = f"{self.api_url}/ISAPI/AccessControl/UserInfo/Modify?format=json"
        try:
            response_enroller = requests.put(
                url_enroll,
                headers={},
                data= json.dumps(userData),
                auth=HTTPDigestAuth(self.user, self.password),
                verify=False
            )
            if response_enroller.status_code == 200:
                return True
            else:
                logger.error(f"Error al enviar solicitud de inscripcion: {response_enroller.status_code} - {response_enroller.text}")
                return False
        except requests.exceptions.RequestException as e:
            logger.error(f"Error al enviar solicitud de inscripcion: {e}")
            return False
    
    def format_user_data(self, user):
        name = user['name']+' '+user['lastname']
        start_date = datetime.strptime(user['start_date'], "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc)
        end_date = datetime.strptime(user['end_date'], "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc)
        user_data = {
                "UserInfo": {
                    "employeeNo": str(user['user_id']),
                    "name": name,
                    "userType": "normal",
                    "Valid": {
                        "enable": True,
                        "beginTime": start_date.strftime("%Y-%m-%dT%H:%M:%S"),
                        "endTime": end_date.strftime("%Y-%m-%dT%H:%M:%S"),
                        "timeType": "local"
                    },
                    "doorRight": "1",
                    "RightPlan": [{"doorNo": 1, "planTemplateNo": "1"}],
                    "gender": 'male',
                    "localUIRight": False,
                    "maxOpenDoorTime": 0,
                    "userVerifyMode": "",
                    "groupId": 1,
                    "userLevel": "Employee",
                    "localPassword": ""
                }
            }
        return user_data
