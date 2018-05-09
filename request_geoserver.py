import requests
from geoserver.catalog import Catalog

## Instructions to execute this script
# 1. decide for which continent you want to execute it and replace the value in for loop with the corresponding list. Also replace the table_name attribute with the corresponding table
# 2. if you run the script for roads (not streets) then the layer_name attribute is: _trs_roads_osm but if you run it for streets then it is "_trs_streets_osm". Also for roads the query inside the xml should be as WHERE fclass in (1,2,3,4,6)  but if you run it for streets then it is WHERE fclass in (5,7)
# Execute the script once. Then comment the lines which create the layers and uncomment the ones which assign styles. Again if you run the script for roads the _set_default_style is road_functional_class while for streets osm_streets_pathways
# In case you make mistakes use the section: "delete layers in case of messup" to remove layers from geoserver


# access geoserver
cat = Catalog("http://ogcserver.gis.wfp.org/geoserver/rest", "admin", "osm_sparc_2017")

headers = {
    'Content-type': 'text/xml',
}


layers_to_be_created_asia = ['UZB','AZE','GEO','TKM','AFG','PAK','NPL','MMR','LAO','KHM','THA','IDN','VUT','FJI','SLB','LKA','PRK']


layers_to_be_created_africa = ['BLZ','GHA','STP','TGO','NER','MLI','BEN','GNB','CPV','KEN','BDI','SOM','DJI','RWA','TZA','AGO','LSO','NAM','SWZ','MWI','MOZ','ZMB','ZWE']


layers_to_be_created_southamerica = ['DOM','VEN','COL','ECU','HTI','GTM','PAN','PRY','PER','CHL','NIC','HND','DMA','BOL','CUB','SLV']


#layers_to_be_created = ['BLZ','DOM']

for iso in layers_to_be_created_asia: #!!! change the list based on the continent you want to create data
    table_name = 'asp_trs_roads_osm'  # !!change the table name based on the continent (asp_trs_roads_osm -> asia, afr_trs_roads_osm -> africa, lac_trs_roads_osm -> latin america)
    layer_name = iso.lower() + "_trs_roads_osm"
    layer_exist = cat.get_layer(layer_name)


    # delete layers in case of messup
    '''
    url = "http://ogcserver.gis.wfp.org/geoserver/rest/layers/geonode:{layer_name}.xml".format(** {
        'layer_name': layer_name,
    })
    response = requests.delete(url, auth=('admin', 'osm_sparc_2017'))

    print response.status_code

    url = "http://ogcserver.gis.wfp.org/geoserver/rest/workspaces/geonode/datastores/osm_prod/featuretypes/{layer_name}.xml".format(** {
        'layer_name': layer_name,
    })
    response = requests.delete(url, auth=('admin', 'osm_sparc_2017'))

    print response.status_code
    '''

    # section to create the layers
    if not layer_exist:
        xml = "<featureType><name>{layername}</name><nativeName>{layername}</nativeName><namespace><name>geonode</name><atom:link xmlns:atom='http://www.w3.org/2005/Atom' rel='alternate' href='http://ogcserver.gis.wfp.org/geoserver/rest/namespaces/geonode.xml' type='application/xml'/></namespace><title>{layername}</title><keywords><string>features</string><string>{layername}</string></keywords><nativeCRS>EPSG:4326</nativeCRS><srs>EPSG:4326</srs><projectionPolicy>FORCE_DECLARED</projectionPolicy><enabled>true</enabled><metadata><entry key='JDBC_VIRTUAL_TABLE'><virtualTable><name>{layername}</name><sql>SELECT * FROM osm.{table} WHERE fclass in (1,2,3,4,6) AND iso3 = '{iso}'</sql><escapeSql>false</escapeSql><geometry><name>geometry</name><type>LineString</type><srid>4326</srid></geometry></virtualTable></entry><entry key='cachingEnabled'>false</entry></metadata><store class='dataStore'><name>geonode:osm_prod</name><atom:link xmlns:atom='http://www.w3.org/2005/Atom' rel='alternate' href='http://ogcserver.gis.wfp.org/geoserver/rest/workspaces/geonode/datastores/osm_prod.xml' type='application/xml'/></store><maxFeatures>0</maxFeatures><numDecimals>0</numDecimals><overridingServiceSRS>false</overridingServiceSRS><skipNumberMatched>false</skipNumberMatched><circularArcPresent>false</circularArcPresent></featureType>".format(** {
            'layername': layer_name,
            'iso': iso,
            'table': table_name
        })

        response = requests.post('http://ogcserver.gis.wfp.org/geoserver/rest/workspaces/geonode/datastores/osm_prod/featuretypes/', headers=headers, data=xml, auth=('admin', 'osm_sparc_2017'))

        print response.status_code
        print response.text
    else:
        print "layer already exists"


    # section to assign the styles to the layers
    '''
    layer_exist = cat.get_layer(layer_name)
    if layer_exist: # assign the default style
        layer_exist._set_default_style("road_functional_class")
        cat.save(layer_exist)
        print True
    else: # if not add it to the list
        no_style_assigned.append(layer_name)
        print False
    '''
