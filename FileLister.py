import sys
import WeoGeoAPI
import json

def main():

    # instantiate the weosession and connect
    # market.weogeo.com gets us the whole public library
    weos = WeoGeoAPI.weoSession('http://market.weogeo.com', 'scitronpousty@gmail.com', 'avimordy')

    # Now we connect to the market
    weos.connectToMarket()

    # if you want to see your connection parameters use this line
    #print weos

    ## Get all the datasets that intersect this box in the public library
    dataSets = weos.getDatasets('JSON', '&north=37.1714&south=37.1012&west=-122.1728&east=-122.0614');

    # Here are a bunch of calls I used to dig into the structure of a returned dataset. Given it's XML origins it
    # has a pretty deeply nested structure. I use the playing around to get to the minimal information I needed to
    # decide which data I wanted

    #print type(dataSets)

    # Get the actual data
    #print dataSets[1]

    # Get the actual dictionary of the data, not the metadata of the query
    dataDict = dataSets[1]

    # Now pull the actual array of datasets
    dataList = dataDict['items'];

    #print json.dumps(dataList[4], sort_keys=True, indent=4)
    #for keys in dataList[0].keys():
    #print keys
    #print type(dataDict['items'])

    # We want token, name, data_type,layers and data coord type (we need this to create bounding box in the native
    # coordinate system.
    for item in dataList:

        #the token is the unique identifier which we use to create a job
        print item['token']
        print item['name']
        print item['data_type']
        print json.dumps(item['layers'])

        #
        print json.dumps(item['boundaries']['data'])
        print ('\n----/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/----\n')

    print "----------\n"
    print "Finished!"


if __name__ == "__main__":
    main()