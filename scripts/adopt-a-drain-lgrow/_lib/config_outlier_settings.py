
class ConfigOutlierSettings(list):
    def __init__(self):
        self.extend([{'column': 'dr_lon',
                 'range': (-90.0, -80.0),
                 'reason': 'Remove {} observations too far west or east.',
                 'count': 0,
                 'name': 'Latitude'
                 },{'column': 'dr_lat',
                 'range': (40.0, 50.0),
                 'reason': 'Remove {} observations too far north or south.',
                 'count': 0,
                 'name': 'Longitude'
                 }])

def main():

    lst = ConfigOutlierSettings()
    print('lst: ', lst)

if __name__ == "__main__":
    main()