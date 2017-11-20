#!/usr/bin/python

import os
import json
import sys

count_links = 0

if(len(sys.argv) == 2):
    print("==================================================")
    for root, dirs, files in os.walk("."):
        path = root.split(os.sep)
        if "SlackFileDownloads" not in path:
            for directory_file_name in files:
                if ".json" in directory_file_name:
                    file_path = "/".join(path) + "/" + directory_file_name
                    with open(file_path) as f:
                        try:
                            parsed_json = json.load(f)
                            for message in parsed_json:
                                try:
                                    download_url = message["file"]["url_private_download"]

                                    print(count_links)
                                    print("==================================================")

                                    print("Download URL: \t\t%s" % download_url)

                                    download_file_id = message["file"]["id"]
                                    print("Download ID: \t\t%s" % download_file_id)

                                    download_file_name = download_url.split("?t")[0].split("/")[-1]
                                    print("File name: \t\t%s" % download_file_name)

                                    output_file_name = download_file_id + "-" + download_file_name
                                    print("Output name: \t\t%s" % output_file_name)

                                    output_dir = "SlackFileDownloads" + "/".join(path).replace(".", "", 1)
                                    print("Output directory: \t%s" % output_dir)

                                    os.system("mkdir -p " + output_dir)

                                    print("Source json file: \t%s" % file_path)

                                    command = 'wget -O "%s/%s" "%s"' % (output_dir, output_file_name, download_url)
                                    print("Command: \t\t%s" % command)

                                    if(sys.argv[1].lower() == "download"):
                                        print("***** DOWNLOADING! *****")
                                        #os.system(command)
                                    print("==================================================")
                                    count_links += 1
                                except:
                                    pass
                        except:
                            pass

    print("Number of download links: %s" % count_links)

else:
    print("Usage: python scrape.py [list/download]\nOptions:\n\tlist: lists all files to be downloaded\n\tdownload: download the files")
