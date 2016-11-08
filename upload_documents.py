import requests
def upload_documents(upload_url, login_url, username, password, file_name,
                      file_path, title):
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
        }
        cookies = {
            "sessionid": sessionid,
            'csrftoken': csrftoken
        }
        #files = {'doc_file': open('/Users/dimitriskarakostis/Desktop/1.png', 'rb')}
        files = {'doc_file': (file_name, open(file_path, 'rb'))}
        payload = {
            'title': title,
            'permissions': '{"users":{"AnonymousUser":["view_resourcebase","download_resourcebase"]},"groups":{}}',
            'csrfmiddlewaretoken': csrftoken
        }
        # print payload
        # print r.status_code
        r = c.post(upload_url, files=files, data=payload, headers=headers)
        # print r.url
        msg = r.url.replace('metadata', 'download')
        return msg
    except:
        msg = "Error uploading file"
        return msg


msg = upload_documents("http://staging.geonode.wfp.org/documents/upload", "http://staging.geonode.wfp.org/account/login/", "dimitris.karakostis", "1234", "image_magick.txt", "/Users/dimitriskarakostis/Desktop/image_magick.txt", "title")
# print msg
