from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import pandas as pd 
import json
import lxml

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm")

select = Select(driver.find_element_by_name('UF'))
select.select_by_value("SC")
driver.find_element_by_class_name("btn2.float-right").click()

dados = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table[2]")
html = dados.get_attribute("innerHTML")
soup = BeautifulSoup(html, "html.parser")
table1 = soup.select_one("tbody")


driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[5]").click()

dados = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table")
html = dados.get_attribute("innerHTML")
soup = BeautifulSoup(html, "html.parser")
table2 = soup.select_one("tbody")

driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[5]").click()

dados = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table")
html = dados.get_attribute("innerHTML")
soup = BeautifulSoup(html, "html.parser")
table3 = soup.select_one("tbody")

driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[5]").click()

dados = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table")
html = dados.get_attribute("innerHTML")
soup = BeautifulSoup(html, "html.parser")
table4 = soup.select_one("tbody")

driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[5]").click()

dados = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table")
html = dados.get_attribute("innerHTML")
soup = BeautifulSoup(html, "html.parser")
table5 = soup.select_one("tbody")

driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[5]").click()

dados = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table")
html = dados.get_attribute("innerHTML")
soup = BeautifulSoup(html, "html.parser")
table6 = soup.select_one("tbody")

driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[5]").click()

dados = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table")
html = dados.get_attribute("innerHTML")
soup = BeautifulSoup(html, "html.parser")
table7 = soup.select_one("tbody")

tablesc = str(table7)
tablesc1 = str(table6)
tablesc2 = str(table5)
tablesc3 = str(table4)
tablesc4 = str(table3)
tablesc5 = str(table2)
tablesc6 = str(table1)

tablesc7 = tablesc6 + tablesc5+ tablesc4 + tablesc3 + tablesc2 + tablesc1 + tablesc

bs = BeautifulSoup(tablesc7, "html.parser")
correios = bs.find_all("td")

for sc in correios:
	arquivo = open("sc.txt", "a")
	arquivo.write(sc.text)

driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[6]").click()

select = Select(driver.find_element_by_name('UF'))
select.select_by_value("AC")
driver.find_element_by_class_name("btn2.float-right").click()

dados = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table[2]")
html = dados.get_attribute("innerHTML")
soup = BeautifulSoup(html, "html.parser")
table8 = soup.select_one("tbody")

tableac = str(table8)

acbs = BeautifulSoup(tableac, "html.parser")  
correiosac = acbs.find_all("td")

for ac in correiosac:
	arquivo = open("ac.txt", "a")
	arquivo.write(ac.text)

driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[6]").click()

select = Select(driver.find_element_by_name('UF'))
select.select_by_value("AM")
driver.find_element_by_class_name("btn2.float-right").click()

dados = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table")
html = dados.get_attribute("innerHTML")
soup = BeautifulSoup(html, "html.parser")
table9 = soup.select_one("tbody")

driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[5]").click()

dados = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table")
html = dados.get_attribute("innerHTML")
soup = BeautifulSoup(html, "html.parser")
table10 = soup.select_one("tbody")

tableam = str(table9)
tableam1 = str(table10)
tableam2 = tableam + tableam1

ambs = BeautifulSoup(tableam2, "html.parser") 
correiosam = ambs.find_all("td")

for am in correiosam:
	arquivo = open("am.txt", "a")
	arquivo.write(am.text)  

driver.quit()

print("Done !")