import requests
from bs4 import BeautifulSoup
import pandas as pd 
req = requests.get("https://www.amazon.com/Good-Sleep-Bedding-Sheet-Pillowcase/dp/B0BWJWWRLZ/ref=sr_1_4_sspa?_encoding=UTF8&content-id=amzn1.sym.83009b1f-702c-4be7-814b-0240b8f687d2&dib=eyJ2IjoiMSJ9.b5R0jRFfVPlGMYMRYmenWeAsYd7EyEHPw7LijM2vLV2XTegqfxE-09Jt-Sg8mrj5d3rZTkutXxMxaNxZhw4aBkwxRjRTXerJIvhWcOKiJRQz1LoYRfbjjDmeEtfR_1_OjSQ-tkr-Txi33MBS6LdtT3UOTnlD35anSaqYi1fgmu87Mal4tL2xwxWY_xX6-GBxmurAQ24GvbpJQyMpRbtD3zXUhZHbFPZg81rlh1TtUj9zc1NvCuxTiCtpmtaq0El80wPxVeCXn5U2kE3AgYgOhL5zEX9k0K0xAq26AghRg44.1YazDsCDiw-riKrWqE388dRm0FaSOZS-xFIXVvbvHGs&dib_tag=se&keywords=bedding&pd_rd_r=4c4d06ef-2764-44bc-b21a-013505a33ad9&pd_rd_w=5i74M&pd_rd_wg=uEdKd&pf_rd_p=83009b1f-702c-4be7-814b-0240b8f687d2&pf_rd_r=WQ0G4T9CNRVE6TTFS731&qid=1733766853&sr=8-4-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")
response=requests.get*(url)
soup=BeautifulSoup(response.text,"html5")


df=pd.DataFrame("data")
df.to_csv("data.csv")
print("done")
