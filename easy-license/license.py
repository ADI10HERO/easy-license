from cryptlex.lexactivator import LexActivator, LexStatusCodes, \
    LexActivatorException, PermissionFlags

PRODUCT_ID = ""
LICENSE_KEY = ""
METADATA = {
    # "key": "value"
}


def activate():
    try:
        # Setting product.dat file and product Id
        with open("./product.dat", "r") as f:
            PRODUCT_DAT_FILE = f.read()
        LexActivator.SetProductData(PRODUCT_DAT_FILE)
        LexActivator.SetProductId(PRODUCT_ID, PermissionFlags.LA_USER)

        # License activation
        LexActivator.SetLicenseKey(LICENSE_KEY)
        for key, value in METADATA.items():
            LexActivator.SetActivationMetadata(key, value)
        status = LexActivator.ActivateLicense()
        if LexStatusCodes.LA_OK == status or \
                LexStatusCodes.LA_EXPIRED == status or \
                LexStatusCodes.LA_SUSPENDED == status:
            print("License activated successfully: ", status)
        else:
            print("License activation failed: ", status)
    except LexActivatorException as exception:
        print('Error code:', exception.code, exception.message)
