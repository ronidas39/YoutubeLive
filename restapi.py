import requests

def allstate():
    response=requests.get("https://api.cowin.gov.in/api/v1/reports/v2/getPublicReports")
    data=response.json()
    states=data["getBeneficiariesGroupBy"]
    state_list=[{"label":"India","value":"India"}]
    for state in states:
        state_list.append({"label":state["state_name"],"value":state["state_name"]})
    return state_list    
