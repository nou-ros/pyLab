import graphene
from graphene_file_upload.scalars import Upload


class SupplierInput(graphene.InputObjectType):
    company_name = graphene.String()
    is_active = graphene.Boolean()
    corporation_no = graphene.String()
    salutation = graphene.String()
    first_name = graphene.String()
    middle_name = graphene.String()
    last_name =  graphene.String()
    display_name = graphene.String()
    logo = Upload()
    website = graphene.String()
    email_address = graphene.String()

class Supplier_Additional_ContactsInput(graphene.InputObjectType):
    is_active = graphene.Boolean()
    salutation = graphene.String()
    first_name = graphene.String()
    middle_name = graphene.String()
    last_name =  graphene.String()
    designation = graphene.String()
    work_phone = graphene.String()
    mobile_phone = graphene.String()
    email_address = graphene.String()
    supplier = graphene.ID()

class CountryInput(graphene.InputObjectType):
  name = graphene.String()
  phone_code = graphene.String()
  short_name = graphene.String()

class SupplierAddressInput(graphene.InputObjectType):
  is_active = graphene.Boolean()
  addresstype = graphene.Int()
  branch_as = graphene.String()
  care_of_person = graphene.String()
  street_address = graphene.String()
  state =  graphene.String()
  zipcode = graphene.String()
  office_number = graphene.String()
  mobile_number = graphene.String()
  fax_number = graphene.String()
  country = graphene.ID()
  supplier = graphene.ID()

class ClientsInput(graphene.InputObjectType):
  is_active = graphene.Boolean()
  is_corporation = graphene.Boolean()
  company_name = graphene.String()
  salutation = graphene.String()
  first_name = graphene.String()
  middle_name = graphene.String()
  last_name =  graphene.String()
  display_name = graphene.String()
  photo = Upload()
  website = graphene.String()
  email_address = graphene.String()
 
class ClientAdditionalContactsInput(graphene.InputObjectType):
  is_active = graphene.Boolean()
  salutation = graphene.String()
  first_name = graphene.String()
  middle_name = graphene.String()
  last_name =  graphene.String()
  designation = graphene.String()
  work_phone = graphene.String()
  mobile_phone = graphene.String()
  email_address = graphene.String()
  client = graphene.ID()

class ClientAddressInput(graphene.InputObjectType):
  is_active = graphene.Boolean()
  addresstype = graphene.Int()
  branch_as = graphene.String()
  care_of_person = graphene.String()
  street_address = graphene.String()
  city = graphene.String()
  state =  graphene.String()
  zipcode = graphene.String()
  office_number = graphene.String()
  mobile_number = graphene.String()
  fax_number = graphene.String()
  country = graphene.ID()
  client = graphene.ID()

class CurrencyInput(graphene.InputObjectType):
  name = graphene.String()
  symbol_native = graphene.String()
  code = graphene.String()
  country = graphene.ID()

class PaymentTermsInput(graphene.InputObjectType):
  term_name = graphene.String()
  no_days = graphene.Int()
  day_of_mon = graphene.Int()
  day_next_mon = graphene.Int()

class SupplierDetailsInput(graphene.InputObjectType):
  is_active = graphene.Boolean()
  bank_acc_no = graphene.String()
  open_bal_date = graphene.String()
  opening_balance = graphene.Float()
  pay_recurring = graphene.Boolean()
  is_contractor = graphene.Boolean()
  send_invitation = graphene.Boolean()
  notes = graphene.String()
  pay_term = graphene.ID()
  currency = graphene.ID()
  supplier = graphene.ID()

class PaymentMethodsInput(graphene.InputObjectType):
  is_active = graphene.Boolean()
  name = graphene.String()
  notes = graphene.String()

class ClientDetailsInput(graphene.InputObjectType):
  bank_acc_no = graphene.String()
  opening_balance = graphene.Float()
  open_bal_date = graphene.String()
  pay_recurring = graphene.Boolean()
  late_fees = graphene.Boolean()
  pay_reminder = graphene.Boolean()
  tax_exemption = graphene.Boolean()
  send_invitation = graphene.Boolean()
  notes = graphene.String()
  pay_term = graphene.ID()
  currency = graphene.ID()
  client = graphene.ID()
  payment_method = graphene.ID()

class ItemTypeInput(graphene.InputObjectType):
  name = graphene.String()
  notes = graphene.String()

class ItemCategoryInput(graphene.InputObjectType):
  name = graphene.String()
  notes = graphene.String()

class ItemBrandsInput(graphene.InputObjectType):
  is_active = graphene.Boolean()
  name = graphene.String()
  notes = graphene.String()

class Head_of_AccountsInput(graphene.InputObjectType):
  is_active = graphene.Boolean()
  head_acc_name = graphene.String()
  notes = graphene.String()
  is_editable = graphene.Boolean()

