from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'djangouser' # Must be replaced by your <storage_account_name>
    account_key = 'SECRET1' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'djangouser' # Must be replaced by your storage_account_name
    account_key = 'SECRET2' # Must be replaced by your <storage_account_key>
    azure_container = 'resumecreator'
    expiration_secs = None


