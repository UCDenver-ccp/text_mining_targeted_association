  
def get_release(self):
    # hard-coded release for demo purpose
    # "self" is a dumper instance, see:
    # https://github.com/biothings/biothings.api/blob/master/biothings/hub/dataload/dumper.py
    import requests
    import datetime
    res = requests.get("https://storage.googleapis.com/translator-text-workflow-dev-public/kgx/UniProt/version.txt")
    if res.status_code == 200:
        file_content = res.text
        # Extract the first line which contains the version
        version = file_content.splitlines()[0]
        return version
    else:
        return str(datetime.date.today())