from getdata import GetData

soup = GetData("https://www.detik.com/terpopuler?","{'tag_from':'wp_cb_mostPopular_more'}").html_parser()

popular_area = soup.find(attrs={'class':'grid-row list-content'})

#print(soup.prettify())
print(popular_area.prettify())
