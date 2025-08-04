import requests


class YouGile:

    def __init__(self, url):
        self.url = url

# Получить id компании (или список компаний)
    def get_id_company(self, login, password, name):
        auth = {
            "login": login,
            "password": password,
            "name": name
        }
        resp = requests.post(self.url+'/api-v2/auth/companies', json=auth)
        return resp.json()['content'][0]['id']

# Создать ключ API (будет использоваться в последующих запросах)
    def get_API_key(self, login, password, id_company):
        auth = {
            "login": login,
            "password": password,
            "companyId": id_company
        }

        resp = requests.post(self.url+'/api-v2/auth/keys', json=auth)
        return resp.json()['key']

# Создать проект
    def create_project(self, title, api_key):
        my_json = {
            "title": title
        }
        my_headers = {
            "Authorization": f"Bearer {api_key}"
        }
        resp = requests.post(
            self.url+'/api-v2/projects', json=my_json, headers=my_headers
            )
        return resp.json()

# Изменить компанию
    def edit_project(self, id, title, deleted, api_key):
        my_json = {
            "deleted": deleted,
            "title": title
        }
        my_headers = {
            "Authorization": f"Bearer {api_key}"
        }
        resp = requests.put(
            self.url+'/api-v2/projects/'+str(id),
            json=my_json, headers=my_headers
            )
        return resp.json()

# Получить список компании
    def get_list_projects_id(self, id, api_key):
        my_headers = {
            "Authorization": f"Bearer {api_key}"
        }

        resp = requests.get(
            self.url+'/api-v2/projects/'+str(id), headers=my_headers
            )
        return resp.json()

    def get_list_projects(self, api_key, params_to_add=None):
        my_headers = {
            "Authorization": f"Bearer {api_key}"
        }
        resp = requests.get(
            self.url+'/api-v2/projects',
            headers=my_headers, params=params_to_add
            )
        return resp.json()
