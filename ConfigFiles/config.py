from ConfigFiles.product_config import product_config


class Config:

    def __init__(self, env, product_name, language):
        if product_name == "sp360commercial":
            self.env_cfg = product_config.sp360commercial[env]
            self.dh_config = product_config.sp360commercial['dh_config']
            self.dh_common_config = product_config.sp360commercial['dh_common_config']

        elif product_name == "fedramp":
            self.env_cfg = product_config.fedramp[env]
            self.dh_config = product_config.fedramp['dh_config']
            self.dh_common_config = product_config.fedramp['dh_common_config']

        elif product_name == "sp360canada":
            
            self.env_cfg = product_config.sp360canada[env]
            self.dh_common_config = product_config.sp360canada['dh_common_config']
            if language == 'french':
                print('inside french')
                self.dh_config = product_config.sp360canada['dh_config_french']
            else:
                print('inside english')
                self.dh_config = product_config.sp360canada['dh_config_english']

        elif product_name == "sp360uk":
            self.env_cfg = product_config.sp360uk[env]
            self.dh_common_config = product_config.sp360uk['dh_common_config']
            self.dh_config = product_config.sp360uk['dh_config']

        elif product_name == "sp360germany":
            self.env_cfg = product_config.sp360germany[env]
            self.dh_common_config = product_config.sp360germany['dh_common_config']
            if language == 'dutch':
                print('inside dutch')
                self.dh_config = product_config.sp360germany['dh_config_dutch']
            else:
                print('inside english')
                self.dh_config = product_config.sp360germany['dh_config_english']