class AccountTypeInput(graphene.InputObjectType):
  is_active = graphene.Boolean()
  acc_type_name = graphene.String()
  notes = graphene.String()
  is_editable = graphene.Boolean()
  head_of_account = graphene.ID()

class AccountNameInput(graphene.InputObjectType):
  is_active = graphene.Boolean()
  acc_code = graphene.Int()
  acc_start_date = graphene.String()
  opening_balance = graphene.Float()
  is_editable = graphene.Boolean()
  is_suspended = graphene.Boolean()
  account_type = graphene.ID()

class ItemsInput(graphene.InputObjectType):
  is_active = graphene.Boolean()
  name = graphene.String()
  description = graphene.String()
  SKU = graphene.String()
  purchase_price = graphene.Float()
  sales_price = graphene.Float()
  markup_price = graphene.Decimal()
  min_sales_price = graphene.Float()
  weight_param = graphene.String()
  weight_values = graphene.Float()
  volume_cbm =  graphene.Float()
  upc_no = graphene.String()
  mpn_no = graphene.String()
  ean_no = graphene.String()
  isbn_no = graphene.String()
  item_barcode = graphene.String()
  warranty_month = graphene.Int()
  stock_in_hand = graphene.Float()
  initial_stock_entry = graphene.String()
  reorder_point = graphene.Int()
  max_stock_no = graphene.Int()
  lead_time_days = graphene.Int()
  allow_sales_commision = graphene.Boolean()
  commission_per_item = graphene.Int()
  commission_percentage =  graphene.Decimal()
  picture = Upload()
  tags = graphene.String()
  item_type = graphene.ID()
  item_category = graphene.ID()
  supplier = graphene.ID()
  item_brand = graphene.ID()
  account_name = graphene.ID()

class ItemGroupInput(graphene.InputObjectType):
  is_active = graphene.Boolean()
  name = graphene.String()
  description = graphene.String()
  SKU = graphene.String()
  volume_cbm =  graphene.Float()
  upc_no = graphene.String()
  warranty_month = graphene.Int()
  tags = graphene.String()
  item_barcode = graphene.String()
  picture = Upload()
  item_type = graphene.ID()
  supplier = graphene.ID()
  item_brand = graphene.ID()
  account_name = graphene.ID()

class ItemGroupMappingInput(graphene.InputObjectType):
  item_groups = ItemGroupInput()
  items = graphene.List(ItemsInput)
  mapping_quantity =  graphene.Float()

class ItemGroupMappingUpdateInput(graphene.InputObjectType):
  id = graphene.ID()
  item_groups = graphene.ID()
  items = graphene.ID()
  mapping_quantity =  graphene.Float()

class InventoryAdjustmentInput(graphene.InputObjectType):
  is_active = graphene.Boolean()
  time_log = graphene.String()
  adjustment_reference_no = graphene.String()
  cause_of_action = graphene.String()
  comments = graphene.String()
  acc_name = graphene.ID()

class InventoryAdjustmentItemsInput(graphene.InputObjectType):
  inventory_adjustment = graphene.ID()
  item = graphene.ID()
  quantity_or_value = graphene.Boolean()
  value = graphene.Float()

class StorageLocationInput(graphene.InputObjectType):
  is_active = graphene.Boolean()
  name = graphene.String()
  address = graphene.String()
  country = graphene.ID()
  state = graphene.String()
  city = graphene.String()
  zipcode = graphene.String()
  notes = graphene.String()

class ItemStorageInput(graphene.InputObjectType):
  is_active = graphene.Boolean()
  lot_number = graphene.String()
  barcode = graphene.String()
  notes = graphene.String()
  storage_location = graphene.ID()

class ItemStorageMappingInput(graphene.InputObjectType):
  quantity = graphene.Int()
  volume = graphene.String()
  item_storage = ItemStorageInput()
  items = graphene.List(ItemsInput)

class ItemStorageMappingUpdateInput(graphene.InputObjectType):
  id = graphene.ID()
  quantity = graphene.Int()
  volume = graphene.String()
  item_storage = graphene.ID()
  items = graphene.ID()

class ItemTransferInput(graphene.InputObjectType):
  is_active = graphene.Boolean()
  time_log = graphene.String()
  reference_no = graphene.String()
  from_storage_location = graphene.ID()
  to_storage_location = graphene.ID()
  shopping_carrier = graphene.ID()
  shipping_method = graphene.Int()
  shipment_tracking_no = graphene.String()
  shipment_cost = graphene.Float()
  bilable = graphene.Boolean()
  notes = graphene.String()

class ItemTransferMappingInput(graphene.InputObjectType):
  quantity = graphene.Int()
  volume = graphene.String()
  item_transfer = ItemTransferInput()
  items = graphene.List(ItemsInput)

class ItemTransferMappingUpdateInput(graphene.InputObjectType):
  id = graphene.ID()
  quantity = graphene.Int()
  volume = graphene.String()
  item_transfer = graphene.ID()
  items = graphene.ID()