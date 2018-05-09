import requests
def upload_documents(login_url, username, password):
    c = requests.session()
    # get the csrftoken
    try:
        c.get(login_url)
        csrftoken = c.cookies['csrftoken']
        print ("csrftoken", csrftoken)
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
        print ("logindata", login_data)
        headers_login = {
            'Referer': login_url
        }
        print (headers_login)
        r = c.post(login_url, data=login_data, headers=headers_login)
        print r.status_code
        sessionid = c.cookies['sessionid']

    except:
        msg = "Error login in."
        return msg
    # get new csrf token (changeg after login)
    try:

        r = c.get(login_url)
        csrftoken = c.cookies['csrftoken']
        print ("csrftoken", csrftoken)
        #sessionid = c.cookies['sessionid']
    except:
        msg = "Error retrieving the csrf token"
        return msg
    try:


        layers_to_be_created = ['Uzbekistan','Azerbaijan','Georgia','Turkmenistan','Afghanistan','Pakistan','Nepal','Myanmar','Laos','Cambodia ','Thailand','Indonesia','Vanuatu','Fiji','Solomon Islands','Sri Lanka','North Korea']

        layers_iso_to_be_created = ['UZB','AZE','GEO','TKM','AFG','PAK','NPL','MMR','LAO','KHM','THA','IDN','VUT','FJI','SLB','LKA','PRK']


        #layers_iso_to_be_created = ['BLZ','GHA','STP','TGO','NER','MLI','BEN','GNB','CPV','KEN','BDI','SOM','DJI','RWA','TZA','AGO','LSO','NAM','SWZ','MWI','MOZ','ZMB','ZWE']

        #layers_to_be_created = ['Belize','Ghana','Sao Tome and Principe','Togo','Niger','Mali','Benin','Guinea-Bissau','Cape Verde','Kenya','Burundi','Somalia','Djibouti','Rwanda','Tanzania','Angola','Lesotho','Namibia','Swaziland','Malawi','Mozambique','Zambia','Zimbabwe']

        #layers_to_be_created = ['Dominican Republic','Venezuela','Colombia','Ecuador','Haiti','Guatemala','Panama','Paraguay','Peru','Chile','Nicaragua','Honduras','Dominica','Bolivia','Cuba','El Salvador']
        #layers_iso_to_be_created = ['DOM','VEN','COL','ECU','HTI','GTM','PAN','PRY','PER','CHL','NIC','HND','DMA','BOL','CUB','SLV']






        for counter, cnt_name in enumerate(layers_to_be_created):

            iso = layers_iso_to_be_created[counter]
            layer_name = (iso + "_trs_streets_osm").lower()
            update_meta_url = 'https://geonode.wfp.org/layers/ogcserver.gis.wfp.org%3Ageonode%3A{layer_name}/metadata'.format(** {
                'layer_name': layer_name,
            })

            headers = {
                "Referer": update_meta_url,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
                "Content-Type": "application/x-www-form-urlencoded",
                "Connection": "keep-alive",
                "Cache-Control": "no-cache",
            }



            resource_abstract = "This dataset is an extraction of streets and pathways from OpenStreetMap data made by WFP that follow UNSDIT standards. The data is updated in near-real time from OSM servers and include all latest updates. NOTE: this dataset doesn't include main roads that have been published on a separate dataset (main roads).\n\n More documentation on the whole process for extracting OpenStreetMap roads can be found here: https://geonode.wfp.org/documents/6823/download"


            resource_title = '{country_name}  streets and pathways'.format(** {
                'country_name': cnt_name,
            })


            #print headers
            files = {}
            payload = {
                'csrfmiddlewaretoken': csrftoken,
                'resource-owner-autocomplete':'',
                'resource-owner':'12',
                'resource-title':resource_title,
                'resource-date':'2018-05-08 12:21',
                'resource-abstract':resource_abstract,
                'resource-keywords':'open street map, logistics, roads',
                'resource-poc-autocomplete':'',
                'resource-poc':'12',
                'resource-metadata_author-autocomplete':'',
                'resource-metadata_author':'12',
                'resource-date_type':'publication',
                'resource-edition':'',
                'resource-purpose':'',
                'resource-maintenance_frequency':'continual',
                'resource-restriction_code_type':'',
                'resource-constraints_other':'',
                'resource-license':'6',
                'resource-language':'eng',
                'resource-spatial_representation_type':'1',
                'resource-temporal_extent_start':'',
                'resource-temporal_extent_end':'',
                'resource-supplemental_information':'No information provided',
                'resource-distribution_url':update_meta_url,
                'resource-distribution_description':'Web address (URL)',
                'resource-data_quality_statement':'',
                'resource-is_published':'on',
                'resource-thumbnail_url':'',
                'category_choice_field':'16',
                'layer_attribute_set-TOTAL_FORMS':' 21',
                'layer_attribute_set-INITIAL_FORMS':' 21',
                'layer_attribute_set-MAX_NUM_FORMS':' 1000',
                'layer_attribute_set-0-id':' 57366',
                'layer_attribute_set-0-attribute':' id',
                'layer_attribute_set-0-attribute_label':' ',
                'layer_attribute_set-0-description':' ',
                'layer_attribute_set-0-display_order':' 1',
                'layer_attribute_set-1-id':' 57367',
                'layer_attribute_set-1-attribute':' osm_id',
                'layer_attribute_set-1-attribute_label':'osm id',
                'layer_attribute_set-1-description':' ',
                'layer_attribute_set-1-display_order':' 2',
                'layer_attribute_set-2-id':' 57368',
                'layer_attribute_set-2-attribute':' sourceid',
                'layer_attribute_set-2-attribute_label':' ',
                'layer_attribute_set-2-description':' ',
                'layer_attribute_set-2-display_order':' 3',
                'layer_attribute_set-3-id':' 57369',
                'layer_attribute_set-3-attribute':' notes',
                'layer_attribute_set-3-attribute_label':' ',
                'layer_attribute_set-3-description':' ',
                'layer_attribute_set-3-display_order':' 4',
                'layer_attribute_set-4-id':' 57370',
                'layer_attribute_set-4-attribute':' onme',
                'layer_attribute_set-4-attribute_label':' ',
                'layer_attribute_set-4-description':' ',
                'layer_attribute_set-4-display_order':' 5',
                'layer_attribute_set-5-id':' 57371',
                'layer_attribute_set-5-attribute':' rtenme',
                'layer_attribute_set-5-attribute_label':' ',
                'layer_attribute_set-5-description':' ',
                'layer_attribute_set-5-display_order':' 6',
                'layer_attribute_set-6-id':' 57372',
                'layer_attribute_set-6-attribute':' ntlclass',
                'layer_attribute_set-6-attribute_label':' ',
                'layer_attribute_set-6-description':' ',
                'layer_attribute_set-6-display_order':' 7',
                'layer_attribute_set-7-id':' 57373',
                'layer_attribute_set-7-attribute':' fclass',
                'layer_attribute_set-7-attribute_label':' ',
                'layer_attribute_set-7-description':' ',
                'layer_attribute_set-7-display_order':' 8',
                'layer_attribute_set-8-id':' 57374',
                'layer_attribute_set-8-attribute':' numlanes',
                'layer_attribute_set-8-attribute_label':' ',
                'layer_attribute_set-8-description':' ',
                'layer_attribute_set-8-display_order':' 9',
                'layer_attribute_set-9-id':' 57375',
                'layer_attribute_set-9-attribute':' srftpe',
                'layer_attribute_set-9-attribute_label':' ',
                'layer_attribute_set-9-description':' ',
                'layer_attribute_set-9-display_order':' 10',
                'layer_attribute_set-10-id':' 57376',
                'layer_attribute_set-10-attribute':' srfcond',
                'layer_attribute_set-10-attribute_label':' ',
                'layer_attribute_set-10-description':' ',
                'layer_attribute_set-10-display_order':' 11',
                'layer_attribute_set-11-id':' 57377',
                'layer_attribute_set-11-attribute':' isseasonal',
                'layer_attribute_set-11-attribute_label':' ',
                'layer_attribute_set-11-description':' ',
                'layer_attribute_set-11-display_order':' 12',
                'layer_attribute_set-12-id':' 57378',
                'layer_attribute_set-12-attribute':' curntprac',
                'layer_attribute_set-12-attribute_label':' ',
                'layer_attribute_set-12-description':' ',
                'layer_attribute_set-12-display_order':' 13',
                'layer_attribute_set-13-id':' 57379',
                'layer_attribute_set-13-attribute':' gnralspeed',
                'layer_attribute_set-13-attribute_label':' ',
                'layer_attribute_set-13-description':' ',
                'layer_attribute_set-13-display_order':' 14',
                'layer_attribute_set-14-id':' 57380',
                'layer_attribute_set-14-attribute':' rdwidthm',
                'layer_attribute_set-14-attribute_label':' ',
                'layer_attribute_set-14-description':' ',
                'layer_attribute_set-14-display_order':' 15',
                'layer_attribute_set-15-id':' 57381',
                'layer_attribute_set-15-attribute':' status',
                'layer_attribute_set-15-attribute_label':' ',
                'layer_attribute_set-15-description':' ',
                'layer_attribute_set-15-display_order':' 16',
                'layer_attribute_set-16-id':' 57382',
                'layer_attribute_set-16-attribute':' iselevated',
                'layer_attribute_set-16-attribute_label':' ',
                'layer_attribute_set-16-description':' ',
                'layer_attribute_set-16-display_order':' 17',
                'layer_attribute_set-17-id':' 57383',
                'layer_attribute_set-17-attribute':' iso3',
                'layer_attribute_set-17-attribute_label':' ',
                'layer_attribute_set-17-description':' ',
                'layer_attribute_set-17-display_order':' 18',
                'layer_attribute_set-18-id':' 57384',
                'layer_attribute_set-18-attribute':' country',
                'layer_attribute_set-18-attribute_label':' ',
                'layer_attribute_set-18-description':' ',
                'layer_attribute_set-18-display_order':' 19',
                'layer_attribute_set-19-id':' 57385',
                'layer_attribute_set-19-attribute':' last_update',
                'layer_attribute_set-19-attribute_label':' ',
                'layer_attribute_set-19-description':' ',
                'layer_attribute_set-19-display_order':' 20',
                'layer_attribute_set-20-id':' 57386',
                'layer_attribute_set-20-attribute':' geometry',
                'layer_attribute_set-20-attribute_label':' ',
                'layer_attribute_set-20-description':' ',
                'layer_attribute_set-20-display_order':' 21',
                'poc-first_name':' ',
                'poc-last_name':' ',
                'poc-email':' ',
                'poc-organization':' ',
                'poc-profile':' ',
                'poc-position':' ',
                'poc-voice':' ',
                'poc-fax':' ',
                'poc-delivery':' ',
                'poc-city':' ',
                'poc-area':' ',
                'poc-zipcode':' ',
                'poc-country':' ',
                'poc-keywords':' ',
                'author-first_name':' ',
                'author-last_name':' ',
                'author-email':' ',
                'author-organization':' ',
                'author-profile':' ',
                'author-position':' ',
                'author-voice':' ',
                'author-fax':' ',
                'author-delivery':' ',
                'author-city':' ',
                'author-area':' ',
                'author-zipcode':' ',
                'author-country':' ',
                'author-keywords':' '
            }
            #print payload
            # print r.status_code
            r = c.post(update_meta_url, files=files, data=payload, headers=headers)
            #print r.url
            print r.status_code
            #print r.headers
            #msg = r.url.replace('metadata', 'download')
            #return msg
    except:
        msg = "Error updating metadata"
        return msg


msg = upload_documents("https://geonode.wfp.org/account/login/", "user", "pass")
#print msg
