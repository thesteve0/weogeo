import json
import WeoGeoAPI


__author__ = 'spousty'


def main():

    weos = WeoGeoAPI.weoSession('http://market.weogeo.com', 'scitronpousty@gmail.com', 'avimordy')

    if weos.connectToMarket() is True:

        print "\nstarting\n"

        response = weos.getJobsInCart('JSON')

        print json.dumps(response, indent=4)
        
        response = weos.getJobEvents('921f2d6f-4f21-4238-aa0d-3cb6452a9883','JSON')
        
        print 'Job events:\n'
        
        print json.dumps(response, indent=4)
        
        print "\n Getting Download(s) \n"
        
        response = weos.getDownloadFile("921f2d6f-4f21-4238-aa0d-3cb6452a9883")
        print json.dumps(response, indent=4)


if __name__ == "__main__":
    main()