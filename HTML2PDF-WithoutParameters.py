#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import json, base64, os.path

inputFile = "/home/user/desktop/HTML2PDF/index-WithoutParameters.html"

def sendDevtools(driver, cmd, params={}):
  try:
    resource = "/session/%s/chromium/send_command_and_get_result" % driver.session_id
    url = driver.command_executor._url + resource
    body = json.dumps({'cmd': cmd, 'params': params})
    response = driver.command_executor._request('POST', url, body)

    if response.get('status'):
      raise Exception(response.get('value'))
    
    return response.get('value')
  
  except Exception as error:
    raise ValueError(error)

def saveHtmlAsPDF(path, chromedriver='./chromedriver', print_options = {}, output='generatedPDF-WithoutParameters.pdf'):
    try:
      webdriver_options = Options()
      webdriver_options.add_argument('--headless')
      webdriver_options.add_argument('--disable-gpu')
      driver = webdriver.Chrome(chromedriver, options=webdriver_options)

      if os.path.isfile(path):
      	path = "file:///" + path

      driver.get(path)

      calculated_print_options = {
        'displayHeaderFooter': False,
        'preferCSSPageSize': True,
        'printBackground': True,
        'landscape': False
      }

      calculated_print_options.update(print_options)
      result = sendDevtools(driver, "Page.printToPDF", calculated_print_options)
                 
      with open(output, 'wb') as file:
      	file.write(base64.b64decode(result['data']))

    except Exception as error:
      raise ValueError(error)

    finally:
    	driver.quit()

try:
	saveHtmlAsPDF(inputFile, chromedriver='/usr/bin/chromedriver')

except Exception as error:
	print(error)