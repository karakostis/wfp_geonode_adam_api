import requests
import datetime
import dateutil.relativedelta


# The following function logins in geonode, searches for static maps which are posted by ADAM based on a predefined time range. It keeps the latest version (based on the number of the title) and deletes the previous versions. The function is executed through a cronjob.
def delete_static_map(url_2, login_url, username, password):
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
    except:
        msg = "Error login in."
        return msg
    # get new csrf token (changeg after login)

    try:
        r = c.get(url_2)
        csrftoken = c.cookies['csrftoken']
        #sessionid = c.cookies['sessionid']
    except:
        msg = "Error retrieving the csrf token"
        return msg



    try:

        # get current day and time

        today = datetime.date.today()
        startDate = today - datetime.timedelta(days=95)
        endDate = today - datetime.timedelta(days=45)

        url = "https://geonode.wfp.org/trainings/api/v2.4/staticmaps/?limit=300&offset=0&date__range={startDate},{endDate}&title__icontains=Tropical%20Cyclone&keywords__slug__in=tropical-storm".format(** {
            'startDate': startDate,
            'endDate': endDate
        })
        r = c.get(url)
        response_json = r.json()
        # gather all the titles inside a list
        # sort by number its list and get the latest
        events = []
        ts_names = []
        for obj in response_json['objects']:
            events.append( obj['title'] )
            ts_names.append(''.join([obj['title'].split()[:3][2]]))

        ts_names_uniques = list(set(ts_names)) # get unique values of TS by converting list to set
        lists_ts = {key:[] for key in ts_names_uniques}

        for key in ts_names_uniques:
            lists_ts[key] = []
        print lists_ts

        # itterate the list and seperate them in different lists (or dictionaries)
        for whole_name in events:
            for unique_name in ts_names_uniques:
                if unique_name in whole_name:
                    lists_ts[unique_name].append(whole_name)
                    continue

        # put the elements in ascending
        for key, value in lists_ts.iteritems():
            lists_ts[key] = sorted(value, key=lambda x: int(x.rsplit('.', 1)[-1]))

        # collect all title to be deleted, create the filenames (slugified, lowercase, sent the request)
        payload = {
            'csrfmiddlewaretoken': csrftoken
        }

        message = "The following static maps of these Tropical Storm Events (from {startDate} till {endDate}) {ts_names}, will be deleted:".format(** {
            'ts_names': ','.join(ts_names_uniques),
            'startDate': startDate,
            'endDate': endDate
        })
        print(message)
        for key, value in lists_ts.iteritems():
            lists_ts[key] = sorted(value, key=lambda x: int(x.rsplit('.', 1)[-1]))
            if len(lists_ts[key]) > 1: # do not remove element from lists with only one value
                del lists_ts[key][-1]
                for value in lists_ts[key]:
                    if "Warning n." in value:
                        prepare_layer_name = value.replace(".", "").lower()
                        delete_url = "https://geonode.wfp.org/wfpdocs/{layer}/remove".format(** {
                            'layer': prepare_layer_name.replace(" ", "-")
                        })
                        print (value + " - " + delete_url)
                        headers = {
                            "Referer": delete_url,
                            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"
                        }

                        try:
                            # post request!!
                            r = c.post(delete_url, data=payload, headers=headers)
                            if r.status_code != 200:
                                raise Exception()
                        except:
                            print "Error completing the post request with status code {status_code}".format(** {
                                'status_code': r.status_code
                            })

    except:
        msg = "Error retrieving results"
        return msg


msg = delete_static_map("https://geonode.wfp.org/wfpdocs/upload/", "https://geonode.wfp.org/account/login/", "user", "pass")
# print msg
