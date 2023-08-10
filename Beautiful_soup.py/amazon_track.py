import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.amazon.in/Crucial-Plus-500GB-PCIe-5000MB/dp/B0B25NTRGD/ref=pd_ci_mcx_mh_mcx_views_1?pd_rd_w=qdGza&content-id=amzn1.sym.cd312cd6-6969-4220-8ac7-6dc7c0447352%3Aamzn1.symc.ca948091-a64d-450e-86d7-c161ca33337b&pf_rd_p=cd312cd6-6969-4220-8ac7-6dc7c0447352&pf_rd_r=E2CHH7DW9GTJCT35BHH3&pd_rd_wg=cNPb1&pd_rd_r=fdc2abf4-d2b3-4ea3-a760-475beed2dab1&pd_rd_i=B0B25NTRGD&th=1"
header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())


print(soup.find(name='span',class_="a-price-whole"))
dom = lxml.etree.HTML (str(soup))
print (dom.xpath ('//*[@id="corePrice_feature_div"]/div/span[1]/span[2]/span[2]'))
# price = soup.find(class_="a-price-whole").get_text()
# price_without_currency = price.split("$")[1]
# price_as_float = float(price_without_currency)
# print(price_as_float)
# //*[@id="corePrice_feature_div"]/div/span[1]/span[2]/span[2]