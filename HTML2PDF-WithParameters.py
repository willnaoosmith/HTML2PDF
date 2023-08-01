#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from selenium.webdriver.chrome.options import Options
import json, base64, os, jinja2
from selenium import webdriver
from datetime import datetime

templateEnviroment = jinja2.Environment(loader=jinja2.FileSystemLoader('./'))
inputFile = "index-WithParameters.html"

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

def saveHtmlAsPDF(path, chromedriver='./chromedriver', print_options = {}, output='generatedPDF-WithParameters.pdf'):
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
  template = templateEnviroment.get_template(inputFile)

  context = {
    "currentDate": datetime.now().strftime("%Y-%m-%d")
  }

  generatedTemplate = template.render(context)

  with open("generatedTemplate-WithParameters.html", "w") as outputFile:
    outputFile.write(generatedTemplate)    
    outputFile.close()

  saveHtmlAsPDF(f"{os.getcwd()}/generatedTemplate-WithParameters.html", chromedriver='/usr/bin/chromedriver')

except Exception as error:
	print(error)

finally:
  try:
    os.remove("generatedTemplate-WithParameters.html")
  except:
    pass  