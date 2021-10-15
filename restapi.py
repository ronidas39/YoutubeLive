import requests
from requests.api import get

def get_district(sname):
    #response=requests.get("https://dashboard.cowin.gov.in/assets/json/csvjson.json")
    response=requests.get("https://api.cowin.gov.in/api/v1/reports/v2/getPublicReports")
    data=response.json()
    data=data["getBeneficiariesGroupBy"]
    for state in data:
        if sname=="India":
            return [{'label': 'ALL', 'value': 'ALL'}]

        elif state["state_name"]==sname:

            id=(state["state_id"])
            data_district=response=requests.get("https://dashboard.cowin.gov.in/assets/json/csvjson.json")
            district_data=data_district.json()
            district_list=[{"label":"ALL","value":"ALL"}]
            for district in district_data:
                #print(district["state_id"],id)
                if district["state_id"]==int(id):
                    district_list.append({"label":district["district_name"],"value":district["district_name"]})
            
            return district_list

        
        
        
    
def allstate():
    response=requests.get("https://api.cowin.gov.in/api/v1/reports/v2/getPublicReports")
    data=response.json()

    states=data["getBeneficiariesGroupBy"]
    state_list=[{"label":"India","value":"India"}]
    for state in states:
        state_list.append({"label":state["state_name"],"value":state["state_name"]})
    return state_list


def get_sites(state_name="",district_name=""):
    if(state_name=="" or state_name=="India"):
        response=requests.get("https://api.cowin.gov.in/api/v1/reports/v2/getPublicReports?state_id=&district_id=")
        data=response.json()
        sites=data["topBlock"]["sites"]
        return sites
    elif(district_name=="ALL"):
        print("line no 48 inside get_sites elif block")
        response=requests.get("https://api.cowin.gov.in/api/v1/reports/v2/getPublicReports")
        data=response.json()
        data=data["getBeneficiariesGroupBy"]
        for state in data:
            if(state["state_name"]==state_name):
                id=state["state_id"]
                print(state_name,district_name)
                url="https://api.cowin.gov.in/api/v1/reports/v2/getPublicReports?state_id="+str(id)+"&district_id="
                response=requests.get(url)
                data=response.json()
                sites=data["topBlock"]["sites"]
                return sites
    else:
        data_district=requests.get("https://dashboard.cowin.gov.in/assets/json/csvjson.json")
        district_data=data_district.json()
        print("line no 64 inside get_sites else block")
        print(state_name,district_name)
        for district in district_data:
            if district["district_name"]==district_name:
                state_id=district["state_id"]
                disc_id=district["district_id"]
                print(state_id,disc_id)
                url="https://api.cowin.gov.in/api/v1/reports/v2/getPublicReports?state_id="+str(state_id)+"&district_id="+str(disc_id)
                response=requests.get(url)
                data=response.json()
                sites=data["topBlock"]["sites"]
                return sites
def get_vaccination(state_name="",district_name=""):
    if(state_name=="" or state_name=="India"):
        response=requests.get("https://api.cowin.gov.in/api/v1/reports/v2/getPublicReports?state_id=&district_id=")
        data=response.json()
        sites=data["topBlock"]["vaccination"]
        return sites
    elif(district_name=="ALL"):
        print("line no 83 inside get_vaccination elif block")
        response=requests.get("https://api.cowin.gov.in/api/v1/reports/v2/getPublicReports")
        data=response.json()
        data=data["getBeneficiariesGroupBy"]
        for state in data:
            if(state["state_name"]==state_name):
                id=state["state_id"]
                print(state_name,district_name)
                url="https://api.cowin.gov.in/api/v1/reports/v2/getPublicReports?state_id="+str(id)+"&district_id="
                response=requests.get(url)
                data=response.json()
                sites=data["topBlock"]["vaccination"]
                return sites


    else:
        data_district=requests.get("https://dashboard.cowin.gov.in/assets/json/csvjson.json")
        district_data=data_district.json()
        print("ine no 101 inside get_vaccination else block")
        print(state_name,district_name)
        for district in district_data:
            if district["district_name"]==district_name:
                state_id=district["state_id"]
                disc_id=district["district_id"]
                print(state_id,disc_id)
                url="https://api.cowin.gov.in/api/v1/reports/v2/getPublicReports?state_id="+str(state_id)+"&district_id="+str(disc_id)
                response=requests.get(url)
                data=response.json()
                sites=data["topBlock"]["vaccination"]
                return sites
def get_registration(state_name="",district_name=""):
    if(state_name=="" or state_name=="India"):
        response=requests.get("https://api.cowin.gov.in/api/v1/reports/v2/getPublicReports?state_id=&district_id=")
        data=response.json()
        sites=data["topBlock"]["registration"]
        return sites










