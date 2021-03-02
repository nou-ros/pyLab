from django.db import models

from django_enumfield import enum

# from django.utils.timezone.now()

# Create your models here.
class Supplier(models.Model):
    company_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    corporation_no = models.CharField(max_length=255, null=True, blank=True)
    salutation = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name =  models.CharField(max_length=255)
    display_name = models.CharField(max_length=255, null=True, blank=True)
    logo = models.ImageField(upload_to='clients/%Y/%m/%D/')
    website = models.CharField(max_length=255, null=True, blank=True)
    email_address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.company_name

class SupplierAdditionalContacts(models.Model):
    is_active = models.BooleanField(default=True)
    salutation = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name =  models.CharField(max_length=255)
    designation =  models.CharField(max_length=255, null=True, blank=True)
    work_phone = models.CharField(max_length=255, null=True, blank=True)
    mobile_phone = models.CharField(max_length=255, null=True, blank=True)
    email_address = models.CharField(max_length=255, null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Country(models.Model):
    name = models.CharField(max_length=255)
    phone_code = models.CharField(max_length=255)
    short_name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name

class AddressTypeEnum(enum.Enum):
    BILLING = 1
    SHIPPING = 2

class SupplierAddress(models.Model):
    is_active = models.BooleanField(default=True)
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

    class Meta:
        verbose_name_plural = 'Supplier Address'

    def __str__(self):
        return self.care_of_person
    

class Clients(models.Model):
    is_active = models.BooleanField(default=True)
    is_corporation = models.BooleanField(default=False)
    company_name = models.CharField(max_length=255, unique=True)
    salutation = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name =  models.CharField(max_length=255)
    display_name = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(upload_to='clients/%Y/%m/%D/')
    website = models.CharField(max_length=255, null=True, blank=True)
    email_address = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.company_name

class ClientAdditionalContacts(models.Model):
    is_active = models.BooleanField(default=True)
    salutation = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name =  models.CharField(max_length=255)
    designation =  models.CharField(max_length=255)
    work_phone = models.CharField(max_length=255)
    mobile_phone = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Client Additional Contacts'

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class ClientAddress(models.Model):
    is_active = models.BooleanField(default=True)
    addresstype = enum.EnumField(AddressTypeEnum, default=AddressTypeEnum.BILLING)
    branch_as = models.CharField(max_length=255, null=True, blank=True)
    care_of_person = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255, null=True, blank=True)
    office_number = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)
    fax_number = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Client Address'

    def __str__(self):
        return self.care_of_person
    

