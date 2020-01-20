from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'djangouser' # Must be replaced by your <storage_account_name>
    account_key = 'GPmn5ja/Dwjpo3M3N9pbQMbVP52Tq+6TkCcgP35cAFgaiGdR2yDCT0MQm19Ql84ZeSIw8BAlAujC2Fp/tJkKrQ==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'djangouser' # Must be replaced by your storage_account_name
    account_key = 'GPmn5ja/Dwjpo3M3N9pbQMbVP52Tq+6TkCcgP35cAFgaiGdR2yDCT0MQm19Ql84ZeSIw8BAlAujC2Fp/tJkKrQ==' # Must be replaced by your <storage_account_key>
    azure_container = 'resumecreator'
    expiration_secs = None


