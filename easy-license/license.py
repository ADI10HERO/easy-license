import os
from dotenv import load_dotenv
from cryptlex.lexactivator import LexActivator, LexStatusCodes, \
    LexActivatorException, PermissionFlags

load_dotenv()

PRODUCT_ID = os.getenv("PRODUCT_ID")
LICENSE_KEY = os.getenv("LICENSE_KEY")
METADATA = {
    # "key": "value"
}


def set_product_data():
    # Setting product.dat file and product Id
    try:
        with open("./product.dat", "r") as f:
            PRODUCT_DAT_FILE = f.read()
        LexActivator.SetProductData(PRODUCT_DAT_FILE)
        LexActivator.SetProductId(PRODUCT_ID, PermissionFlags.LA_USER)
    except LexActivatorException as exception:
        print('Error code:', exception.code, exception.message)
    return


def activate():
    try:
        set_product_data()

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


def verify():
    try:
        set_product_data()

        # License verification
        status = LexActivator.IsLicenseGenuine()
        if LexStatusCodes.LA_OK == status:
            print("License is genuinely activated!")
        elif LexStatusCodes.LA_EXPIRED == status:
            print("License is genuinely activated but has expired!")
        elif LexStatusCodes.LA_SUSPENDED == status:
            print("License is genuinely activated but has been suspended!")
        elif LexStatusCodes.LA_GRACE_PERIOD_OVER == status:
            print("License is genuinely activated but grace period is over!")
        else:
            print("License is not activated: ", status)
    except LexActivatorException as exception:
        print('Error code:', exception.code, exception.message)
