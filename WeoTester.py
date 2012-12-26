import json
import WeoGeoAPI


__author__ = 'spousty'


def main():

    weos = WeoGeoAPI.weoSession('http://market.weogeo.com', 'scitronpousty@gmail.com', 'avimordy')

    if weos.connectToMarket() is True:

        print "\nstarting\n"

        response = weos.getJobsInCart('JSON')

        print json.dumps(response, indent=4)

if __name__ == "__main__":
    main()