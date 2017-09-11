import requests, ast

def getBiomarkerLinks(biomarker, idDataSource):
    if not idDataSource:
        return None
    if idDataSource.strip() == "":
        return None
    try:    
        r = requests.get(idDataSource+"/"+biomarker, headers={'Accept': 'application/json'})
    except requests.exceptions.ConnectionError:
        return None

    j= r.text
    jsonresults = None
    if j != "":
        try:
            jsonresults = ast.literal_eval(j)
        except:
            pass
    return jsonresults
