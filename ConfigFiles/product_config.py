from ConfigFiles import common_config, english_config, french_config, dutch_config
from ConfigFiles.Canada import canada_config
from ConfigFiles.Fedramp import fedramp_config
from ConfigFiles.Germany import germany_config
from ConfigFiles.SP360 import sp360_config
from ConfigFiles.UK import uk_config


class product_config:

    sp360commercial = {
        'dev': sp360_config.sp360_dev_config,
        'qa': sp360_config.sp360_qa_config,
        'ppd': sp360_config.sp360_ppd_config,
        'prod':sp360_config.sp360_prod_config,
        'dh_config': english_config.dh_app_config_windows,
        'dh_common_config': common_config.dh_app_common_config_windows
    }
    fedramp = {
        'qa': fedramp_config.fedramp_qa_config,
        'ppd': fedramp_config.fedramp_ppd_config,
        'dev': fedramp_config.fedramp_dev_config,
        'dh_config': english_config.dh_app_config_windows,
        'dh_common_config': common_config.dh_app_common_config_windows
    }
    sp360canada = {
        'ppd': canada_config.canada_ppd_config,
        'dh_config_english': english_config.dh_app_config_windows,
        'dh_config_french': french_config.dh_app_config_windows,
        'dh_common_config': common_config.dh_app_common_config_windows,
        'prod': canada_config.canada_prod_config,
    }
    sp360uk = {
        'ppd': uk_config.uk_ppd_config,
        'dh_config': english_config.dh_app_config_windows,
        'dh_common_config': common_config.dh_app_common_config_windows,
        'prod': uk_config.uk_prod_config,
    }
    sp360germany = {
        'ppd': germany_config.germany_ppd_config,
        'dh_config_english': english_config.dh_app_config_windows,
        'dh_config_dutch': dutch_config.dh_app_config_windows,
        'dh_common_config': common_config.dh_app_common_config_windows,
        'prod': germany_config.germany_prod_config
    }
