import requests
import yaml
import os

inteltype = ['INTEL_ADDR']
path = os.environ["WORKDIR"]
with open(path + "/enrichment_plugins/DShield/dnifconfig.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)


def import_ip_intel():
    try:
        source = cfg['enrichment_plugin']['DSHIELD_IP_SOURCE']
        response = requests.get(source)
    except Exception, e:
        print 'Api Request Error %s' % e
    try:
        lines = []
        for line in response.iter_lines():
            line = line.strip()
            s = str(line)
            s = s.strip()
            if not s.startswith("#") and s != '' and s != 'Site' :
                tmp_dict = {}
                tmp_dict["DomainName"] = s
                tmp_dict["DomainSensitivity"] = ["Low Level Sensitivity"]
                tmp_dict2 = {}
                tmp_dict2["IntelRef"] = ["DShield"]
                tmp_dict2["IntelRefURL"] = [source]
                b_lst = []
                tmp_dict2["ThreatType"] = b_lst
                tmp_dict["AddFields"] = tmp_dict2
                lines.append(tmp_dict)
    except:
        lines = []
    return lines, 'INTEL_ADDR'
