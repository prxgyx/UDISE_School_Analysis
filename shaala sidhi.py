import requests
from bs4 import BeautifulSoup
import json


cookies = {
    'ASP.NET_SessionId': 'oadfyljegrb45u3w3tuo3gka',
}

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'Accept': '*/*',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
    'Origin': 'https://shaalasiddhi.niepa.ac.in',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://shaalasiddhi.niepa.ac.in/shaalasiddhi/Reports/SchoolEvaluationReportForPublic?AcademicYearId=0',
    'Accept-Language': 'en-US,en;q=0.9',
}


state_data = {
  'UserId': '177442',
  'StateId': '23'
}

state_response = requests.post('https://shaalasiddhi.niepa.ac.in/shaalasiddhi/Reports/GetDistrictByStateId', headers=headers, cookies=cookies, data=state_data)

# print(state_response.json())
f = open("output.txt", "a")

for district_info in state_response.json():
	print(district_info)
	final_list = []
	district_id = district_info["DistrictID"]

	if district_id not in ["2351"]:

		district_data = {
		  'UserId': '177442',
		  'DistrictId': district_id
		}
		f = open("output_{}.txt".format(district_id), "a")
		district_response = requests.post('https://shaalasiddhi.niepa.ac.in/shaalasiddhi/Reports/GetBlocksByDistrictId', headers=headers, cookies=cookies, data=district_data)

		for district in district_response.json():
			# print(district)
			block_id = district["BlockId"]
			block_name = district["BlockName"]

			if block_name not in ["ALIRAJPUR", "BHABARA"]:
			
				block_data = {
				  'UserId': '177442',
				  'BlockId': block_id
				}

				village_response = requests.post('https://shaalasiddhi.niepa.ac.in/shaalasiddhi/Reports/GetVillageByBlockId', headers=headers, cookies=cookies, data=block_data).json()

				# print(village_response.json())

				for village_info in village_response:
					# print(village_info)
					village_id = village_info['VillageId']

					village_data = {
					  'UserId': '177442',
					  'ClusterId': '0',
					  'VillageId': village_id
					}

					school_responses = requests.post('https://shaalasiddhi.niepa.ac.in/shaalasiddhi/Reports/GetSchoolsByClusterAndVillageId', headers=headers, cookies=cookies, data=village_data).json()

					for school_response in school_responses:
						# print(school_response)
						school_id = school_response["InstanceId"]

						print(school_id)

						school_html = requests.get("https://shaalasiddhi.niepa.ac.in/shaalasiddhi/Reports/PublicSchoolEvaluationDetails?AcademicYearId=9&SchoolId="+school_id).text

						soup = BeautifulSoup(school_html, "html.parser")

						category_type = soup.find("label", {"for": "CategoryType"})

						# print(category_type.text)

						locality = soup.find("input", {"checked": "checked"})

						# print(locality.get("title"))

						data = {
							'district name': district_info["DistrictName"],
							'block_name': block_name,
							'village_name': village_info['VillageName'],
							'school_name': school_response['InstanceName'],
							'locality': locality.get("title"),
							'category': category_type.text
						}

						print(json.dumps(data))

						# print(soup.get("title"))
						# final_list.append(data)
						f.write(json.dumps(data) + ",\n")

				# divs = soup.findAll("td", {"class": "ftd-2"})  
				# for div in divs:
				# 	if "Level-" in div.text:
				# 		f.write(div.text + "\n")

				# 		# print(div.text)
				# 		# print("0" not in div.text)
				# 		if "0" not in div.text:
				# 			f.write(json.dumps(district_info)+ json.dumps(district)+ json.dumps(village_info)+ json.dumps(school_response))



