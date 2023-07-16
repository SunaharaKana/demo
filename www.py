#!/usr/bin/python3
# -*- utf-8 -*-
#
# Copyright (C) 2021-2023 Ken'ichi Fukamachi
#   All rights reserved. This program is free software; you can
#   redistribute it and/or modify it under 2-Clause BSD License.
#   https://opensource.org/licenses/BSD-2-Clause
#
# mailto: fukachan@fml.org
#    web: https://www.fml.org/
# github: https://github.com/fmlorg
#
# $FML: www.py,v 1.7 2023/04/07 06:57:31 fukachan Exp $
# $Revision: 1.7 $
#        NAME: www.py
# DESCRIPTION: a standalone web server based on python3 modules,
#              which is used as a template for our system build exercises.
#              See https://sysbuild-entrance.fml.org/ for more details.
#
import os
import sys
import http.server
import socketserver
import json
import random
import cgi

import boto3

import io
# from PIL import Image, ImageDraw, ExifTags, ImageColor, ImageFont

import sys

#
# Configurations
#
HTTP_HOST       = "0.0.0.0"
HTTP_PORT       = 80
HTDOCS_DIR      = "/home/admin"


# WWW server example: Handler class, which handles www requests
# httpHandler inherits ths superclass http.server.SimpleHTTPRequestHandler
class httpHandler(http.server.SimpleHTTPRequestHandler):
   def __init__(self, *args, **kwargs):
      super().__init__(*args, directory=HTDOCS_DIR, **kwargs)

   def _set_headers(self):
      self.send_response(200)
      self.send_header('Content-type','application/json; charset=utf-8')
      self.send_header('Access-Control-Allow-Origin', '*')
      self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
      self.send_header("Access-Control-Allow-Headers", "X-Requested-With, Access-Control-Allow-Origin")
      self.send_header("Access-Control-Allow-Credentials", "true")
      self.end_headers()

   def do_OPTIONS(self):
      self.send_response(200)
      self.send_header('Access-Control-Allow-Origin', '*')
      self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
      self.send_header("Access-Control-Allow-Headers", "X-Requested-With,Access-Control-Allow-Origin")
      self.send_header("Access-Control-Allow-Credentials", "true")
      self.end_headers()

   def do_GET(self):
      return super().do_GET()

   def do_POST(self):
      self._set_headers()
      data = {}
      if self.path == '/parrot/file/v2':
         print('AAAAAAAAAAAAAAAAAAAA')
         #print(sys.executable)
         data = self.rkg_judge()
         #data = self.kaoninsyou()

      elif self.path == '/parrot/file/v3':
         print('ZZZZZZZZZZZZZZZZZZZZZZZZZZ')
         data = self.custom()

      elif self.path == '/parrot/file/v4':
         print('DDDDDDDDDDDDDDDDDDDDDDDDDD') 
         data = self.kaoninsyou()
           

      message = json.dumps(data, ensure_ascii=False)
      self.wfile.write(bytes(message, "utf8"))


   def jibun(self):
      form = cgi.FieldStorage(
          fp=self.rfile,
          headers=self.headers,
          environ={'REQUEST_METHOD':'POST'}
          )
      key = form.getvalue("jibun")
      jibun = int(key) 
      return jibun  

   def aite(self):
      return random.randrange(3)

   def janken(self):
      ji = self.jibun()
      ai = self.aite()
      data = {"jibun":ji,"aite":ai,"kekka":(3+ji-ai)%3}
      return data


   def rkg_judge(self):
       print("CCCCCCCCCCCCCCCCCCCCCCCCC")
       form = cgi.FieldStorage(
               fp=self.rfile,
               headers=self.headers,
               environ={'REQUEST_METHOD': 'POST'}
               )

       # 変数 body に、CGI経由で渡されたファイルの"中身"を代入
       body = form.getvalue("jibun")

       
       # ... CGI経由でア?��?プロードしたファイルを変数body??��?��メモリ上）に読み込む...

       client = boto3.client('rekognition','us-east-1')
       print(type(body))
       response = client.detect_labels(
               Image = {
                   'Bytes': body
                   }
               )
        
       # return response
   

       response2 = response['Labels']
       response3 = response2[0]
       response4 = response3['Name']
       
       print('CCCCCCCCCCCCCCCCCCCCCCCCCC')
       print(response4)
       ji = 3
       

       if response4 == 'Rock':
            ji =  0
       elif response4 == 'Scissors':
            ji =  1
       elif response4 == 'Paper':
            ji =  2
      
       print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
       ai = self.aite()
       print('BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB')
       data = {'jibun':ji,'aite':ai,'kekka':(3+ji-ai)%3}
       return data

     
        
   def custom(self):
       print('BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB')
       form = cgi.FieldStorage(
               fp=self.rfile,
               headers=self.headers,
               environ={'REQUEST_METHOD': 'POST'}
               )

       # 変数 body に、CGI経由で渡されたファイルの"中身"を代入
       body = form.getvalue("jibun2")

       
       # ... CGI経由でア?��?プロードしたファイルを変数body??��?��メモリ上）に読み込む...

       client = boto3.client('rekognition','us-east-1')
       print(type(body))
       print('YYYYYYYYYYYYYYYYYYYYYYYYYY')
       response = client.detect_custom_labels(
               Image = {
               'Bytes': body
                 },
               #Image = {'S3Object': {'Bucket': 'custom-labels-console-us-east-1-1ba4b7a349', 'Name': 'グー1.jpg'}},
               MinConfidence=40,
               ProjectVersionArn='arn:aws:rekognition:us-east-1:433161940860:project/Janken3/version/Janken3.2023-05-27T19.31.43/1685183503633'
               )
       print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')        
       print(response)
       return response

   def kaoninsyou(self):
      print('EEEEEEEEEEEEEEEEEEEEEEEEEEE')

      form = cgi.FieldStorage(
               fp=self.rfile,
               headers=self.headers,
               environ={'REQUEST_METHOD': 'POST'}
               )

       # 変数 body に、CGI経由で渡されたファイルの"中身"を代入
      body = form.getvalue("jibun3")

       
       # ... CGI経由でア?��?プロードしたファイルを変数body??��?��メモリ上）に読み込む...

      client = boto3.client('rekognition','us-east-1')
      print(type(body))

      print('FFFFFFFFFFFFFFFFFFFFFFFFFFFF')
      response = client.compare_faces(
   
         SourceImage={
			   'Bytes': body
		      },
		   TargetImage={
			   "S3Object": {
				   "Bucket": 'kaoninsyou',
				   "Name": 'sunahara1.jpg',
			   }
		      },
            SimilarityThreshold= 0
                        
               )

      # return response    

      response2 = response['FaceMatches'][0]
      response3 = response2['Similarity']

      if response3 >= 90:
         return {'facial recognition': 'success'} 
      else:
         return {'facial recognition': 'failure'}      



   def openbd(self):
      pass

   def db_connect(self):
      pass

   def db_insert(self, jibun, aite, kekka):
      connection            = self.db_connect()
      connection.autocommit = True

      pass

      connection.close

   def db_show(self):
      connection            = self.db_connect()
      connection.autocommit = True

      pass

      connection.close


#
# MAIN
#
if __name__ == "__main__":
   # run python www server (httpd)
   with socketserver.TCPServer((HTTP_HOST, HTTP_PORT), httpHandler) as httpd:
      print("(debug) serving at port", HTTP_PORT, file=sys.stderr)
      httpd.serve_forever()
