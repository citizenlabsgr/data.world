
class ConfigCommonNameMap(dict):
    # common names from imported files and how then map to actual names

    def __init__(self):
        self.update({
            "str_type": "dr_subtype",
            "strtype": "dr_subtype",
            "subtype": "dr_subtype",
            "jurisdicti": "dr_jurisdiction",
            "drain__owner": "dr_owner",
            "owner": "dr_owner",
            "local__id": "dr_local_id",
            "facilityid": "dr_facility_id",
            "drain__jurisdiction": "dr_jurisdiction",
            "subwatershed": "dr_subwatershed",
            "subbasin": "dr_subwatershed",
            "point__x": "dr_lon",
            "long": "dr_lon",
            "point__y": "dr_lat",
            "lat": "dr_lat",
            "soure__id": "del_source_id"
        })

def main():
    map = ConfigCommonNameMap()
    print(map)
    assert map['subtype'] == 'dr_subtype'
    assert map['strtype'] == 'dr_subtype'


if __name__ == "__main__":
    main()