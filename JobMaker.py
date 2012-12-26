__author__ = 'spousty'

import WeoGeoAPI
import json


def main():

    print "making jobs"

    # Alright, we need to make an order for each dataset we want and we need to add it to our cart.
    # For the meaning of the different pieces of the Job please refer to "create a job" on the following
    # page:  http://www.weogeo.com/developer_doc/Jobs_API.html

    # DRGs are a raster images which are scans of the USGS Topo sheets - we will use this as a backdrop
    drgOrder = {

        # may be either true or false
        "cart" : "true",
        "job" :
            {
                # This corresponds to the token from the listing we did before
                "dataset_token" : "f1bca22c-013e-4e57-a78b-f9bbb3a918e8",

                # must be 1 or it will not be accepted
                "content_license_acceptance" : "1",

                "parameters":
                    {
                        "job_geocrop" : "Clip",
                        #all of the coordinates must in the native coords of the data layer,
                        # NOT in our projected coord system
                        "job_north": "-96662.277645466 ",
                        "job_south": "-112947.414047391 ",
                        "job_east" : "-176976.959816694 ",
                        "job_west" : "-189395.961743919 ",
                        "job_layers": "layer_1",
                        "job_datum_projection" : "EPSG:4326",

                        # FME name for file format
                        "job_file_format": "PNG",

                        # raster only - this seems to correspond to the level of compression used on the image
                        "job_spatial_resolution": "1"
                    }
            }
    }

    # Add the job we just created to a List which will contain all orders
    jobOrders = [drgOrder]

    # Next job will be the vector data from the US Census - TIGER/Line - Santa Cruz County, California
    landmarkOrder = {
        "cart" : "true",
        "job" :
            {
                "dataset_token" : "63472b72-0f0d-2554-8120-67b445942ff7",
                "content_license_acceptance" : "1",
                "parameters":
                    {
                        "job_geocrop" : "Clip",
                        "job_north": "37.1714 ",
                        "job_south": "37.1012 ",
                        "job_east" : "-122.1728 ",
                        "job_west" : "-122.0614 ",
                        # We are grabbing all the landmarks from this census dataset
                        "job_layers": "Point Landmark;Area Landmark",
                        "job_datum_projection" : "EPSG:4326",
                        "job_file_format": "SHAPEFILE",
                    }

            }

    }

    censusOrder = {
        "cart" : "true",
        "job" :
            {
                "dataset_token" : "85da9c3d-a58b-9b5f-9c59-f324f4d4d186",
                "content_license_acceptance" : "1",
                "parameters":
                    {
                        "job_geocrop" : "Clip",
                        "job_north": "37.1714 ",
                        "job_south": "37.1012 ",
                        "job_east" : "-122.1728 ",
                        "job_west" : "-122.0614 ",
                        # We are grabbing all the landmarks from this census dataset
                        "job_layers": "Census Block Group;Census Block;Census Tract;Tribal Block Group;Tribal Census Tract",
                        "job_datum_projection" : "EPSG:4326",
                        "job_file_format": "SHAPEFILE",
                        }

            }

    }

    votingOrder = {
        "cart" : "true",
        "job" :
            {
                "dataset_token" : "1a9f8125-cd90-ef5a-9c16-c3329fb51497",
                "content_license_acceptance" : "1",
                "parameters":
                    {
                        "job_geocrop" : "Clip",
                        "job_north": "37.1714 ",
                        "job_south": "37.1012 ",
                        "job_east" : "-122.1728 ",
                        "job_west" : "-122.0614 ",
                        # We are grabbing all the landmarks from this census dataset
                        "job_layers": "State Legislative District--Lower Chamber;tate Legislative District--Upper Chamber;Place",
                        "job_datum_projection" : "EPSG:4326",
                        "job_file_format": "SHAPEFILE",
                        }

            }

    }

    zipOrder = {
        "cart" : "true",
        "job" :
            {
                "dataset_token" : "5c910ad3-fc69-4023-b180-8c862639eadb",
                "content_license_acceptance" : "1",
                "parameters":
                    {
                        "job_geocrop" : "Clip",
                        "job_north": "37.1714 ",
                        "job_south": "37.1012 ",
                        "job_east" : "-122.1728 ",
                        "job_west" : "-122.0614 ",
                        # We are grabbing all the landmarks from this census dataset
                        "job_layers": "Layer_1",
                        "job_datum_projection" : "EPSG:4326",
                        "job_file_format": "SHAPEFILE",
                        }

            }

    }

    schoolOrder = {
        "cart" : "true",
        "job" :
            {
                "dataset_token" : "1a4d4a22-d84b-4cb3-b874-1a99bf6d42eb",
                "content_license_acceptance" : "1",
                "parameters":
                    {
                        "job_geocrop" : "Clip",
                        "job_north": "37.1714 ",
                        "job_south": "37.1012 ",
                        "job_east" : "-122.1728 ",
                        "job_west" : "-122.0614 ",
                        # We are grabbing all the landmarks from this census dataset
                        "job_layers": "School District--Elementary;School District--Secondary;School District--Unified",
                        "job_datum_projection" : "EPSG:4326",
                        "job_file_format": "SHAPEFILE",
                        }

            }

    }

    transOrder = {
        "cart" : "true",
        "job" :
            {
                "dataset_token" : "fd732c1b-880b-4ea2-ac4e-60e8f95d677f",
                "content_license_acceptance" : "1",
                "parameters":
                    {
                        "job_geocrop" : "Clip",
                        "job_north": "37.1714 ",
                        "job_south": "37.1012 ",
                        "job_east" : "-122.1728 ",
                        "job_west" : "-122.0614 ",
                        # We are grabbing all the landmarks from this census dataset
                        "job_layers": "Primary Roads;Primary and Secondary Roads;All Roads;Rails",
                        "job_datum_projection" : "EPSG:4326",
                        "job_file_format": "SHAPEFILE",
                        }

            }

    }

    waterOrder = {
        "cart" : "true",
        "job" :
            {
                "dataset_token" : "e1f0bcce-30cb-4890-81e2-e5e768c7ddfa",
                "content_license_acceptance" : "1",
                "parameters":
                    {
                        "job_geocrop" : "Clip",
                        "job_north": "37.1714 ",
                        "job_south": "37.1012 ",
                        "job_east" : "-122.1728 ",
                        "job_west" : "-122.0614 ",
                        # We are grabbing all the landmarks from this census dataset
                        "job_layers": "Area Hydrography;Linear Hydrography",
                        "job_datum_projection" : "EPSG:4326",
                        "job_file_format": "SHAPEFILE",
                        }

            }

    }

    jobOrders.append(landmarkOrder)
    jobOrders.append(censusOrder)
    jobOrders.append(votingOrder)
    jobOrders.append(zipOrder)
    jobOrders.append(schoolOrder)
    jobOrders.append(transOrder)
    jobOrders.append(waterOrder)

    weos = WeoGeoAPI.weoSession('http://market.weogeo.com', 'scitronpousty@gmail.com', 'avimordy')

    if weos.connectToMarket() is True:

        print "\nSubmitting your jobs...\n"

        for job in jobOrders:
            weos.createJob(job, 'JSON')
            print "Here is your order info:\n"
            print json.dumps(job, indent=4)

        print "\nfinished creating jobs - now to order!\n"
        #weoJobOrder = weos.orderJobsInCart('', 'JSON')
        #print json.dumps(weoJobOrder, indent=4)

        print "\n\n ---Finished---\n"


if __name__ == "__main__":
    main()