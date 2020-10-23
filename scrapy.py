from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import pandas as pd 
import json

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

bs = BeautifulSoup()
correios = bs.select('table7')

localidade = []
CEP = []

for itens in correios:
	localidade.append(itens.find('td', style_ ='font-family: Arial;width: 100px;margin: 0;height: 20px;border: 1px solid #CFCFCF;color: black;padding: 3px;font-size: 1.1em;').get_text())
	CEP.append(itens.find('td', width_ = '80').get_text())
	
df = pd.DataFrame({
	"localidade" : localidade,
	"CEP" : CEP   
	 })
	

df.head()
print(df)
