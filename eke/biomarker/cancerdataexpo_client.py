import requests, ast

def getBiomarkerLinks(biomarker, idDataSource):
    if not idDataSource:
        return None
    if idDataSource.strip() == "":
        return None
    print "START"
    try:    
        print "GOT HERE"
        print "request: {}".format(idDataSource+"/"+biomarker)
        r = requests.get(idDataSource+"/"+biomarker, headers={'Accept': 'application/json'})
    except requests.exceptions.ConnectionError:
        print "GOT CONNECITION ERROR"
        return None

    j= r.text
    print j
    jsonresults = None
    if j != "":
        try:
            jsonresults = ast.literal_eval(j)
            print "JSON Successful!!!"
        except:
            print "JSON FAILED, WARNING!"
            pass
    return jsonresults
