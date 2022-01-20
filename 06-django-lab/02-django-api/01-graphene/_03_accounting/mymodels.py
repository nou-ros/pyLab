from django.db import models
from common_utils.base_entity import BaseEntityBasicAbstract, BaseEntityAbstract
from django_enumfield import enum
from core.s3utils import PrivateS3BotoStorage, PublicS3BotoStorage
from accounting.enum import (
    AddressTypeEnum, ShippingMethodsTypeEnum
)
from common_utils.uploads import supplier_logo_upload, client_photo_upload, item_picture_upload, items_group_picture_upload

# Create your models here.
class HeadOfAccounts(BaseEntityAbstract):
    head_acc_name = models.CharField(max_length=255)
    notes = models.TextField()
    is_editable = models.BooleanField(default=False)

class AccountType(BaseEntityAbstract):
    acc_type_name = models.CharField(max_length=255)
    notes = models.TextField(null=True, blank=True)
    is_editable = models.BooleanField(default=False)
    head_of_accounts = models.ForeignKey(HeadOfAccounts, on_delete=models.CASCADE)

class AccountName(BaseEntityAbstract):
    acc_code = models.IntegerField() 
    acc_start_date = models.DateTimeField(auto_now_add=True)
    opening_balance = models.FloatField(default=0)
    is_editable = models.BooleanField(default=False)
    is_suspended = models.BooleanField(default=False)
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE)

class SubAccounts(BaseEntityAbstract):
    parent = models.ForeignKey(AccountType, related_name='parent-account', on_delete=models.CASCADE)
    child = models.ForeignKey(AccountType, related_name='child-account', on_delete=models.CASCADE)

class Supplier(BaseEntityAbstract):
    company_name = models.CharField(max_length=255)
    corporation_no = models.CharField(max_length=255, null=True, blank=True)
    salutation = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name =  models.CharField(max_length=255)
    display_name = models.CharField(max_length=255, null=True, blank=True)
    logo = models.ImageField(
        upload_to=supplier_logo_upload, blank=True, null=True, storage=PrivateS3BotoStorage())
    website = models.CharField(max_length=255, null=True, blank=True)
    email_address = models.CharField(max_length=255, null=True, blank=True)

class SupplierAdditionalContacts(BaseEntityAbstract):
    salutation = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name =  models.CharField(max_length=255)
    designation =  models.CharField(max_length=255, null=True, blank=True)
    work_phone = models.CharField(max_length=255, null=True, blank=True)
    mobile_phone = models.CharField(max_length=255, null=True, blank=True)
    email_address = models.CharField(max_length=255, null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

class Country(BaseEntityAbstract):
    name = models.CharField(max_length=255)
    phone_code = models.CharField(max_length=255)
    short_name = models.CharField(max_length=20)

class SupplierAddress(BaseEntityAbstract):
    addresstype = enum.EnumField(AddressTypeEnum, default=AddressTypeEnum.BILLING)
    branch_as = models.CharField(max_length=255, null=True, blank=True)
    care_of_person = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    office_number = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)
    fax_number = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

class Clients(BaseEntityAbstract):
    is_corporation = models.BooleanField(default=False)
    company_name = models.CharField(max_length=255, unique=True)
    salutation = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name =  models.CharField(max_length=255)
    display_name = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(
        upload_to=client_photo_upload, blank=True, null=True, storage=PrivateS3BotoStorage())
    website = models.CharField(max_length=255, null=True, blank=True)
    email_address = models.CharField(max_length=255, null=True, blank=True)

class ClientAdditionalContacts(BaseEntityAbstract):
    salutation = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name =  models.CharField(max_length=255)
    designation =  models.CharField(max_length=255)
    work_phone = models.CharField(max_length=255)
    mobile_phone = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)


class ClientAddress(BaseEntityAbstract):
    addresstype = enum.EnumField(AddressTypeEnum, default=AddressTypeEnum.BILLING)
    branch_as = models.CharField(max_length=255, null=True, blank=True)
    care_of_person = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    office_number = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)
    fax_number = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)

