import base64
from urllib import request
from urllib import parse
from urllib.request import urlopen
import cv2
import os
import json
import time

'''
Human key point recognition
'''

#
# Declare some parameters.
#
request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_analysis"
access_token = '24.e80453bdcdaf5d05c00cc769d9670d46.2592000.1567151284.282335-16925978'
request_url = request_url + "?access_token=" + access_token


#
# Open image and convert to base64, get the skeleton point after calling api and mark them on image.
# Then save them.
#

def label_bone(img_intput_path, img_output_path):
    try:
        # Binary way to open image files.
        f = open(img_intput_path, 'rb')
        img = base64.b64encode(f.read())
        params = {"image": img}
        params = parse.urlencode(params).encode('utf-8')

        # Send a post request for getting content.
        post = request.Request(request_url, params)
        post.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urlopen(post)
        content = eval(response.read())  # Convert binary content to dict.

        if content:
            print(content)

        # write content to json file.
        filename = os.path.basename(img_intput_path)
        jsonname = os.path.splitext(filename)[0]
        with open('jsondic1/' + jsonname + '.json', 'w') as f:
            json.dump(content, f)

        # Extract Skeleton_points from content and save them to Skeleton_points.
        body_parts = content['person_info'][0]['body_parts']
        Skeleton_points = []
        for item in body_parts.items():
            point = [item[1]['y'], item[1]['x']]  # Point[y,x]
            Skeleton_points.append(point)
        print(Skeleton_points)

        # Draw bone points on the original image.
        img = cv2.imread(img_intput_path)
        for i in Skeleton_points:
            cv2.circle(img, (int(i[1]), int(i[0])), 3, color=(112, 25, 25), thickness=-1)
        # write img as jpg.
        cv2.imwrite(img_output_path, img)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    for i in os.listdir('data1'):
        print(i)
        label_bone('data1/{}'.format(i), 'data_output1/{}'.format(i))
        time.sleep(1)
