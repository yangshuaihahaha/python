import requests

# head 信息
head = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
}
meta = {
    "query": "",
    "recr": "Not yet Recruiting;Recruiting;Available;Completed;Terminated;Suspended;Withdrawn;Withheld;Active, not recruiting;Enrolling by invitation;Expanded Access: Temporarily not available;Expanded Access: No longer available;Expanded Access: Approved for marketing",
    "source": "US;EU;JP;CN;CN2;NZ",
    "phase": "Phase 0;Phase 1;Phase 2;Phase 3;Phase 4",
    "updated_from": "",
    "updated_to": "",
    "received_from": "01/01/2020",
    "received_to": "01/31/2020",
    "role": "Patient",
    "resources": ""
}
res = requests.post('https://globalclinicaltrialdata.com/download', data=meta, headers=head, verify=False)
print("status_code : " + str(res.status_code))
print("text : " + res.text)
