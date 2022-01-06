
class ConfigRegionMap(dict):
    def __init__(self):
        self.update({
        "Kent County Road Commission": "KCRC",
        "KENT COUNTY ROAD COMMISSION":"KCRC",
        "City of East Grand Rapids": "EGR",
        "City of Grandville": "GRANDV",
        "City of Wyoming": "CWY",
        "City of Kentwood": "CK",
        "Grand Rapids Township": "GRTWP",
        "City of Walker": "CW",
        "CGR": "CGR",
        "City of Grand Rapids": "CGR",
        "Georgetown Township": "GTWP",
        "City of Hudsonville": "CHV",
        "Jamestown Township": "JTTWP",
        "Cascade Township": "CASTWP",
        "Algoma Township": "ALGTWP",
        "Grattan Township": "GRATWP",
        "Gaines Township": "GAITWP",
        "Vergennes Township": "VERTWP",
        "Lowell Township": "LOWTWP",
        "Oakfield Township": "OAKTWP",
        "Cannon Township": "CANTWP",
        "Sparta Township": "SPATWP",
        "Solon Township": "SOLTWP",
        "Ada Township": "ADATWP",
        "City of Lowell": "CLO",
        "Bowne Township": "BOWTWP",
        "Tyrone Township": "TYRTWP",
        "Caledonia Township": "CALTWP",
        "Courtland Township": "COUTWP",
        "Spencer Township": "SPETWP",
        "Village of Sparta": "VSP",
        "BYRON TOWNSHIP": "BYRTWP",
        "CALEDONIA TOWNSHIP": "CALETWP",
        "City of Rockford": "CRF",
        "Alpine Township": "ALPTWP",
        "Plainfield Township": "PLATWP",
        "Byron Township": "BYRTWP",
        "OCWRC": "OCWRC",
        "Village of Spring Lake": "VSL",
        "Village of Spring Lake DPW": "VSL",
        "Ottawa County Road Commission": "OCRC",
        "OCRC": "OCRC",
        "Ottawa County Water Resource Commissioner":"OCRC",
        "Village of Fruitport":"VF",
        "Village of Caledonia":"VC",
        "City of Grand Haven DPW": "CGH",
        "OC Facilities":"OCF"
    })

def main():
    map = ConfigRegionMap()

    assert map['Kent County Road Commission'] == 'KCRC'
    assert map['KENT COUNTY ROAD COMMISSION'] == 'KCRC'


if __name__ == "__main__":
    main()