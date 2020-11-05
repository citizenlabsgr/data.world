from helper import Helper

class ConfigLocal(dict):
    def __init__(self):
        self.update({
                 "app_name": Helper().get_app_name(),
                 "local_raw": None,
                 "local_clean": None
               })

def main():

    config = ConfigLocal()
    print(config)

if __name__ == "__main__":
    main()