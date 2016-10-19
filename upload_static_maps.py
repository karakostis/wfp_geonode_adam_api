

import requests
def upload_static_map(upload_url, login_url, username, password, file_name, file_path, title, source, date):
    c = requests.session()
    # get the csrftoken
    try:
        c.get(login_url)
        csrftoken = c.cookies['csrftoken']
    except:
        msg = "Error retrieving the csrf token"
        return msg
    # login
    try:
        login_data = {
            "username": username,
            "password": password,
            "csrfmiddlewaretoken": csrftoken
        }
        headers_login = {
            'Referer': login_url
        }
        r = c.post(login_url, data=login_data, headers=headers_login)
        sessionid = c.cookies['sessionid']
        #print sessionid
    except:
        msg = "Error login in."
        return msg
    # get new csrf token (changeg after login)
    try:
        r = c.get(upload_url)
        csrftoken = c.cookies['csrftoken']
        #sessionid = c.cookies['sessionid']
    except:
        msg = "Error retrieving the csrf token"
        return msg
    try:
        headers = {
            "Referer": upload_url,
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"
        }
        cookies = {
            "sessionid": sessionid,
            'csrftoken': csrftoken
        }
        #files = {'doc_file': open('/Users/dimitriskarakostis/Desktop/1.png', 'rb')}
        files = {'doc_file': (file_name, open(file_path, 'rb'))}
        payload = {
            'title': title,
            'source': source,
            'date': date,
            'orientation': '0',
            'page_format': '0',
            'keywords': '',
            'permissions': '{"users":{"AnonymousUser":["view_resourcebase"]},"groups":{}}',
            'csrfmiddlewaretoken': csrftoken
        }
        #print payload
        r = c.post(upload_url, files=files, data=payload, headers=headers)
        #print r.headers
        print r.status_code
    except:
        msg = "Error uploading file"
        return msg


msg = upload_static_map("http://staging.geonode.wfp.org/wfpdocs/upload/", "http://staging.geonode.wfp.org/account/login/", "username", "password", "1.png", "/Users/dimitriskarakostis/Desktop/1.png", "aaa3235", "WFP", "2016-10-26 02:13")
print msg