class Currency(BaseEntityAbstract):
    symbol = models.CharField(max_length=255 , null=True, blank=True)
    name = models.CharField(max_length=255 , null=True, blank=True) 
    symbol_native = models.CharField(max_length=255 , null=True, blank=True)
    code = models.CharField(max_length=255, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

class PaymentTerms(BaseEntityAbstract):
    term_name = models.CharField(max_length=255)
    no_days = models.IntegerField(null=True, blank=True)
    day_of_mon = models.IntegerField(null=True, blank=True)
    day_next_mon = models.IntegerField(null=True, blank=True)

class SupplierDetails(BaseEntityAbstract):
    bank_acc_no = models.CharField(max_length=255, null=True, blank=True)
    opening_balance = models.FloatField(default=0)
    open_bal_date = models.DateTimeField(auto_now_add=True)
    pay_recurring = models.BooleanField(default=False)
    is_contractor = models.BooleanField(default=False)
    send_invitation = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)
    pay_term = models.ForeignKey(PaymentTerms, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    supplier = models.OneToOneField(Supplier, on_delete=models.CASCADE)

class PaymentMethods(BaseEntityAbstract):
    name = models.CharField(max_length=255)
    notes = models.TextField(null=True, blank=True)

class ClientDetails(BaseEntityAbstract):
    bank_acc_no = models.CharField(max_length=255, null=True, blank=True)
    opening_balance = models.FloatField(default=0)
    open_bal_date = models.DateTimeField(auto_now_add=True)
    pay_recurring = models.BooleanField(default=False)
    late_fees = models.BooleanField(default=False)
    pay_reminder = models.BooleanField(default=False)
    tax_exemption = models.BooleanField(default=False)
    send_invitation = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    pay_term = models.ForeignKey(PaymentTerms, on_delete=models.CASCADE)
    client = models.OneToOneField(Clients, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(PaymentMethods, on_delete=models.CASCADE)

class ItemType(BaseEntityAbstract):
    name = models.CharField(max_length=255)
    notes = models.CharField(max_length=255, null=True, blank=True)

class ItemCategory(BaseEntityAbstract):
    name = models.CharField(max_length=255)
    notes = models.CharField(max_length=255, null=True, blank=True)

class ItemBrands(BaseEntityAbstract):
    name = models.CharField(max_length=255)
    notes = models.TextField(null=True, blank=True)

class Items(BaseEntityAbstract):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    SKU = models.CharField(max_length=255, null=True, blank=True)
    picture = models.ImageField(
        upload_to=item_picture_upload, blank=True, null=True, storage=PrivateS3BotoStorage())
    item_type = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    item_category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    purchase_price = models.FloatField(default=0, null=True, blank=True)
    account_name = models.ForeignKey(AccountName, on_delete=models.CASCADE)
    sales_price = models.FloatField(default=0)
    markup_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    min_sales_price = models.FloatField(default=0, null=True, blank=True)  
    weight_param = models.CharField(max_length=255)
    weight_values = models.FloatField(default=0)
    volume_cbm = models.FloatField(default=0)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    item_brand = models.ForeignKey(ItemBrands, on_delete=models.CASCADE)
    upc_no = models.CharField(max_length=255, null=True, blank=True)
    mpn_no = models.CharField(max_length=255, null=True, blank=True)
    ean_no = models.CharField(max_length=255, null=True, blank=True)
    isbn_no = models.CharField(max_length=255, null=True, blank=True)
    item_barcode = models.CharField(max_length=255, null=True, blank=True)
    warranty_month = models.IntegerField(null=True, blank=True) 
    stock_in_hand = models.FloatField(default=0)
    initial_stock_entry = models.DateTimeField(auto_now_add=True)
    reorder_point = models.IntegerField(null=True, blank=True) 
    max_stock_no = models.IntegerField(null=True, blank=True) 
    lead_time_days = models.IntegerField(null=True, blank=True)
    allow_sales_commision = models.BooleanField(default=True)
    commission_per_item = models.IntegerField() 
    commission_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    tags = models.CharField(max_length=255)

class ItemsGroup(BaseEntityAbstract):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    SKU = models.CharField(max_length=255, null=True, blank=True)
    picture = models.ImageField(
        upload_to=items_group_picture_upload, blank=True, null=True, storage=PrivateS3BotoStorage())
    item_type = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    volume_cbm = models.FloatField(default=0)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    item_brand = models.ForeignKey(ItemBrands, on_delete=models.CASCADE)
    upc_no = models.CharField(max_length=255, null=True, blank=True)
    item_barcode = models.CharField(max_length=255, null=True, blank=True)
    warranty_month = models.IntegerField(null=True, blank=True) 
    account_name = models.ForeignKey(AccountName, on_delete=models.CASCADE)
    tags = models.CharField(max_length=255)

class ItemGroupMapping(BaseEntityAbstract):
    item_group = models.OneToOneField(ItemsGroup, on_delete=models.CASCADE)
    item = models.OneToOneField(Items, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)

class InventoryAdjustment(BaseEntityAbstract):
    time_log = models.DateTimeField(auto_now_add=True)
    adjustment_reference_no = models.CharField(max_length=255)
    cause_of_action = models.CharField(max_length=255)
    acc_name = models.ForeignKey(AccountName, on_delete=models.CASCADE)
    comments = models.TextField(null=True, blank=True)

class InventoryAdjustmentItems(BaseEntityAbstract):
    inventory_adjustment = models.OneToOneField(InventoryAdjustment, on_delete=models.CASCADE)
    item = models.OneToOneField(Items, on_delete=models.CASCADE)
    quantity_or_value = models.BooleanField(default=True)
    value = models.FloatField(default=0)

class StorageLocation(BaseEntityAbstract):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

class ItemStorage(BaseEntityAbstract):
    storage_location = models.ForeignKey(StorageLocation, on_delete=models.CASCADE)
    lot_number = models.CharField(max_length=255, null=True, blank=True)
    barcode = models.CharField(max_length=255, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

class ItemStorageMapping(BaseEntityAbstract):
    item_storage = models.OneToOneField(ItemStorage, on_delete=models.CASCADE)
    item = models.OneToOneField(Items, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True) 
    volume = models.CharField(max_length=255)

class ItemTransfer(BaseEntityAbstract):
    time_log = models.DateTimeField(auto_now_add=True)
    reference_no = models.CharField(max_length=255)
    from_storage_location = models.ForeignKey(StorageLocation, on_delete=models.CASCADE, related_name="from_storage")
    to_storage_location = models.ForeignKey(StorageLocation, on_delete=models.CASCADE, related_name="to_storage")
    shopping_carrier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    shipping_method = enum.EnumField(ShippingMethodsTypeEnum, default=ShippingMethodsTypeEnum.GROUND)
    shipment_tracking_no = models.CharField(max_length=255, null=True, blank=True)
    shipment_cost = models.FloatField(default=0)
    bilable = models.BooleanField(default=False)
    notes = models.TextField()

class ItemTransferMapping(BaseEntityAbstract):
    item_transfer = models.OneToOneField(ItemTransfer, on_delete=models.CASCADE)
    item = models.OneToOneField(Items, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    volume = models.CharField(max_length=255)