class Currency(models.Model):
    symbol = models.CharField(max_length=32 , null=True, blank=True)
    name = models.CharField(max_length=128 , null=True, blank=True) 
    symbol_native = models.CharField(max_length=50 , null=True, blank=True)
    code = models.CharField(max_length=50, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Currency'

    def __str__(self):
        return self.name

class PaymentTerms(models.Model):
    term_name = models.CharField(max_length=255)
    no_days = models.IntegerField(null=True, blank=True)
    day_of_mon = models.IntegerField(null=True, blank=True)
    day_next_mon = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Payment Terms'

    def __str__(self):
        return self.term_name

class SupplierDetails(models.Model):
    is_active = models.BooleanField(default=True)
    bank_acc_no = models.CharField(max_length=255, null=True, blank=True)
    opening_balance = models.FloatField(default=0)
    open_bal_date = models.DateTimeField(null=True, blank=True)
    pay_recurring = models.BooleanField(default=False)
    is_contractor = models.BooleanField(default=False)
    send_invitation = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)
    pay_term = models.ForeignKey(PaymentTerms, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Supplier Details'

    def __str__(self):
        return self.bank_acc_no

class PaymentMethods(models.Model):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Payment Methods'

    def __str__(self):
        return self.name

class ClientDetails(models.Model):
    bank_acc_no = models.CharField(max_length=255, null=True, blank=True)
    opening_balance = models.FloatField(default=0)
    open_bal_date = models.DateTimeField(null=True, blank=True)
    pay_recurring = models.BooleanField(default=False)
    late_fees = models.BooleanField(default=False)
    pay_reminder = models.BooleanField(default=False)
    tax_exemption = models.BooleanField(default=False)
    send_invitation = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    pay_term = models.ForeignKey(PaymentTerms, on_delete=models.CASCADE)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(PaymentMethods, on_delete=models.CASCADE, )

    class Meta:
        verbose_name_plural = 'Client Details'

    def __str__(self):
        return self.bank_acc_no


class ItemType(models.Model):
    name = models.CharField(max_length=255)
    notes = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Item Types'

    def __str__(self):
        return self.name

class ItemCategory(models.Model):
    name = models.CharField(max_length=255)
    notes = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Item Categories'

    def __str__(self):
        return self.name

class ItemBrands(models.Model):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Item Brands'

    def __str__(self):
        return self.name

class HeadOfAccounts(models.Model):
    is_active = models.BooleanField(default=True)
    head_acc_name = models.CharField(max_length=255)
    notes = models.TextField(null=True, blank=True)
    is_editable = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Head of Accounts'

    def __str__(self):
        return self.head_acc_name

class AccountType(models.Model):
    is_active = models.BooleanField(default=True)
    acc_type_name = models.CharField(max_length=255)
    notes = models.TextField(null=True, blank=True)
    is_editable = models.BooleanField(default=False)
    head_of_accounts = models.ForeignKey(HeadOfAccounts, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Account Type'

    def __str__(self):
        return self.acc_type_name

class AccountName(models.Model):
    is_active = models.BooleanField(default=True)
    acc_code = models.IntegerField() 
    acc_start_date = models.DateTimeField(null=True, blank=True)
    opening_balance = models.FloatField(default=0)
    is_editable = models.BooleanField(default=False)
    is_suspended = models.BooleanField(default=False)
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'Account Name'

    def __str__(self):
        return str(self.acc_code)
    

class Items(models.Model):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    SKU = models.CharField(max_length=255, null=True, blank=True)
    # picture = models.ImageField(upload_to='Items/%Y/%m/%D/')
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
    initial_stock_entry = models.DateTimeField(null=True, blank=True)
    reorder_point = models.IntegerField(null=True, blank=True) 
    max_stock_no = models.IntegerField(null=True, blank=True) 
    lead_time_days = models.IntegerField(null=True, blank=True)
    allow_sales_commision = models.BooleanField(default=True)
    commission_per_item = models.IntegerField() 
    commission_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    tags = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.name

class ItemsGroup(models.Model):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    SKU = models.CharField(max_length=255, null=True, blank=True)
    picture = models.ImageField(upload_to='Items/%Y/%m/%D/')
    item_type = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    volume_cbm = models.FloatField(default=0)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    item_brand = models.ForeignKey(ItemBrands, on_delete=models.CASCADE)
    upc_no = models.CharField(max_length=255, null=True, blank=True)
    item_barcode = models.CharField(max_length=255, null=True, blank=True)
    warranty_month = models.IntegerField(null=True, blank=True) 
    account_name = models.ForeignKey(AccountName, on_delete=models.CASCADE)
    tags = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = 'Items Group'

    def __str__(self):
        return self.name

class ItemGroupMapping(models.Model):
    item_group = models.ForeignKey(ItemsGroup, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)
    
    class Meta:
        verbose_name_plural = 'Item Group Mapping'

    def __str__(self):
        return str(self.quantity)

class InventoryAdjustment(models.Model):
    is_active = models.BooleanField(default=True)
    time_log = models.DateTimeField(null=True, blank=True)
    adjustment_reference_no = models.CharField(max_length=255)
    cause_of_action = models.CharField(max_length=255)
    acc_name = models.ForeignKey(AccountName, on_delete=models.CASCADE)
    comments = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Inventory Adjustment'

    def __str__(self):
        return self.adjustment_reference_no

class InventoryAdjustmentItems(models.Model):
    inventory_adjustment = models.ForeignKey(InventoryAdjustment, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE, null=True, blank=True)
    quantity_or_value = models.BooleanField(default=True)
    value = models.FloatField(default=0)

    class Meta:
        verbose_name_plural = 'Inventory Adjustment Items'

    def __str__(self):
        return str(self.value)

class StorageLocation(models.Model):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Storage Location'

    def __str__(self):
        return self.name

class ItemStorage(models.Model):
    is_active = models.BooleanField(default=True)
    storage_location = models.ForeignKey(StorageLocation, on_delete=models.CASCADE)
    lot_number = models.CharField(max_length=255, null=True, blank=True)
    barcode = models.CharField(max_length=255, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Item Storage'

    def __str__(self):
        return self.lot_number


class ItemStorageMapping(models.Model):
    item_storage = models.ForeignKey(ItemStorage, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True) 
    volume = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Item Storage mapping'

    def __str__(self):
        return self.volume

class ShippingMethodsEnum(enum.Enum):
    GROUND = 1
    PRIORITY = 2
    NEXTDAY = 3
    AIR = 4
    EXPEDITE = 5
    PICKUP = 6

class ItemTransfer(models.Model):
    is_active = models.BooleanField(default=True)
    time_log = models.DateTimeField(null=True, blank=True)
    reference_no = models.CharField(max_length=255)
    from_storage_location = models.ForeignKey(StorageLocation, on_delete=models.CASCADE, related_name="from_storage")
    to_storage_location = models.ForeignKey(StorageLocation, on_delete=models.CASCADE, related_name="to_storage")
    shopping_carrier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    shipping_method = enum.EnumField(ShippingMethodsEnum, default=ShippingMethodsEnum.GROUND)
    shipment_tracking_no = models.CharField(max_length=255, null=True, blank=True)
    shipment_cost = models.FloatField(default=0)
    bilable = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Item Transfer'

    def __str__(self):
        return self.reference_no

class ItemTransferMapping(models.Model):
    item_transfer = models.ForeignKey(ItemTransfer, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    volume = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Item Tansfer Mapping'

    def __str__(self):
        return self.volume