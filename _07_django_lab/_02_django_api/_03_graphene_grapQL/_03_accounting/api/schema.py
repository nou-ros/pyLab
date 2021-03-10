import graphene
from .utils import prepare_model_data_from_dict

from graphene_django import DjangoObjectType 

from graphql import GraphQLError

from .models import *

import graphql_jwt

from graphql_jwt.decorators import login_required

from django.db import transaction

# APB - 1
class SupplierType(DjangoObjectType):
    class Meta: 
        model = Supplier

# APB - 2 
class Supplier_Additional_ContactsType(DjangoObjectType):
    class Meta:
        model = SupplierAdditionalContacts

# APB - 3
class CountryType(DjangoObjectType):
  class Meta:
    model = Country

class SupplierAddressType(DjangoObjectType):
  class Meta:
    model = SupplierAddress

# APB - 4
class ClientsType(DjangoObjectType):
  class Meta:
    model = Clients

# APB-5
class ClientAdditionalContactsType(DjangoObjectType):
  class Meta:
    model = ClientAdditionalContacts

# APB-6
class ClientAddressType(DjangoObjectType):
  class Meta:
    model = ClientAddress

# APB-7
class CurrencyType(DjangoObjectType):
  class Meta:
    model = Currency

class PaymentTermsType(DjangoObjectType):
  class Meta:
    model = PaymentTerms

class SupplierDetailsType(DjangoObjectType):
  class Meta:
    model = SupplierDetails

# APB - 8
class PaymentMethodType(DjangoObjectType):
  class Meta:
    model = PaymentMethods

class ClientDetailsType(DjangoObjectType):
  class Meta:
    model = ClientDetails

# APB - 9
class ItemtypeType(DjangoObjectType):
  class Meta:
    model = ItemType

class ItemCategoryType(DjangoObjectType):
  class Meta:
    model = ItemCategory

class ItemBrandsType(DjangoObjectType):
  class Meta:
    model = ItemBrands

# APB - 10
class Head_of_AccountsType(DjangoObjectType):
  class Meta:
    model = HeadOfAccounts

class AccounttypeType(DjangoObjectType):
  class Meta:
    model = AccountType

class AccountNameType(DjangoObjectType):
  class Meta:
    model = AccountName

class ItemsType(DjangoObjectType):
  class Meta:
    model = Items
# APB-11
class ItemsGroupType(DjangoObjectType):
  class Meta:
    model = ItemsGroup
    
class ItemGroupMappingType(DjangoObjectType):
  class Meta:
    model = ItemGroupMapping

# APB-12
class InventoryAdjustmentType(DjangoObjectType):
  class Meta:
    model = InventoryAdjustment

class InventoryAdjustmentItemsType(DjangoObjectType):
  class Meta:
    model = InventoryAdjustmentItems

class StorageLocationType(DjangoObjectType):
  class Meta:
    model = StorageLocation

class ItemStorageType(DjangoObjectType):
  class Meta:
    model = ItemStorage

class ItemStorageMappingType(DjangoObjectType):
  class Meta:
    model = ItemStorageMapping

class ItemTransferType(DjangoObjectType):
  class Meta:
    model = ItemTransfer

class ItemTransferMappingType(DjangoObjectType):
  class Meta:
    model = ItemTransferMapping

class Query(graphene.ObjectType):
    suppliers = graphene.List(SupplierType, company_name = graphene.String())

    supplier_additional_contacts = graphene.List(Supplier_Additional_ContactsType, id = graphene.ID())

    supplier_address = graphene.List(SupplierAddressType, id = graphene.ID())

    clients = graphene.List(ClientsType, id = graphene.ID())

    client_additional_contacts = graphene.List(ClientAdditionalContactsType, id = graphene.ID())

    client_address = graphene.List(ClientAddressType, id = graphene.ID())

    payment_terms = graphene.List(PaymentTermsType, id = graphene.ID())
    supplier_details = graphene.List(SupplierDetailsType, id = graphene.ID())

    client_details = graphene.List(ClientDetailsType, id = graphene.ID())

    item_type = graphene.List(ItemtypeType, id = graphene.ID())
    item_category = graphene.List(ItemCategoryType, id = graphene.ID())
    item_brands = graphene.List(ItemBrandsType, id = graphene.ID())

    items = graphene.List(ItemsType, id = graphene.ID())
    
    item_group = graphene.List(ItemsGroupType, id = graphene.ID())
    item_group_mapping = graphene.List(ItemGroupMappingType, id = graphene.ID())

    inventory_adjustment = graphene.List(InventoryAdjustmentType, id = graphene.ID())
    inventory_adjustment_items = graphene.List(InventoryAdjustmentItemsType, id = graphene.ID())
    storage_location = graphene.List(StorageLocationType, id = graphene.ID())

    item_storage = graphene.List(ItemStorageType, id = graphene.ID())

    item_storage_mapping = graphene.List(ItemStorageMappingType, id=graphene.ID())
    
    item_transfer = graphene.List(ItemTransferType, id=graphene.ID())
    
    item_transfer_mapping = graphene.List(ItemTransferMappingType, id=graphene.ID())

    def resolve_suppliers(self, info, **kwargs):
        company_name = kwargs.get('company_name')

        if company_name is not None:
            return [Supplier.objects.get(company_name=company_name)]
        else:
            return Supplier.objects.all()
    
    def resolve_supplier_additional_contacts(self, info, **kwargs):
        suppAdd = kwargs.get('id')
        if suppAdd is not None:
            return list(SupplierAdditionalContacts.objects.filter(pk=id))
        else:
            return SupplierAdditionalContacts.objects.all()

    def resolve_supplier_address(self, info, **kwargs):
      address = kwargs.get('id')
      # print(kwargs.get('address_type'))
      if address is not None:
        return list(SupplierAddress.objects.filter(pk=address))
      else:
        return SupplierAddress.objects.all()

    @login_required
    def resolve_clients(self, info, **kwargs):
      # either this approach or @login_required
      # user = info.context.user
      # if not user.is_authenticated:
      #   raise Exception(' Auth credentials are needed')
      client = kwargs.get('id')
      if client is not None:
        return list(Clients.objects.filter(pk=client))
      else:
        return Clients.objects.all() 

    def resolve_client_additional_contacts(self, info, **kwargs):
      client_add = kwargs.get('id')
      if client_add is not None:
        return list(ClientAdditionalContacts.objects.filter(pk=client_add))
      else:
        return ClientAdditionalContacts.objects.all()
      
    def resolve_client_address(self, info, **kwargs):
      address = kwargs.get('id')
      # print(kwargs.get('address_type'))
      if address is not None:
        return list(ClientAddress.objects.filter(pk=address))
      else:
        return ClientAddress.objects.all()

    def resolve_payment_terms(self, info, **kwargs):
      payment = kwargs.get('id')
      if payment is not None:
        return list(PaymentTerms.objects.filter(pk=payment))
      else:
        return PaymentTerms.objects.all()

    def resolve_supplier_details(self, info, **kwargs):
      supplier_details = kwargs.get('id')
      if supplier_details is not None:
        return list(SupplierDetails.objects.filter(pk=supplier_details))
      else:
        return SupplierDetails.objects.all()

    def resolve_client_details(self, info, **kwargs):
      client_details = kwargs.get('id')
      if client_details is not None:
        return list(ClientDetails.objects.filter(pk=client_details))
      else:
        return ClientDetails.objects.all()
    
    def resolve_item_type(self, info, **kwargs):
      item_type = kwargs.get('id')
      if item_type is not None:
        return list(ItemType.objects.filter(pk=item_type))
      else:
        return ItemType.objects.all()

    def resolve_item_category(self, info, **kwargs):
      item_category = kwargs.get('id')
      if item_category is not None:
        return list(ItemCategory.objects.filter(pk=item_category))
      else:
        return ItemCategory.objects.all()

    def resolve_item_brands(self, info, **kwargs):
      item_brand = kwargs.get('id')
      if item_brand is not None:
        return list(ItemBrands.objects.filter(pk=item_brand))
      else:
        return ItemBrands.objects.all()

    def resolve_items(self, info, **kwargs):
      items = kwargs.get('id')
      if items is not None:
        return list(Items.objects.filter(pk=items))
      else:
        return Items.objects.all()

    def resolve_item_group(self, info, **kwargs):
      item_group = kwargs.get('id')
      if item_group is not None:
        return list(ItemsGroup.objects.filter(pk=item_group))
      else:
        return ItemsGroup.objects.all()

    def resolve_item_group_mapping(self, info, **kwargs):
      item_group_mapping = kwargs.get('id')
      if item_group_mapping is not None:
        return list(ItemGroupMapping.objects.filter(pk=item_group_mapping))
      else:
        return ItemGroupMapping.objects.all()
    
    def resolve_inventory_adjustment(self, info, **kwargs):
      inventory_adjustment = kwargs.get('id')
      if inventory_adjustment is not None:
        return list(InventoryAdjustment.objects.filter(pk=inventory_adjustment))
      else:
        return InventoryAdjustment.objects.all()

    def resolve_inventory_adjustment_items(self, info, **kwargs):
      inventory_adjustment_items = kwargs.get('id')
      if inventory_adjustment_items is not None:
        return list(InventoryAdjustmentItems.objects.filter(pk=inventory_adjustment_items))
      else:
        return InventoryAdjustmentItems.objects.all()

    def resolve_storage_location(self, info, **kwargs):
      storage_location = kwargs.get('id')
      if storage_location is not None:
        return list(StorageLocation.objects.filter(pk=storage_location))
      else:
        return StorageLocation.objects.all()

    def resolve_item_storage(self, info, **kwargs):
      item_storage = kwargs.get('id')
      if item_storage is not None:
        return list(ItemStorage.objects.filter(pk=item_storage))
      else:
        return ItemStorage.objects.all()

    def resolve_item_storage_mapping(self, info, **kwargs):
      item_storage_mapping = kwargs.get('id')
      if item_storage_mapping is not None:
        return list(ItemStorageMapping.objects.filter(pk=item_storage_mapping))
      else:
        return ItemStorageMapping.objects.all()

    def resolve_item_transfer(self, info, **kwargs):
      item_transfer = kwargs.get('id')
      if item_transfer is not None:
        return list(ItemTransfer.objects.filter(pk=item_transfer))
      else:
        return ItemTransfer.objects.all()
    
    def resolve_item_transfer_mapping(self, info, **kwargs):
      item_transfer_mapping = kwargs.get('id')
      if item_transfer_mapping is not None:
        return list(ItemTransferMapping.objects.filter(pk=item_transfer_mapping))
      else:
        return ItemTransferMapping.objects.all()

# inputs
class SupplierInput(graphene.InputObjectType):
    company_name = graphene.String()
    is_active = graphene.Boolean()
    corporation_no = graphene.String()
    salutation = graphene.String()
    first_name = graphene.String()
    middle_name = graphene.String()
    last_name =  graphene.String()
    display_name = graphene.String()
    logo = graphene.String()
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
  # photo = graphene.String()
  # photo = Upload()
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
  open_bal_date = graphene.DateTime()
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
  open_bal_date = graphene.DateTime()
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
  acc_start_date = graphene.DateTime()
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
  initial_stock_entry = graphene.DateTime()
  reorder_point = graphene.Int()
  max_stock_no = graphene.Int()
  lead_time_days = graphene.Int()
  allow_sales_commision = graphene.Boolean()
  commission_per_item = graphene.Int()
  commission_percentage =  graphene.Decimal()
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
  time_log = graphene.DateTime()
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
  time_log = graphene.DateTime()
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

#Mutation
class CreateSupplier(graphene.Mutation):
    class Arguments:
        input = SupplierInput(required=True)
    
    supplier = graphene.Field(SupplierType)

    def mutate(self, info, input=None):
        supplier_instance = Supplier(company_name=input.company_name, is_active=input.is_active, corporation_no=input.corporation_no, salutation=input.salutation, first_name=input.first_name, middle_name=input.middle_name, last_name=input.last_name,display_name=input.display_name, logo=input.logo, website=input.website, email_address=input.email_address)
        supplier_instance.save()

        return CreateSupplier(supplier=supplier_instance)

class UpdateSupplier(graphene.Mutation):
    class Arguments:

        id = graphene.ID(required=True)
        input = SupplierInput(required=True)

    supplier = graphene.Field(SupplierType)

    def mutate(self, info, id, input=None):
        supplier_instance = Supplier.objects.get(pk=id)

        if supplier_instance:
            if supplier_instance.company_name is not None:
                supplier_instance.company_name = input.company_name

            if supplier_instance.is_active is not None:
                supplier_instance.is_active = input.is_active

            if supplier_instance.corporation_no is not None:
                supplier_instance.corporation_no = input.corporation_no
            
            if supplier_instance.salutation is not None:
                supplier_instance.salutation = input.salutation

            if supplier_instance.first_name is not None:
                supplier_instance.first_name = input.first_name

            if supplier_instance.middle_name is not None:
                supplier_instance.middle_name = input.middle_name
            
            if supplier_instance.last_name is not None:
                supplier_instance.last_name = input.last_name

            if supplier_instance.display_name is not None:
                supplier_instance.display_name = input.display_name

            if supplier_instance.logo is not None:
                supplier_instance.logo = input.logo

            if supplier_instance.website is not None:
                supplier_instance.website = input.website
            
            if supplier_instance.email_address is not None:
                supplier_instance.email_address = input.email_address

                supplier_instance.save()

            return UpdateSupplier(supplier=supplier_instance)
            

class DeleteSupplier(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    supplier = graphene.Field(SupplierType)

    def mutate(self, info, id):
        supplier_instance = Supplier.objects.get(pk=id)
        supplier_instance.delete()

        return DeleteSupplier(supplier=None)

class Create_Supplier_Additional_Contacts(graphene.Mutation):
    class Arguments:
        input = Supplier_Additional_ContactsInput(required=True)
    
    supplier_additional_contacts = graphene.Field(Supplier_Additional_ContactsType)

    def mutate(self, info, input=None):
        supAdd = input.get("supplier")
        supplier = Supplier.objects.get(pk=supAdd)

        supplier_additional_contacts_instance = SupplierAdditionalContacts(is_active=input.is_active, salutation=input.salutation, first_name=input.first_name, middle_name=input.middle_name, last_name=input.last_name, designation=input.designation, work_phone=input.work_phone, mobile_phone=input.mobile_phone, email_address=input.email_address)

        supplier_additional_contacts_instance.supplier = supplier
        supplier_additional_contacts_instance.save()

        return Create_Supplier_Additional_Contacts(supplier_additional_contacts=supplier_additional_contacts_instance)


class Update_Supplier_Additional_Contacts(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = Supplier_Additional_ContactsInput(required=True)
    
    supplier_additional_contacts = graphene.Field(Supplier_Additional_ContactsType)

    def mutate(self, info, id, input=None):
        supplier_additional_contacts_instance = Supplier_Additional_Contacts.objects.get(pk=id)
        supplier = input.get("supplier")
        # print(supplier)
        supplier = Supplier.objects.get(pk=supplier)
        # print(supplier)

        if supplier_additional_contacts_instance:

            if supplier_additional_contacts_instance.is_active is not None:
                supplier_additional_contacts_instance.is_active = input.is_active
            
            if supplier_additional_contacts_instance.salutation is not None:
                supplier_additional_contacts_instance.salutation = input.salutation

            if supplier_additional_contacts_instance.first_name is not None:
                supplier_additional_contacts_instance.first_name = input.first_name

            if supplier_additional_contacts_instance.middle_name is not None:
                supplier_additional_contacts_instance.middle_name = input.middle_name
            
            if supplier_additional_contacts_instance.last_name is not None:
                supplier_additional_contacts_instance.last_name = input.last_name

            if supplier_additional_contacts_instance.designation is not None:
                supplier_additional_contacts_instance.designation = input.designation

            if supplier_additional_contacts_instance.work_phone is not None:
                supplier_additional_contacts_instance.work_phone = input.work_phone

            if supplier_additional_contacts_instance.mobile_phone is not None:
                supplier_additional_contacts_instance.mobile_phone = input.mobile_phone
            
            if supplier_additional_contacts_instance.email_address is not None:
                supplier_additional_contacts_instance.email_address = input.email_address
            
            if supplier_additional_contacts_instance.supplier is not None:
                supplier_additional_contacts_instance.supplier = supplier

            supplier_additional_contacts_instance.save()

            return Update_Supplier_Additional_Contacts(supplier_additional_contacts=supplier_additional_contacts_instance)

class Delete_Supplier_Additional_Contacts(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    supplier_additional_contacts = graphene.Field(Supplier_Additional_ContactsType)

    def mutate(self, info, id):
        supplier_additional_contacts = SupplierAdditionalContacts.objects.get(pk=id)
        supplier_additional_contacts.delete()

        return Delete_Supplier_Additional_Contacts(supplier_additional_contacts=None)


class CreateSupplierAddress(graphene.Mutation):
  class Arguments:
    input = SupplierAddressInput(required=True)

  supplier_address = graphene.Field(SupplierAddressType)

  def mutate(self, info, input=None):
    country = input.get("country")
    country = Country.objects.get(pk=country)
    supplier = input.get("supplier")
    supplier = Supplier.objects.get(pk=supplier)

    supplier_address_instance = SupplierAddress(is_active=input.is_active, addresstype=input.addresstype, branch_as=input.branch_as, care_of_person=input.care_of_person, street_address=input.street_address, state=input.state, zipcode=input.zipcode, office_number=input.office_number, mobile_number=input.mobile_number, fax_number=input.fax_number)
    print("address_type: ", input.addresstype)
    supplier_address_instance.country = country
    supplier_address_instance.supplier = supplier
    supplier_address_instance.save()

    return CreateSupplierAddress(supplier_address=supplier_address_instance)

class DeleteSupplierAddress(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    supplier_address = graphene.Field(SupplierAddressType)

    def mutate(self, info, id):
        supplier_address = SupplierAddress.objects.get(pk=id)
        supplier_address.delete()

        return DeleteSupplierAddress(supplier_address=None)

class UpdateSupplierAddress(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)
    input = SupplierAddressInput(required=True)

  supplier_address = graphene.Field(SupplierAddressType)

  def mutate(self, info, id, input=None):
    supplier_address_instance =  SupplierAddress.objects.get(pk=id)

    country = input.get("country")
    country = Country.objects.get(pk=country)
    supplier = input.get("supplier")
    supplier = Supplier.objects.get(pk=supplier)

    if supplier_address_instance:
      if supplier_address_instance.is_active is not None:
                supplier_address_instance.is_active = input.is_active
      if supplier_address_instance.addresstype is not None:
                supplier_address_instance.addresstype = input.addresstype
      if supplier_address_instance.branch_as is not None:
                supplier_address_instance.branch_as = input.branch_as
      if supplier_address_instance.care_of_person is not None:
                supplier_address_instance.care_of_person = input.care_of_person
      if supplier_address_instance.street_address is not None:
                supplier_address_instance.street_address = input.street_address
      if supplier_address_instance.state is not None:
                supplier_address_instance.state = input.state
      if supplier_address_instance.zipcode is not None:
                supplier_address_instance.zipcode = input.zipcode
      if supplier_address_instance.office_number is not None:
                supplier_address_instance.office_number = input.office_number
      if supplier_address_instance.mobile_number is not None:
                supplier_address_instance.mobile_number = input.mobile_number
      if supplier_address_instance.fax_number is not None:
                supplier_address_instance.fax_number = input.fax_number
      if supplier_address_instance.country is not None:
                supplier_address_instance.country = country
      if supplier_address_instance.supplier is not None:
                supplier_address_instance.supplier = supplier

      supplier_address_instance.save()

      return UpdateSupplierAddress(supplier_address=supplier_address_instance)


class CreateClient(graphene.Mutation):
  class Arguments:
    input = ClientsInput(required=True)
    
  client = graphene.Field(ClientsType)
  

  def mutate(self, info, input=None):
      client_instance = Clients(is_active=input.is_active, is_corporation=input.is_corporation, company_name=input.company_name, salutation=input.salutation, first_name=input.first_name, middle_name=input.middle_name, last_name=input.last_name,display_name=input.display_name, website=input.website, email_address=input.email_address)
      client_instance.save()

      return CreateClient(client=client_instance)

class DeleteClient(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)

  client = graphene.Field(ClientsType)
  
  def mutate(self, info, id):
      client_instance = Clients.objects.get(pk=id)
      client_instance.delete()

      return DeleteClient(client=None)

class UpdateClient(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)
    input = ClientsInput(required=True)

  client = graphene.Field(ClientsType)

  def mutate(self, info, id, input=None):
    client_instance =  Clients.objects.get(pk=id)

    if client_instance:
      if client_instance.is_active is not None:
                client_instance.is_active = input.is_active
      if client_instance.is_corporation is not None:
                client_instance.is_corporation = input.is_corporation
      if client_instance.company_name is not None:
                client_instance.company_name = input.company_name
      if client_instance.salutation is not None:
                client_instance.salutation = input.salutation
      if client_instance.first_name is not None:
                client_instance.first_name = input.first_name
      if client_instance.middle_name is not None:
                client_instance.middle_name = input.middle_name
      if client_instance.last_name is not None:
                client_instance.last_name = input.last_name
      if client_instance.display_name is not None:
                client_instance.display_name = input.display_name
      if client_instance.website is not None:
                client_instance.website = input.website
      if client_instance.email_address is not None:
                client_instance.email_address = input.email_address

      client_instance.save()

      return UpdateClient(client=client_instance)


class Create_Client_Additional_Contacts(graphene.Mutation):
    class Arguments:
        input = ClientAdditionalContactsInput(required=True)
    
    client_additional_contacts = graphene.Field(ClientAdditionalContactsType)

    def mutate(self, info, input=None):
        client = input.get("client")
        client = Clients.objects.get(pk=client)

        client_additional_contacts_instance = ClientAdditionalContacts(is_active=input.is_active, salutation=input.salutation, first_name=input.first_name, middle_name=input.middle_name, last_name=input.last_name, designation=input.designation, work_phone=input.work_phone, mobile_phone=input.mobile_phone, email_address=input.email_address)

        client_additional_contacts_instance.client = client
        client_additional_contacts_instance.save()

        return Create_Client_Additional_Contacts(client_additional_contacts=client_additional_contacts_instance)

class Update_Client_Additional_Contacts(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = ClientAdditionalContactsInput(required=True)
    
    client_additional_contacts = graphene.Field(ClientAdditionalContactsType)

    def mutate(self, info, id, input=None):
        client_additional_contacts_instance = ClientAdditionalContacts.objects.get(pk=id)
        client = input.get("client")
        # print(client)
        client = Clients.objects.get(pk=client)
        # print(client)

        if client_additional_contacts_instance:

            if client_additional_contacts_instance.is_active is not None:
                client_additional_contacts_instance.is_active = input.is_active
            
            if client_additional_contacts_instance.salutation is not None:
                client_additional_contacts_instance.salutation = input.salutation

            if client_additional_contacts_instance.first_name is not None:
                client_additional_contacts_instance.first_name = input.first_name

            if client_additional_contacts_instance.middle_name is not None:
                client_additional_contacts_instance.middle_name = input.middle_name
            
            if client_additional_contacts_instance.last_name is not None:
                client_additional_contacts_instance.last_name = input.last_name

            if client_additional_contacts_instance.designation is not None:
                client_additional_contacts_instance.designation = input.designation

            if client_additional_contacts_instance.work_phone is not None:
                client_additional_contacts_instance.work_phone = input.work_phone

            if client_additional_contacts_instance.mobile_phone is not None:
                client_additional_contacts_instance.mobile_phone = input.mobile_phone
            
            if client_additional_contacts_instance.email_address is not None:
                client_additional_contacts_instance.email_address = input.email_address
            
            if client_additional_contacts_instance.client is not None:
                client_additional_contacts_instance.client = client

            client_additional_contacts_instance.save()

            return Update_Client_Additional_Contacts(client_additional_contacts=client_additional_contacts_instance)

class Delete_Client_Additional_Contacts(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    client_additional_contacts = graphene.Field(ClientAdditionalContactsType)

    def mutate(self, info, id):
        client_additional_contacts = ClientAdditionalContacts.objects.get(pk=id)
        client_additional_contacts.delete()

        return Delete_Client_Additional_Contacts(client_additional_contacts=None)


class CreateClientAddress(graphene.Mutation):
  class Arguments:
    input = ClientAddressInput(required=True)

  client_address = graphene.Field(ClientAddressType)

  def mutate(self, info, input=None):
    country = input.get("country")
    country = Country.objects.get(pk=country)
    client = input.get("client")
    client = Clients.objects.get(pk=client)

    client_address_instance = ClientAddress(is_active=input.is_active, addresstype=input.addresstype, branch_as=input.branch_as, care_of_person=input.care_of_person, street_address=input.street_address, city=input.city, state=input.state, zipcode=input.zipcode, office_number=input.office_number, mobile_number=input.mobile_number, fax_number=input.fax_number)
    client_address_instance.country = country
    client_address_instance.client = client
    client_address_instance.save()

    return CreateClientAddress(client_address=client_address_instance)

class DeleteClientAddress(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    client_address = graphene.Field(ClientAddressType)

    def mutate(self, info, id):
        client_address = ClientAddress.objects.get(pk=id)
        client_address.delete()

        return DeleteClientAddress(client_address=None)

class UpdateClientAddress(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)
    input = ClientAddressInput(required=True)

  client_address = graphene.Field(ClientAddressType)

  def mutate(self, info, id, input=None):
    client_address_instance =  ClientAddress.objects.get(pk=id)

    country = input.get("country")
    country = Country.objects.get(pk=country)
    client = input.get("client")
    client = Clients.objects.get(pk=client)

    if client_address_instance:
      if client_address_instance.is_active is not None:
                client_address_instance.is_active = input.is_active
      if client_address_instance.addresstype is not None:
                client_address_instance.addresstype = input.addresstype
      if client_address_instance.branch_as is not None:
                client_address_instance.branch_as = input.branch_as
      if client_address_instance.care_of_person is not None:
                client_address_instance.care_of_person = input.care_of_person
      if client_address_instance.street_address is not None:
                client_address_instance.street_address = input.street_address
      if client_address_instance.state is not None:
                client_address_instance.state = input.state
      if client_address_instance.city is not None:
                client_address_instance.city = input.city
      if client_address_instance.zipcode is not None:
                client_address_instance.zipcode = input.zipcode
      if client_address_instance.office_number is not None:
                client_address_instance.office_number = input.office_number
      if client_address_instance.mobile_number is not None:
                client_address_instance.mobile_number = input.mobile_number
      if client_address_instance.fax_number is not None:
                client_address_instance.fax_number = input.fax_number
      if client_address_instance.country is not None:
                client_address_instance.country = country
      if client_address_instance.client is not None:
                client_address_instance.client = client

      client_address_instance.save()

      return UpdateClientAddress(client_address=client_address_instance)


class CreatePaymentTerms(graphene.Mutation):
  class Arguments:
    input = PaymentTermsInput(required=True)

  payment_terms = graphene.Field(PaymentTermsType)

  def mutate(self, info, input=None):
    payment_terms_instance = PaymentTerms(term_name=input.term_name, no_days=input.no_days, day_of_mon=input.day_of_mon, day_next_mon=input.day_next_mon)
    payment_terms_instance.save()

    return CreatePaymentTerms(payment_terms=payment_terms_instance)

class DeletePaymentTerms(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)

  payment_terms = graphene.Field(PaymentTermsType)
  
  def mutate(self, info, id):
      payment_terms_instance = PaymentTerms.objects.get(pk=id)
      payment_terms_instance.delete()

      return DeletePaymentTerms(payment_terms=None)

class UpdatePaymentTerms(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)
    input = PaymentTermsInput(required=True)

  payment_terms = graphene.Field(PaymentTermsType)

  def mutate(self, info, id, input=None):
    payment_terms_instance =  PaymentTerms.objects.get(pk=id)

    if payment_terms_instance:
      if payment_terms_instance.term_name is not None:
        payment_terms_instance.term_name = input.term_name
      if payment_terms_instance.no_days is not None:
        payment_terms_instance.no_days = input.no_days
      if payment_terms_instance.day_of_mon is not None:
        payment_terms_instance.day_of_mon = input.day_of_mon
      if payment_terms_instance.day_next_mon is not None:
        payment_terms_instance.day_next_mon = input.day_next_mon
      payment_terms_instance.save()

      return UpdatePaymentTerms(payment_terms=payment_terms_instance)


class CreateSupplierDetails(graphene.Mutation):
  class Arguments:
    input = SupplierDetailsInput(required=True)

  supplier_details = graphene.Field(SupplierDetailsType)

  def mutate(self, info, input=None):
    pay_term = input.get("pay_term")
    pay_term = PaymentTerms.objects.get(pk=pay_term)
    currency = input.get("currency")
    currency = Currency.objects.get(pk=currency)
    supplier= input.get("supplier")
    supplier = Supplier.objects.get(pk=supplier)

    supplier_details_instance = SupplierDetails(is_active=input.is_active, bank_acc_no=input.bank_acc_no, opening_balance=input.opening_balance,  open_bal_date=input.open_bal_date, pay_recurring=input.pay_recurring, is_contractor=input.is_contractor, send_invitation=input.send_invitation, notes=input.notes)

    supplier_details_instance.pay_term = pay_term
    supplier_details_instance.currency = currency
    supplier_details_instance.supplier = supplier
    supplier_details_instance.save()

    return CreateSupplierDetails(supplier_details=supplier_details_instance)

class UpdateSupplierDetails(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = SupplierDetailsInput(required=True)
    
    supplier_details = graphene.Field(SupplierDetailsType)

    def mutate(self, info, id, input=None):
        supplier_details_instance = SupplierDetails.objects.get(pk=id)
        pay_term = input.get("pay_term")
        pay_term = PaymentTerms.objects.get(pk=pay_term)
        currency = input.get("currency")
        currency = Currency.objects.get(pk=currency)
        supplier= input.get("supplier")
        supplier = Supplier.objects.get(pk=supplier)

        if supplier_details_instance:

            if supplier_details_instance.is_active is not None:
                supplier_details_instance.is_active = input.is_active
            
            if supplier_details_instance.bank_acc_no is not None:
                supplier_details_instance.bank_acc_no = input.bank_acc_no

            if supplier_details_instance.opening_balance is not None:
                supplier_details_instance.opening_balance = input.opening_balance
            
            if supplier_details_instance.open_bal_date is not None:
                supplier_details_instance.open_bal_date = input.open_bal_date

            if supplier_details_instance.pay_recurring is not None:
                supplier_details_instance.pay_recurring = input.pay_recurring
            
            if supplier_details_instance.is_contractor is not None:
                supplier_details_instance.is_contractor = input.is_contractor

            if supplier_details_instance.send_invitation is not None:
                supplier_details_instance.send_invitation = input.send_invitation

            if supplier_details_instance.notes is not None:
                supplier_details_instance.notes = input.notes

            if supplier_details_instance.pay_term is not None:
                supplier_details_instance.pay_term = pay_term

            if supplier_details_instance.currency is not None:
                supplier_details_instance.currency = currency

            if supplier_details_instance.supplier is not None:
                supplier_details_instance.supplier = supplier

            supplier_details_instance.save()

            return UpdateSupplierDetails(supplier_details=supplier_details_instance)

class DeleteSupplierDetails(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)

  supplier_details = graphene.Field(SupplierDetailsType)
  
  def mutate(self, info, id):
      supplier_details_instance = SupplierDetails.objects.get(pk=id)
      supplier_details_instance.delete()

      return DeleteSupplierDetails(supplier_details=None)


class CreateClientDetails(graphene.Mutation):
  class Arguments:
    input = ClientDetailsInput(required=True)

  client_details = graphene.Field(ClientDetailsType)

  def mutate(self, info, input=None):
    pay_term = input.get("pay_term")
    pay_term = PaymentTerms.objects.get(pk=pay_term)
    currency = input.get("currency")
    currency = Currency.objects.get(pk=currency)
    client= input.get("client")
    client = Clients.objects.get(pk=client)
    payment_method = input.get("payment_method")
    payment_method = PaymentMethods.objects.get(pk=payment_menthod)

    client_details_instance = ClientDetails(bank_acc_no=input.bank_acc_no, opening_balance=input.opening_balance, open_bal_date=input.open_bal_date, pay_recurring=input.pay_recurring, late_fees=input.late_fees, pay_reminder=input.pay_reminder, tax_exemption=input.tax_exemption, send_invitation=input.send_invitation, notes=input.notes)

    client_details_instance.pay_term = pay_term
    client_details_instance.currency = currency
    client_details_instance.client = client
    client_details_instance.payment_method = payment_method

    client_details_instance.save()
    return CreateClientDetails(client_details=client_details_instance)

class DeleteClientDetails(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)

  client_details = graphene.Field(ClientDetailsType)
  
  def mutate(self, info, id):
      client_details_instance = ClientDetails.objects.get(pk=id)
      client_details_instance.delete()

      return DeleteClientDetials(client_details=None)

class UpdateClientDetails(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = ClientDetailsInput(required=True)
    
    client_details = graphene.Field(ClientDetailsType)

    def mutate(self, info, id, input=None):
        client_details_instance = ClientDetails.objects.get(pk=id)
        pay_term = input.get("pay_term")
        pay_term = PaymentTerms.objects.get(pk=pay_term)
        currency = input.get("currency")
        currency = Currency.objects.get(pk=currency)
        client= input.get("client")
        client = Clients.objects.get(pk=client)
        payment_method = input.get("payment_method")
        payment_method = PaymentMethods.objects.get(pk=payment_method)

        if client_details_instance:

            if client_details_instance.bank_acc_no is not None:
                client_details_instance.bank_acc_no = input.bank_acc_no

            if client_details_instance.opening_balance is not None:
                client_details_instance.opening_balance = input.opening_balance

            if client_details_instance.open_bal_date is not None:
                client_details_instance.open_bal_date = input.open_bal_date

            if client_details_instance.pay_recurring is not None:
                client_details_instance.pay_recurring = input.pay_recurring
            
            if client_details_instance.late_fees is not None:
                client_details_instance.late_fees = input.late_fees

            if client_details_instance.pay_reminder is not None:
                client_details_instance.pay_reminder = input.pay_reminder

            if client_details_instance.tax_exemption is not None:
                client_details_instance.tax_exemption = input.tax_exemption
            
            if client_details_instance.send_invitation is not None:
                client_details_instance.send_invitation = input.send_invitation

            if client_details_instance.notes is not None:
                client_details_instance.notes = input.notes

            if client_details_instance.pay_term is not None:
                client_details_instance.pay_term = pay_term

            if client_details_instance.currency is not None:
                client_details_instance.currency = currency

            if client_details_instance.client is not None:
                client_details_instance.client = client
            
            if client_details_instance.payment_method is not None:
                client_details_instance.payment_method = payment_method

            client_details_instance.save()

            return UpdateClientDetails(client_details=client_details_instance)



class CreateItemType(graphene.Mutation):
  class Arguments:
    input = ItemTypeInput(required=True)
    
  item_type = graphene.Field(ItemtypeType)

  def mutate(self, info, input=None):
    item_type_instance = ItemType(name=input.name, notes=input.notes)
    item_type_instance.save()
    return CreateItemType(item_type=item_type_instance)

class UpdateItemType(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = ItemTypeInput(required=True)
    
    item_type = graphene.Field(ItemtypeType)

    def mutate(self, info, id, input=None):
        item_type_instance = ItemType.objects.get(pk=id)

        if item_type_instance:
            if item_type_instance.name is not None:
                item_type_instance.name = input.name

            if item_type_instance.notes is not None:
                item_type_instance.notes = input.notes

            item_type_instance.save()

            return UpdateItemType(item_type=item_type_instance)

class DeleteItemType(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)

  item_type = graphene.Field(ItemtypeType)
  
  def mutate(self, info, id):
    item_type_instance = ItemType.objects.get(pk=id)

    item_type_instance.delete()

    return DeleteItemType(item_type=None)


class CreateItemCategory(graphene.Mutation):
  class Arguments:
    input = ItemCategoryInput(required=True)
    
  item_category = graphene.Field(ItemCategoryType)

  def mutate(self, info, input=None):
    item_category_instance = ItemCategory(name=input.name, notes=input.notes)
    item_category_instance.save()
    return CreateItemCategory(item_category=item_category_instance)

class UpdateItemCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = ItemCategoryInput(required=True)
    
    item_category = graphene.Field(ItemCategoryType)

    def mutate(self, info, id, input=None):
        item_category_instance = ItemCategory.objects.get(pk=id)

        if item_category_instance:
            if item_category_instance.name is not None:
                item_category_instance.name = input.name

            if item_category_instance.notes is not None:
                item_category_instance.notes = input.notes

            item_category_instance.save()

            return UpdateItemCategory(item_category=item_category_instance)

class DeleteItemCategory(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)

  item_category = graphene.Field(ItemCategoryType)
  
  def mutate(self, info, id):
    item_category_instance = ItemCategory.objects.get(pk=id)

    item_category_instance.delete()

    return DeleteItemCategory(item_category=None)


class CreateItemBrands(graphene.Mutation):
  class Arguments:
    input = ItemBrandsInput(required=True)
    
  item_brands= graphene.Field(ItemBrandsType)

  def mutate(self, info, input=None):
    item_brands_instance = ItemBrands(is_active=input.is_active, name=input.name, notes=input.notes)
    item_brands_instance.save()
    return CreateItemBrands(item_brands=item_brands_instance)

class UpdateItemBrands(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = ItemBrandsInput(required=True)
    
    item_brands = graphene.Field(ItemBrandsType)

    def mutate(self, info, id, input=None):
        item_brands_instance = ItemBrands.objects.get(pk=id)

        if item_brands_instance:
            if item_brands_instance.name is not None:
                item_brands_instance.name = input.name

            if item_brands_instance.notes is not None:
                item_brands_instance.notes = input.notes

            item_brands_instance.save()

            return UpdateItemBrands(item_brands=item_brands_instance)

class DeleteItemBrands(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)

  item_brands = graphene.Field(ItemBrandsType)
  
  def mutate(self, info, id):
    item_brands_instance = ItemBrands.objects.get(pk=id)

    item_brands_instance.delete()

    return DeleteItemBrands(item_brands=None)

# APB-10
class CreateItems(graphene.Mutation):
  class Arguments:
    input = ItemsInput(required=True)
  
  items = graphene.Field(ItemsType)

  def mutate(self, info, input=None):
    item_type = input.get("item_type")
    print(item_type)
    item_type = ItemType.objects.get(pk=item_type)
    item_category = input.get("item_category")
    item_category = ItemCategory.objects.get(pk=item_category)
    supplier= input.get("supplier")
    supplier = Supplier.objects.get(pk=supplier)
    item_brand = input.get("item_brand")
    item_brand = ItemBrands.objects.get(pk=item_brand)
    account_name = input.get("account_name")
    account_name = AccountName.objects.get(pk=account_name)

    items_instance = Items(is_active=input.is_active, name=input.name, description=input.description,SKU= input.SKU, purchase_price=input.purchase_price, sales_price=input.sales_price, markup_price=input.markup_price, min_sales_price=input.min_sales_price, weight_param=input.weight_param, weight_values=input.weight_values, volume_cbm=input.volume_cbm, upc_no=input.upc_no, mpn_no=input.mpn_no, ean_no=input.ean_no, isbn_no=input.isbn_no,item_barcode=input.item_barcode, warranty_month=input.warranty_month,stock_in_hand=input.stock_in_hand, initial_stock_entry=input.initial_stock_entry, reorder_point=input.reorder_point, max_stock_no=input.max_stock_no, lead_time_days=input.lead_time_days, allow_sales_commision=input.allow_sales_commision, commission_per_item=input.commission_per_item, commission_percentage=input.commission_percentage, tags=input.tags)

    items_instance.item_type = item_type
    items_instance.item_category = item_category
    items_instance.supplier = supplier
    items_instance.item_brand = item_brand
    items_instance.account_name = account_name

    items_instance.save()
    return CreateItems(items=items_instance)

class UpdateItems(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)
    input = ItemsInput(required=True)
  
  items = graphene.Field(ItemsType)

  def mutate(self, info, id, input=None):
      items_instance = Items.objects.get(pk=id)
      item_type = input.get("item_type")
      item_type = ItemType.objects.get(pk=item_type)
      item_category = input.get("item_category")
      item_category = ItemCategory.objects.get(pk=item_category)
      supplier= input.get("supplier")
      supplier = Supplier.objects.get(pk=supplier)
      item_brand = input.get("item_brand")
      item_brand = ItemBrands.objects.get(pk=item_brand)
      account_name = input.get("account_name")
      account_name = AccountName.objects.get(pk=account_name)

      if items_instance:

          if items_instance.is_active is not None:
              items_instance.is_active = input.is_active

          if items_instance.name is not None:
              items_instance.name = input.name

          if items_instance.description is not None:
              items_instance.description = input.description

          if items_instance.SKU is not None:
              items_instance.SKU = input.SKU
          
          if items_instance.purchase_price is not None:
              items_instance.purchase_price = input.purchase_price

          if items_instance.sales_price is not None:
              items_instance.sales_price = input.sales_price

          if items_instance.markup_price is not None:
              items_instance.markup_price = input.markup_price
          
          if items_instance.min_sales_price is not None:
              items_instance.min_sales_price = input.min_sales_price

          if items_instance.weight_param is not None:
              items_instance.weight_param = input.weight_param

          if items_instance.volume_cbm is not None:
              items_instance.volume_cbm = input.volume_cbm

          if items_instance.upc_no is not None:
              items_instance.upc_no = input.upc_no

          if items_instance.mpn_no is not None:
              items_instance.mpn_no = input.mpn_no

          if items_instance.ean_no is not None:
              items_instance.ean_no = input.ean_no

          if items_instance.isbn_no is not None:
              items_instance.isbn_no = input.isbn_no

          if items_instance.item_barcode is not None:
              items_instance.item_barcode = input.item_barcode

          if items_instance.warranty_month is not None:
              items_instance.warranty_month = input.warranty_month

          if items_instance.stock_in_hand is not None:
              items_instance.stock_in_hand = input.stock_in_hand
          
          if items_instance.initial_stock_entry is not None:
              items_instance.initial_stock_entry = input.initial_stock_entry
          
          if items_instance.max_stock_no is not None:
              items_instance.max_stock_no = input.max_stock_no
          
          if items_instance.lead_time_days is not None:
              items_instance.lead_time_days = input.lead_time_days
          
          if items_instance.allow_sales_commision is not None:
              items_instance.allow_sales_commision = input.allow_sales_commision
          
          if items_instance.commission_per_item is not None:
              items_instance.commission_per_item = input.commission_per_item
          
          if items_instance.commission_percentage is not None:
              items_instance.commission_percentage = input.commission_percentage
          
          if items_instance.commission_percentage is not None:
              items_instance.commission_percentage = input.commission_percentage
          
          if items_instance.tags is not None:
              items_instance.tags = input.tags

          if items_instance.item_type is not None:
                items_instance.item_type = item_type

          if items_instance.item_category is not None:
                items_instance.item_category = item_category

          if items_instance.supplier is not None:
                items_instance.supplier = supplier

          if items_instance.item_brand is not None:
                items_instance.item_brand = item_brand
          
          if items_instance.account_name is not None:
                items_instance.account_name = account_name

          items_instance.save()

          return UpdateItems(items=items_instance)

class DeleteItems(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)

  items = graphene.Field(ItemsType)
  
  def mutate(self, info, id):
    items_instance = Items.objects.get(pk=id)

    items_instance.delete()

    return DeleteItems(items=None)


class CreateItemGroup(graphene.Mutation):
  class Arguments:
    input = ItemGroupInput(required=True)
  
  item_group = graphene.Field(ItemsGroupType)
  def mutate(self, info, input=None):
    item_type = input.get("item_type")
    print(item_type)
    item_type = ItemType.objects.get(pk=item_type)
    supplier= input.get("supplier")
    supplier = Supplier.objects.get(pk=supplier)
    item_brand = input.get("item_brand")
    item_brand = ItemBrands.objects.get(pk=item_brand)
    account_name = input.get("account_name")
    account_name = AccountName.objects.get(pk=account_name)

    items_group_instance = ItemsGroup(is_active=input.is_active, name=input.name, description=input.description,SKU= input.SKU, volume_cbm=input.volume_cbm, upc_no=input.upc_no, warranty_month=input.warranty_month,tags=input.tags, item_barcode=input.item_barcode)

    items_group_instance.item_type = item_type
    items_group_instance.supplier = supplier
    items_group_instance.item_brand = item_brand
    items_group_instance.account_name = account_name

    items_group_instance.save()
    return CreateItemGroup(item_group=items_group_instance)

class UpdateItemGroup(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)
    input = ItemGroupInput(required=True)
  
  item_group = graphene.Field(ItemsGroupType)

  def mutate(self, info, id, input=None):
      items_group_instance = ItemsGroup.objects.get(pk=id)
      item_type = input.get("item_type")
      item_type = ItemType.objects.get(pk=item_type)
      supplier= input.get("supplier")
      supplier = Supplier.objects.get(pk=supplier)
      item_brand = input.get("item_brand")
      item_brand = ItemBrands.objects.get(pk=item_brand)
      account_name = input.get("account_name")
      account_name = AccountName.objects.get(pk=account_name)

      if items_group_instance:

          if items_group_instance.is_active is not None:
              items_group_instance.is_active = input.is_active

          if items_group_instance.name is not None:
              items_group_instance.name = input.name

          if items_group_instance.description is not None:
              items_group_instance.description = input.description

          if items_group_instance.SKU is not None:
              items_group_instance.SKU = input.SKU
          
          if items_group_instance.volume_cbm is not None:
              items_group_instance.volume_cbm = input.volume_cbm

          if items_group_instance.upc_no is not None:
              items_group_instance.upc_no = input.upc_no

          if items_group_instance.item_barcode is not None:
              items_group_instance.item_barcode = input.item_barcode

          if items_group_instance.warranty_month is not None:
              items_group_instance.warranty_month = input.warranty_month

          if items_group_instance.tags is not None:
              items_group_instance.tags = input.tags

          if items_group_instance.item_type is not None:
                items_group_instance.item_type = item_type

          if items_group_instance.supplier is not None:
                items_group_instance.supplier = supplier

          if items_group_instance.item_brand is not None:
                items_group_instance.item_brand = item_brand
          
          if items_group_instance.account_name is not None:
                items_group_instance.account_name = account_name

          items_group_instance.save()

          return UpdateItemGroup(item_group=items_group_instance)

class DeleteItemGroup(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)

  item_group = graphene.Field(ItemsGroupType)
  
  def mutate(self, info, id):
    items_group_instance  = ItemsGroup.objects.get(pk=id)

    items_group_instance.delete()

    return DeleteItemGroup(item_group=None)


class CreateGroupMapping(graphene.Mutation):
  class Arguments:
    data = ItemGroupMappingInput(required=True)
  
  item_group_mapping = graphene.List(ItemGroupMappingType)
  def mutate(self, info, data):
    item_groups = data.get("item_groups")
    items = data.get("items")
    quantity = data.get("mapping_quantity")

    item_mapping_ins_list = []
    item_group_ins = ItemsGroup.objects.create(**prepare_model_data_from_dict(ItemsGroup, item_groups))  
    for item in items:
      item = prepare_model_data_from_dict(Items, item)
      item_ins = Items.objects.create(**item)
      # item_ins_list.append(item_ins)
      item_mapping_ins_list.append(ItemGroupMapping.objects.create(item_group=item_group_ins, item = item_ins, quantity=quantity))

    return CreateGroupMapping(item_group_mapping=item_mapping_ins_list)

    
class DeleteGroupMapping(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)

  item_group_mapping = graphene.List(ItemGroupMappingType)
  def mutate(self, info, id):
    item_group_mapping_instance  = ItemGroupMapping.objects.get(pk=id)

    item_group_mapping_instance.delete()

    return DeleteGroupMapping(item_group_mapping=None)


class UpdateGroupMapping(graphene.Mutation):
  class Arguments:
    data = ItemGroupMappingUpdateInput()
  
  items_group_mapping = graphene.Field(ItemGroupMappingType)
  def mutate(self, info, data):
    id = data.get("id")
    item_groups = data.get("item_groups")
    items = data.get("items")

    items_group_mapping_instance = ItemGroupMapping.objects.get(pk=id)
    
    if item_groups is not None:
      item_group_instance = ItemsGroup.objects.get(pk=item_groups)
      if item_group_instance is None:
        raise GraphQLError("ItemGroup ID not found")

    if items is not None:
      items_instance = Items.objects.get(pk=items)
      if items_instance is None:
        raise GraphQLError("Item ID not found")

    if items_group_mapping_instance:
      if items_group_mapping_instance.item_group is not None:
          items_group_mapping_instance.item_group = item_group_instance

      if items_group_mapping_instance.item is not None:
          items_group_mapping_instance.item = items_instance

      if items_group_mapping_instance.quantity is not None:
          items_group_mapping_instance.quantity = data.get("mapping_quantity")

      items_group_mapping_instance.save()

      return UpdateGroupMapping(items_group_mapping=items_group_mapping_instance)


class CreateInventoryAdjustment(graphene.Mutation):
  class Arguments:
    input = InventoryAdjustmentInput(required=True)

  inventory_adjustment = graphene.Field(InventoryAdjustmentType)

  def mutate(self, info, input=None):
    acc_name= input.get("acc_name")
    acc_name = AccountName.objects.get(pk=acc_name)

    inventory_adjustment_instance = InventoryAdjustment(is_active=input.is_active, time_log=input.time_log, adjustment_reference_no=input.adjustment_reference_no,cause_of_action= input.cause_of_action, comments=input.comments)

    inventory_adjustment_instance.acc_name = acc_name

    inventory_adjustment_instance.save()
    return CreateInventoryAdjustment(inventory_adjustment=inventory_adjustment_instance)

class UpdateInventoryAdjustment(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)
    input = InventoryAdjustmentInput(required=True)
  
  inventory_adjustment = graphene.Field(InventoryAdjustmentType)

  def mutate(self, info, id, input=None):
    inventory_adjustment_instance = InventoryAdjustment.objects.get(pk=id)
    acc_name= input.get("acc_name")
    acc_name = AccountName.objects.get(pk=acc_name)
    
    if inventory_adjustment_instance:

        if inventory_adjustment_instance.is_active is not None:
            inventory_adjustment_instance.is_active = input.is_active

        if inventory_adjustment_instance.time_log is not None:
            inventory_adjustment_instance.time_log = input.time_log

        if inventory_adjustment_instance.adjustment_reference_no is not None:
            inventory_adjustment_instance.adjustment_reference_no = input.adjustment_reference_no

        if inventory_adjustment_instance.comments is not None:
            inventory_adjustment_instance.comments = input.comments

        if inventory_adjustment_instance.acc_name is not None:
              inventory_adjustment_instance.acc_name = acc_name

        inventory_adjustment_instance.save()

        return UpdateInventoryAdjustment(inventory_adjustment=inventory_adjustment_instance)

class DeleteInventoryAdjustment(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)

  inventory_adjustment = graphene.Field(InventoryAdjustmentType)
  
  def mutate(self, info, id):
    inventory_adjustment_instance  = InventoryAdjustment.objects.get(pk=id)

    inventory_adjustment_instance.delete()

    return DeleteInventoryAdjustment(inventory_adjustment=None)

class CreateInventoryAdjustmentItems(graphene.Mutation):
  class Arguments:
    input = InventoryAdjustmentItemsInput(required=True)

  inventory_adjustment_items = graphene.Field(InventoryAdjustmentItemsType)

  def mutate(self, info, input=None):
    inventory_adjustment = input.get("inventory_adjustment")
    inventory_adjustment = InventoryAdjustment.objects.get(pk=inventory_adjustment)
    item = input.get("item")
    item = Items.objects.get(pk=item)

    inventory_adjustment_items_instance = InventoryAdjustmentItems(quantity_or_value=input.quantity_or_value, value=input.value)

    inventory_adjustment_items_instance.inventory_adjustment = inventory_adjustment
    inventory_adjustment_items_instance.item = item

    inventory_adjustment_items_instance.save()
    return CreateInventoryAdjustmentItems(inventory_adjustment_items=inventory_adjustment_items_instance)

class UpdateInventoryAdjustmentItems(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)
    input = InventoryAdjustmentItemsInput(required=True)

  inventory_adjustment_items = graphene.Field(InventoryAdjustmentItemsType)

  def mutate(self, info, id, input=None):
    inventory_adjustment_items_instance = InventoryAdjustmentItems.objects.get(pk=id)
    inventory_adjustment = input.get("inventory_adjustment")
    inventory_adjustment = InventoryAdjustment.objects.get(pk=inventory_adjustment)
    item = input.get("item")
    item = Items.objects.get(pk=item)

    if inventory_adjustment_items_instance:
      if inventory_adjustment_items_instance.quantity_or_value is not None:
        inventory_adjustment_items_instance.quantity_or_value = input.quantity_or_value

      if inventory_adjustment_items_instance.value is not None:
        inventory_adjustment_items_instance.value = input.value

      if inventory_adjustment_items_instance.inventory_adjustment is not None:
        inventory_adjustment_items_instance.inventory_adjustment = inventory_adjustment
        
      if inventory_adjustment_items_instance.item is not None:
        inventory_adjustment_items_instance.item = item

      inventory_adjustment_items_instance.save()

      return UpdateInventoryAdjustmentItems(inventory_adjustment_items=inventory_adjustment_items_instance)

class DeleteInventoryAdjustmentItems(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)

  inventory_adjustment_items = graphene.Field(InventoryAdjustmentItemsType)

  def mutate(self, info, id):
    inventory_adjustment_items_instance  = InventoryAdjustmentItems.objects.get(pk=id)

    inventory_adjustment_items_instance.delete()

    return DeleteInventoryAdjustmentItems(inventory_adjustment_items=None)

class CreateStorageLocation(graphene.Mutation):
  class Arguments:
    input = StorageLocationInput(required=True)

  storage_location = graphene.Field(StorageLocationType)

  def mutate(self, info, input=None):
    country = input.get("country")
    country = Country.objects.get(pk=country)
    storage_location_instance = StorageLocation(is_active=input.is_active, name=input.name, address=input.address, state= input.state, city=input.city, zipcode=input.zipcode, notes=input.notes)

    storage_location_instance.country = country

    storage_location_instance.save()
    return CreateStorageLocation(storage_location=storage_location_instance)
  
class UpdateStorageLocation(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)
    input = StorageLocationInput(required=True)

  storage_location = graphene.Field(StorageLocationType)

  def mutate(self, info, id, input=None):
    storage_location_instance = StorageLocation.objects.get(pk=id)
    country = input.get("country")
    country = Country.objects.get(pk=country)

    if storage_location_instance:
      if storage_location_instance.is_active is not None:
        storage_location_instance.is_active = input.is_active

      if storage_location_instance.name is not None:
        storage_location_instance.name = input.name

      if storage_location_instance.address is not None:
        storage_location_instance.address = input.address
      
      if storage_location_instance.state is not None:
        storage_location_instance.state = input.state
      
      if storage_location_instance.city is not None:
        storage_location_instance.city = input.city
      
      if storage_location_instance.zipcode is not None:
        storage_location_instance.zipcode = input.zipcode
      
      if storage_location_instance.notes is not None:
        storage_location_instance.notes = input.notes
        
      if storage_location_instance.country is not None:
        storage_location_instance.country = country

      storage_location_instance.save()

      return UpdateStorageLocation(storage_location=storage_location_instance)

class DeleteStorageLocation(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)

  storage_location = graphene.Field(StorageLocationType)

  def mutate(self, info, id):
    storage_location_instance  = StorageLocation.objects.get(pk=id)

    storage_location_instance.delete()

    return DeleteStorageLocation(storage_location=None)

class CreateItemStorage(graphene.Mutation):
  class Arguments:
    input = ItemStorageInput(required=True)

  item_storage = graphene.Field(ItemStorageType)

  def mutate(self, info, input=None):
    storage_location = input.get("storage_location")
    storage_location = StorageLocation.objects.get(pk=storage_location)
    item_storage_instance = ItemStorage(is_active=input.is_active, lot_number=input.lot_number, barcode=input.barcode, notes= input.notes)

    item_storage_instance.storage_location = storage_location

    item_storage_instance.save()
    return CreateItemStorage(item_storage=item_storage_instance)

class UpdateItemStorage(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)
    input = ItemStorageInput(required=True)

  item_storage = graphene.Field(ItemStorageType)

  def mutate(self, info, id, input=None):
    item_storage_instance = ItemStorage.objects.get(pk=id)
    storage_location = input.get("storage_location")
    storage_location = StorageLocation.objects.get(pk=storage_location)

    if item_storage_instance:
      if item_storage_instance.is_active is not None:
        item_storage_instance.is_active = input.is_active

      if item_storage_instance.lot_number is not None:
        item_storage_instance.lot_number = input.lot_number

      if item_storage_instance.barcode is not None:
        item_storage_instance.barcode = input.barcode
      
      if item_storage_instance.notes is not None:
        item_storage_instance.notes = input.notes
        
      if item_storage_instance.storage_location is not None:
        item_storage_instance.storage_location = storage_location

      item_storage_instance.save()

      return UpdateItemStorage(item_storage=item_storage_instance)

class DeleteItemStorage(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)

  item_storage = graphene.Field(ItemStorageType)

  def mutate(self, info, id):
    item_storage_instance  = ItemStorage.objects.get(pk=id)

    item_storage_instance.delete()

    return DeleteItemStorage(item_storage=None)


class CreateItemStorageMapping(graphene.Mutation):
  class Arguments:
    data = ItemStorageMappingInput(required=True)
  
  item_storage_mapping = graphene.List(ItemStorageMappingType)
  def mutate(self, info, data):
    quantity = data.get("quantity")
    volume = data.get("volume")
    item_storage = data.get("item_storage")
    items = data.get("items")

    item_storage_mapping_ins_list = []
    item_storage_ins = ItemStorage.objects.create(**prepare_model_data_from_dict(ItemStorage, item_storage))  
    for item in items:
      item = prepare_model_data_from_dict(Items, item)
      item_ins = Items.objects.create(**item)
      item_storage_mapping_ins_list.append(ItemStorageMapping.objects.create(quantity=quantity, volume=volume, item_storage=item_storage_ins, item = item_ins))

    return CreateItemStorageMapping(item_storage_mapping=item_storage_mapping_ins_list)

    
class DeleteItemStorageMapping(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)

  item_storage_mapping = graphene.List(ItemStorageMappingType)
  def mutate(self, info, id):
    item_storage_mapping_instance  = ItemStorageMapping.objects.get(pk=id)

    item_storage_mapping_instance.delete()

    return DeleteItemStorageMapping(item_storage_mapping=None)


class UpdateItemStorageMapping(graphene.Mutation):
  class Arguments:
    data = ItemStorageMappingUpdateInput(required=True)
  
  item_storage_mapping = graphene.Field(ItemStorageMappingType)
  def mutate(self, info, data):
    id = data.get("id")
    item_storage = data.get("item_storage")
    items = data.get("items")

    item_storage_mapping_instance = ItemStorageMapping.objects.get(pk=id)
    
    if item_storage is not None:
      item_storage_instance = ItemStorage.objects.get(pk=item_storage)
      if item_storage_instance is None:
        raise GraphQLError("Item Storage ID not found")

    if items is not None:
      items_instance = Items.objects.get(pk=items)
      if items_instance is None:
        raise GraphQLError("Item ID not found")

    if item_storage_mapping_instance:
      if item_storage_mapping_instance.item_storage is not None:
          item_storage_mapping_instance.item_storage = item_storage_instance

      if item_storage_mapping_instance.item is not None:
          item_storage_mapping_instance.item = items_instance

      if item_storage_mapping_instance.quantity is not None:
          item_storage_mapping_instance.quantity = data.get("quantity")

      if item_storage_mapping_instance.volume is not None:
          item_storage_mapping_instance.volume = data.get("volume")

      item_storage_mapping_instance.save()

      return UpdateItemStorageMapping(item_storage_mapping=item_storage_mapping_instance)


class CreateItemTransfer(graphene.Mutation):
  class Arguments:
    input = ItemTransferInput(required=True)

  item_transfer = graphene.Field(ItemTransferType)

  def mutate(self, info, input=None):
    from_storage_location = input.get("from_storage_location")
    from_storage_location = StorageLocation.objects.get(pk=from_storage_location)
    to_storage_location = input.get("to_storage_location")
    to_storage_location = StorageLocation.objects.get(pk=to_storage_location)
    shopping_carrier = input.get("shopping_carrier")
    shopping_carrier = Supplier.objects.get(pk=shopping_carrier)
    item_transfer_instance = ItemTransfer(is_active=input.is_active, time_log=input.time_log, reference_no=input.reference_no, shipping_method= input.shipping_method, shipment_tracking_no=input.shipment_tracking_no, shipment_cost=input.shipment_cost, bilable=input.bilable, notes= input.notes)

    item_transfer_instance.from_storage_location = from_storage_location
    item_transfer_instance.to_storage_location = to_storage_location
    item_transfer_instance.shopping_carrier = shopping_carrier

    item_transfer_instance.save()
    return CreateItemTransfer(item_transfer=item_transfer_instance)

class UpdateItemTransfer(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)
    input = ItemTransferInput(required=True)

  item_transfer = graphene.Field(ItemTransferType)

  def mutate(self, info, id, input=None):
    item_transfer_instance = ItemTransfer.objects.get(pk=id)
    from_storage_location = input.get("from_storage_location")
    from_storage_location = StorageLocation.objects.get(pk=from_storage_location)
    to_storage_location = input.get("to_storage_location")
    to_storage_location = StorageLocation.objects.get(pk=to_storage_location)
    shopping_carrier = input.get("shopping_carrier")
    shopping_carrier = Supplier.objects.get(pk=shopping_carrier)

    if item_transfer_instance:
      if item_transfer_instance.is_active is not None:
        item_transfer_instance.is_active = input.is_active

      if item_transfer_instance.time_log is not None:
        item_transfer_instance.time_log = input.time_log

      if item_transfer_instance.reference_no is not None:
        item_transfer_instance.reference_no = input.reference_no
      
      if item_transfer_instance.shipping_method is not None:
        item_transfer_instance.shipping_method = input.shipping_method
      
      if item_transfer_instance.shipment_tracking_no is not None:
        item_transfer_instance.shipment_tracking_no = input.shipment_tracking_no
      
      if item_transfer_instance.shipment_cost is not None:
        item_transfer_instance.shipment_cost = input.shipment_cost
      
      if item_transfer_instance.bilable is not None:
        item_transfer_instance.bilable = input.bilable
      
      if item_transfer_instance.notes is not None:
        item_transfer_instance.notes = input.notes
        
      if item_transfer_instance.from_storage_location is not None:
        item_transfer_instance.from_storage_location = from_storage_location
      
      if item_transfer_instance.to_storage_location is not None:
        item_transfer_instance.to_storage_location = to_storage_location
      
      if item_transfer_instance.shopping_carrier is not None:
        item_transfer_instance.shopping_carrier = shopping_carrier

      item_transfer_instance.save()

      return UpdateItemTransfer(item_transfer=item_transfer_instance)

class DeleteItemTransfer(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)

  item_transfer = graphene.Field(ItemTransferType)

  def mutate(self, info, id):
    item_transfer_instance  = ItemTransfer.objects.get(pk=id)

    item_transfer_instance.delete()

    return DeleteItemTransfer(item_transfer=None)


class CreateItemTransferMapping(graphene.Mutation):
  class Arguments:
    data = ItemTransferMappingInput(required=True)
  
  item_transfer_mapping = graphene.List(ItemTransferMappingType)
  def mutate(self, info, data):
    quantity = data.get("quantity")
    volume = data.get("volume")
    item_transfer = data.get("item_transfer")
    items = data.get("items")

    item_transfer_mapping_ins_list = []
    item_transfer_ins = ItemTransfer.objects.create(**prepare_model_data_from_dict(ItemTransfer, item_transfer))  
    for item in items:
      item = prepare_model_data_from_dict(Items, item)
      item_ins = Items.objects.create(**item)
      item_transfer_mapping_ins_list.append(ItemTransferMapping.objects.create(quantity=quantity, volume=volume, item_transfer=item_transfer_ins, item = item_ins))

    return CreateItemTransferMapping(item_transfer_mapping=item_transfer_mapping_ins_list)


class DeleteItemTransferMapping(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)

  item_transfer_mapping = graphene.List(ItemTransferMappingType)
  def mutate(self, info, id):
    item_transfer_mapping_instance  = ItemTransferMapping.objects.get(pk=id)

    item_transfer_mapping_instance.delete()

    return DeleteItemTransferMapping(item_transfer_mapping=None)


class UpdateItemTransferMapping(graphene.Mutation):
  class Arguments:
    data = ItemTransferMappingUpdateInput(required=True)

  item_transfer_mapping = graphene.Field(ItemTransferMappingType)

  def mutate(self, info, data):
    id = data.get("id")
    item_transfer = data.get("item_transfer")
    items = data.get("items")
  
    item_transfer_mapping_instance = ItemTransferMapping.objects.get(pk=id)

    if item_transfer is not None:
      item_transfer_instance = ItemTransfer.objects.get(pk=item_transfer)
      if item_transfer_instance is None:
        raise GraphQLError("Item Transfer ID not found")
      
    if items is not None:
      items_instance = Items.objects.get(pk=items)
      if items_instance is None:
        raise GraphQLError("Item ID not found")
    
    if item_transfer_mapping_instance:
      if item_transfer_mapping_instance.item_transfer is not None:
          item_transfer_mapping_instance.item_transfer = item_transfer_instance

      if item_transfer_mapping_instance.item is not None:
          item_transfer_mapping_instance.item = items_instance

      if item_transfer_mapping_instance.quantity is not None:
          item_transfer_mapping_instance.quantity = data.get("quantity")

      if item_transfer_mapping_instance.volume is not None:
          item_transfer_mapping_instance.volume = data.get("volume")
      
      item_transfer_mapping_instance.save()

      return UpdateItemTransferMapping(item_transfer_mapping=item_transfer_mapping_instance)


class Mutation:
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
  
    verify_token = graphql_jwt.Verify.Field()

    create_supplier = CreateSupplier.Field()
    update_supplier = UpdateSupplier.Field()
    delete_supplier = DeleteSupplier.Field()

    create_supplier_additional_contacts = Create_Supplier_Additional_Contacts.Field()
    update_supplier_additional_contacts = Update_Supplier_Additional_Contacts.Field()
    delete_supplier_additional_contacts = Delete_Supplier_Additional_Contacts.Field()

    create_supplier_address = CreateSupplierAddress.Field()
    update_supplier_address = UpdateSupplierAddress.Field()
    delete_supplier_address = DeleteSupplierAddress.Field()
    
    create_client = CreateClient.Field()
    update_client = UpdateClient.Field()
    delete_client = DeleteClient.Field()

    create_client_additional_contacts = Create_Client_Additional_Contacts.Field()
    update_client_additional_contacts = Update_Client_Additional_Contacts.Field()
    delete_client_additional_contacts = Delete_Client_Additional_Contacts.Field()

    create_client_address = CreateClientAddress.Field()
    update_client_address = UpdateClientAddress.Field()
    delete_client_address = DeleteClientAddress.Field()

    create_payment_terms = CreatePaymentTerms.Field()
    delete_payment_terms = DeletePaymentTerms.Field()
    update_payment_terms = UpdatePaymentTerms.Field()

    create_supplier_details = CreateSupplierDetails.Field()
    update_supplier_details = UpdateSupplierDetails.Field()
    delete_supplier_details = DeleteSupplierDetails.Field()

    create_client_details = CreateClientDetails.Field()
    delete_client_details = DeleteClientDetails.Field()
    update_client_details = UpdateClientDetails.Field()

    create_item_types = CreateItemType.Field()
    delete_item_types = DeleteItemType.Field()
    update_item_types = UpdateItemType.Field()

    create_item_category = CreateItemCategory.Field()
    delete_item_category = DeleteItemCategory.Field()
    update_item_category = UpdateItemCategory.Field()

    create_item_brands = CreateItemBrands.Field()
    delete_item_brands = DeleteItemBrands.Field()
    update_item_brands = UpdateItemBrands.Field()

    create_item = CreateItems.Field()
    update_item = UpdateItems.Field()
    delete_item = DeleteItems.Field()
    

    create_item_group = CreateItemGroup.Field()
    update_item_group = UpdateItemGroup.Field()
    delete_item_group = DeleteItemGroup.Field()
   
    create_item_group_mapping = CreateGroupMapping.Field()
    delete_item_group_mapping = DeleteGroupMapping.Field()
    update_item_group_mapping = UpdateGroupMapping.Field()

    create_inventory_adjustment = CreateInventoryAdjustment.Field()
    update_inventory_adjustment = UpdateInventoryAdjustment.Field()
    delete_inventory_adjustment = DeleteInventoryAdjustment.Field()

    create_inventory_adjustment_items = CreateInventoryAdjustmentItems.Field()
    update_inventory_adjustment_items = UpdateInventoryAdjustmentItems.Field()
    delete_inventory_adjustment_items = DeleteInventoryAdjustmentItems.Field()

    create_storage_location = CreateStorageLocation.Field()
    update_storage_location = UpdateStorageLocation.Field()
    delete_storage_location = DeleteStorageLocation.Field()

    create_item_storage = CreateItemStorage.Field()
    update_item_storage = UpdateItemStorage.Field()
    delete_item_storage = DeleteItemStorage.Field()

    create_item_storage_mapping = CreateItemStorageMapping.Field()
    delete_item_storage_mapping = DeleteItemStorageMapping.Field()
    update_item_storage_mapping = UpdateItemStorageMapping.Field()
    
    create_item_transfer = CreateItemTransfer.Field()
    delete_item_transfer = DeleteItemTransfer.Field()
    update_item_transfer = UpdateItemTransfer.Field()
    
    create_item_transfer_mapping = CreateItemTransferMapping.Field()
    delete_item_transfer_mapping  = DeleteItemTransferMapping.Field()
    update_item_transfer_mapping  = UpdateItemTransferMapping.Field()

    

"""
#APB-1 & #APB-2

# Suppliers
query allSuppliers{
  suppliers{
    id
    companyName
    firstName
    lastName
    website
    displayName
    salutation
    isActive
    middleName
    emailAddress
    logo
    corporationNo
    supplierAdditionalContactsSet{
      id
      isActive
      firstName
      mobilePhone
      lastName
      middleName
      workPhone
      emailAddress
      salutation
      supplier{
        id
        companyName
      }
    }
  }
}

query singleSupplier{
  suppliers(companyName: "Bio Hazard Tech"){
    id
    companyName
    firstName
    lastName
    website
    displayName
    salutation
    isActive
    corporationNo
  }
}

query singleSuplierAddContacts{
  suppliers(companyName: "Bio Hazard Tech"){
    supplierAdditionalContactsSet{
      firstName
      middleName
      lastName
      mobilePhone
    }
  }
}

query allSuppliersAddContacs{
	supplierAdditionalContacts{
    firstName
    middleName
    lastName
    id
    mobilePhone
    supplier{
      id
      companyName
    }
  }
}

mutation supplierCreation{
  createSupplier(input: {
    companyName: "Argo Chemicalz Firm",
    firstName: "Argo",
    isActive: true,
    middleName: "Chemicals"
    lastName: "Firm",
    displayName: "ACF",
    website: "www.acf.com",
    salutation: "fca",
    emailAddress: "acf@acf.com.bd"
  })
  {
    supplier{
      id
    }
  }
}

mutation supplierUpdate{
  updateSupplier(id:5, input: {
  companyName: "Argo Chemicals Firm",
  isActive: true,
  firstName: "Argo",
  middleName: "Chemicals",
  lastName: "Firm",
	website: "www.argo.com",
  emailAddress: "argo@argo.com.bd"
  })
  {
    supplier{
      id
      companyName
      website
      emailAddress
    }
  }
}

mutation supplierDelete{
  deleteSupplier(id: 4){
    supplier{
      id
    }
  }
}

mutation additionalSupplierContactCreation{
  createSupplierAdditionalContacts(input:{
    isActive: true,
    firstName: "Tech",
    middleName: "Chemicals"
    lastName: "Production"
    designation: "hello",
    workPhone: "1111",
    emailAddress: "tech@tech.com.bd",
    salutation: "91k",
    mobilePhone: "1010",
    supplier:5
  })
  {
    supplierAdditionalContacts{
      id
      firstName
      lastName
    }
  }
}
mutation additionalSupplierContactUpdate{
  updateSupplierAdditionalContacts(id: 5, input:{
    isActive: true,
    firstName: "Neon",
    lastName: "Firm"
    mobilePhone: "3333",
    supplier:2
  })
  {
    supplierAdditionalContacts{
    id
    firstName
    lastName
    salutation
    isActive
    middleName
    emailAddress
		supplier{
      id
      companyName
    }
  }
  }
}


mutation additionalSupplierContactsDelete{
  deleteSupplierAdditionalContacts(id: 3){
   supplierAdditionalContacts{
      id
      firstName
      lastName
    }
  }
}

#APB-3
#Suppliers Address


query singleSupplierAddress{
  supplierAddress(id: 2){
    id
    careOfPerson
    isActive
    state
    zipcode
    supplier{
      companyName
    }
    branchAs
    officeNumber
    mobileNumber
    country{
      id
      name
    }
    addresstype
    streetAddress
    branchAs
    
  }
}

mutation supplierAddressCreate{
  createSupplierAddress(input:{
    isActive: true,
    branchAs: "second",
  	careOfPerson: "second_person",
  	streetAddress: "secondt_street",
  	state: "second",
  	zipcode: "888",
  	officeNumber: "123",
    mobileNumber: "654",
    faxNumber: "t7s",
    addresstype: 2,
    country:2
    supplier:3
  })
  {
    supplierAddress{
    id
    careOfPerson
    isActive
    state
    zipcode
    supplier{
      companyName
    }
    branchAs
    officeNumber
    mobileNumber
    country{
      id
      name
    }
    addresstype
    streetAddress
    branchAs
    
  }
  }
}


mutation supplierAddressUpdate{
  updateSupplierAddress(id: 1, input: {
    isActive: true,
    addresstype: 2,
    branchAs: "Hello", 
    state: "Dakota",
    careOfPerson: "Hello World",
    country:2
    supplier:2
    
  })
  {
    supplierAddress{
      id
      careOfPerson
      addresstype
      
    }
  }
}
# APB-4
#Clients
query allClients{
  clients{
    id
    isActive
		isCorporation
    companyName
    salutation
    firstName
    middleName
    lastName
    displayName
    photo
    website
    emailAddress
  }
}

mutation clientCreate{
  createClient(input: {
    isActive: true,
    isCorporation: true,
    companyName: "The second Client",
    salutation: "12j",
    firstName: "The",
    middleName: "Second",
    lastName: "Client",
    displayName: "Second Client",
    website: "secondClient.com",
    emailAddress: "second@second.com"
  })
  {
		client{
      companyName
      
    }
  }
}

mutation clientDelete{
  deleteClient(id:3){
    client{
      id
    }
  }
}


mutation clientUpdate{
  updateClient(id:2, input: {
  isActive: true,
  isCorporation: true,
	companyName: "Django Graphene Tech",
  firstName: "Django",
  middleName: "Graphene",
  lastName: "Tech",
  displayName: "Django Tech",
  website: "www.djangotech.com",
  emailAddress: "django@tech.com"
  })
	{
    client{
      companyName
    }
  }
}

# token
mutation AuthToken{
  tokenAuth(username: "nouros", password:
  "nouros01"){
    token
    payload
    refreshExpiresIn
  }
}

mutation VerifyToken{
  verifyToken(token:"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im5vdXJvcyIsImV4cCI6MTYwMzcyNTcxOCwib3JpZ0lhdCI6MTYwMzcyNTQxOH0.PVt0tJmnTpxhHyLgOyuN4oVuV4OIeM-5Gcjq18eWMgY"){
    payload
  }
}

#APB-5 
# Client Additional Contacts
query allClientAdditionalContacts{
  clientAdditionalContacts{
    id
    isActive
    salutation
    firstName
    middleName
    lastName
    designation
    workPhone
    mobilePhone
    emailAddress
    client{
      id
      companyName
    }
    
  }
}



mutation clientAdditionalContactsCreate{
  createClientAdditionalContacts(input:{
    isActive: true,
    salutation: "12k",
    firstName: "Angular",
    middleName: "Js",
    lastName: "Client",
    designation: "frontend",
    workPhone: "1938",
    mobilePhone: "1132",
    emailAddress: "angular@js.com",
    clientId:4
  })
  {
    clientAdditionalContacts{
      id
      firstName
      lastName
      
    }
  }
}

mutation ClientAdditionalContactsUpdate{
  updateClientAdditionalContacts(id: 2, input:{
    isActive: true,
    firstName: "Angular",
		designation: "frontend",
    workPhone: "9898",
    lastName: "Firm",
    mobilePhone: "3333",
    emailAddress: "angular@js.com"
    clientId:2
  })
  {
    clientAdditionalContacts{
    id
    firstName
    lastName
    salutation
    isActive
    middleName
    emailAddress
		clientId{
      id
      companyName
    }
  }
  }
}


mutation clientAdditionalContactsDelete{
  deleteClientAdditionalContacts(id: 3){
   clientAdditionalContacts{
      id
      firstName
      lastName
    }
  }
}

#APB-6
#Client Address
query singleClientAddress{
  clientAddress(id: 1){
    id
    careOfPerson
    isActive
    city
    state
    zipcode
    client{
      id
      companyName
    }
    branchAs
    officeNumber
    mobileNumber
    country{
      id
      name
    }
    addresstype
    streetAddress
    branchAs
    
  }
}

query allClientAddress{
  clientAddress{
    id
    careOfPerson
    isActive
    city
    state
    zipcode
    faxNumber
    client{
      id
      companyName
    }
    branchAs
    officeNumber
    mobileNumber
    country{
      id
      name
    }
    addresstype
    streetAddress
    branchAs
    
  }
}

mutation clientAddressCreate{
  createClientAddress(input:{
    isActive: true,
    branchAs: "second",
  	careOfPerson: "second_person",
  	streetAddress: "secondt_street",
  	state: "second",
    city: "Florida"
  	zipcode: "888",
  	officeNumber: "123",
    mobileNumber: "654",
    faxNumber: "t7s",
    addresstype: 2,
    country:2,
    client:4,
  })
  {
    clientAddress{
    id
    careOfPerson
    isActive
    state
    zipcode
    client{
      companyName
    }
    branchAs
    officeNumber
    mobileNumber
    country{
      id
      name
    }
    addresstype
    streetAddress
    branchAs
    
  }
  }
}

mutation clientAddressDelete{
  deleteClientAddress(id: 2){
   clientAddress{
      id
    }
  }
}

mutation clientAddressUpdate{
  updateClientAddress(id: 1, input: {
    isActive: true,
    addresstype: 2,
    branchAs: "Hello", 
    state: "Alaska",
    city:"Hawaii",
    careOfPerson: "Hello World",
    streetAddress: "Mirpur1",
    officeNumber: "12321",
    mobileNumber: "12312",
    faxNumber: "123123",
    countryId:2
    clientId:4
    
  })
  {
    clientAddress{
      id
      careOfPerson
      addresstype
      
    }
  }
}


#APB-7

#PaymentTerms
query allPaymentTerms{
  paymentTerms{
    id
    termName
    noDays
    dayOfMon
    dayNextMon
  }
}

query allSupplierDetails{
  supplierDetails{
    id
    isActive
    bankAccNo
    openBalDate
    openingBalance
    payRecurring
    isContractor
    sendInvitation
    notes
    payTerm{
      termName
    }
    currency{
      name
    }
    
  }
}

mutation PaymentCreation{
  createPaymentTerms(input: {
    termName: "Second",
    noDays: 4,
    dayOfMon: 5,
    dayNextMon: 12
  }){
    paymentTerms{
      termName
      noDays
    }
  }
}

mutation PaymentDeletion{
  deletePaymentTerms(id: 3){
    paymentTerms{
      termName
      noDays
    }
  }
}

mutation PaymentUpdate{
  updatePaymentTerms(id: 2, input:{
    termName: "Second Term",
    noDays: 2,
    dayOfMon: 21,
    dayNextMon: 12
  }){
    paymentTerms{
    id
    termName
    noDays
    dayOfMon
    dayNextMon
  }
  }
}

#Supplier Details
query allSupplierDetails{
  supplierDetails{
    id,
    isActive
    bankAccNo
    openBalDate
    openBalDate
    payRecurring
    isContractor
    sendInvitation
    notes
    payTerm{
      id
      termName
      noDays
      dayOfMon
      dayNextMon
    }
    currency{
      id
      symbol
      symbolNative
      name
      code
      country{
        name
      }
    }
    supplierId{
      id
      companyName
    }
    
  }
}

mutation SupplierDetailsCreation{
  createSupplierDetails(input: {
    isActive: true,
    bankAccNo: "12452454725Ac5",
    openingBalance: 500.23,
    payRecurring: true
    isContractor: true
    sendInvitation: true,
    notes: "Hello",
    payTermId:2,
    currencyId:1,
    supplierId:2,
  })
  {
    supplierDetails{
    id,
    isActive
    bankAccNo
    openBalDate
    openBalDate
    payRecurring
    isContractor
    sendInvitation
    notes
    payTerm{
      id
      termName
      noDays
      dayOfMon
      dayNextMon
    }
    currency{
      id
      symbol
      symbolNative
      name
      code
      country{
        name
      }
    }
    supplier{
      id
      companyName
    }
    
  }
  }
}

mutation SupplierDetailsDeletion{
  deleteSupplierDetails(id:3){
    supplierDetails{
      id
    }
  }
}

mutation SupplierDetailsUpdate{
  updateSupplierDetails(id:2, input:{
    isActive: true,
    bankAccNo: "123456789",
    openingBalance: 400.23,
    payRecurring: true,
    isContractor: true,
    sendInvitation: true,
    notes: "Second note",
    payTermId:1
    currencyId:1
    supplierId:1
  })
  {
    supplierDetails{
    id,
    isActive
    bankAccNo
    openBalDate
    openBalDate
    payRecurring
    isContractor
    sendInvitation
    notes
    payTerm{
      id
      termName
      noDays
      dayOfMon
      dayNextMon
    }
    currency{
      id
      symbol
      symbolNative
      name
      code
      country{
        name
      }
    }
    supplier{
      id
      companyName
    }
    
  }
  }
}
# APB - 8
# Client Details 
query allClientDetails{
  clientDetails{
    id
    bankAccNo
    openBalDate
    openingBalance
    payRecurring
    lateFees
    payReminder
    taxExemption
    sendInvitation
    notes
    currency{
  		id
      name
  	}
    payTerm{
      id
      termName
    }
    client{
      id
      companyName
    }
    paymentMethod{
      id
    }
    
  }
}

mutation clientDetailsCreation{
  createClientDetails(input: {
    bankAccNo: "142536789", 
    openingBalance: 700.12,
    payRecurring:true,
    lateFees: true,
    payReminder: true,
    taxExemption: true,
    sendInvitation: true,
    notes: "client-2",
    currency:1
    payTerm:1
    client: 1
    paymentMethod:1
  })
  {
    clientDetails{
      id
    }
  }
}


mutation clientDetailsDeletion{
  deleteClientDetails(id: 2){
    clientDetails{
      id
    }
  }
}

mutation clientDetailsUpdate{
  updateClientDetails(id: 1, input:{
    bankAccNo: "12345667",
    openingBalance: 400.23,
    payRecurring:true
    lateFees: false,
    payReminder: true,
    taxExemption: false,
    sendInvitation: true,
    notes: "updated client-1"
    currency:1
    payTerm:1
    clientId:2
    paymentMethodId:1
    
  })
  
	{
    clientDetails{
      id
      bankAccNo
      openBalDate
    }
  }
}
#APB - 9
#Item Type
query AllItemTypes{
	itemType{
    id
    name
    notes
  }  
}

mutation ItemTypeCreate{
  createItemTypes(input:{
    name: "second item type",
    notes: "item type second"
  })
  {
   itemType{
    name
    notes
  } 
  }
}
mutation ItemTypeUpdate{
  updateItemTypes(id: 2, input:{
    name: "second item type updated",
    notes: "item type second note updated"
  })
  {
   itemType{
    name
  } 
  }
}
mutation ItemTypeDelete{
  deleteItemTypes(id: 3)
  {
   itemType{
    name
  } 
  }
}

#Items Category
query AllItemsCatgory{
	itemCategory{
    id
    name
    notes
  }  
}

mutation ItemCategoryCreate{
  createItemCategory(input:{
    name: "second item type",
    notes: "item type second"
  })
  {
   itemCategory{
    name
    notes
  } 
  }
}
mutation ItemCategoryUpdate{
  updateItemCategory(id: 1, input:{
    name: "second item category updated",
    notes: "item category second note updated"
  })
  {
   itemCategory{
    name
  } 
  }
}
mutation ItemCategoryDelete{
  deleteItemCategory(id: 1)
  {
   itemCategory{
    name
  } 
  }
}

#Item Brands
query AllItemBrands{
	itemBrands{
    id
    isActive
    name
    notes
  }  
}

mutation ItemBrandsCreate{
  createItemBrands(input:{
    isActive: true
    name: "first item brand",
    notes: "item brand first"
  })
  {
   itemBrands{
    isActive
    name
    notes
  } 
  }
}
mutation ItemBrandUpdate{
  updateItemBrands(id: 1, input:{
    name: "first item brand updated",
    notes: "item brand first note updated"
  })
  {
   itemBrands{
    isActive
    name
    notes
  } 
  }
}
mutation ItemBrandDelete{
  deleteItemBrands(id: 1)
  {
   itemBrands{
    name
  } 
  }
}

#APB-10
# Items
query AllItems{
	items{
    id
    isActive
    name
    description
    SKU
    itemType{
      id
      name
    }
    itemCategory{
      id
      name
    }
    purchasePrice
    salesPrice
    markupPrice
    minSalesPrice
    weightParam
    weightValues
    volumeCbm
    supplier{
      id
      companyName
    }
    itemBrand{
      id
      name
    }
    upcNo
    mpnNo
    eanNo
    isbnNo
    itemBarcode
    warrantyMonth
    stockInHand
    initialStockEntry
    reorderPoint
    maxStockNo
    leadTimeDays
    allowSalesCommision
    commissionPerItem
    commissionPercentage
    tags
  }  
}

mutation ItemCreation{
  createItem(input:{
    isActive:true,
    name: "fourth item",
    description: "fourth item description",
    SKU: "10",
    itemType: 1,
    itemCategory:2
    purchasePrice: 12.50,
    salesPrice: 20,
    markupPrice: "10.15",
    minSalesPrice: 15,
    weightParam: "KG",
    weightValues: 5.1,
    volumeCbm: 3,
    supplier:3
    itemBrand:2
    accountName:2
    upcNo: "3",
    mpnNo: "3",
    eanNo: "3",
    isbnNo: "3",
    itemBarcode: "3",
    warrantyMonth: 10,
    stockInHand: 3,
    initialStockEntry: "2020-10-29T07:53:33.156157+00:00"
    reorderPoint: 3,
    maxStockNo: 5,
    leadTimeDays: 2,
    allowSalesCommision: true,
    commissionPerItem: 3,
    commissionPercentage: "10.14",
    tags: "fourth item tag"
  })
  {
    items{
      id
      name
    }
  }
}
mutation ItemUpdate{
  updateItem(id:9, input:{
    isActive:true,
    name: "ninth item",
    description: "ninth item description",
    SKU: "10",
    itemType: 1,
    itemCategory:2
    purchasePrice: 12.50,
    salesPrice: 20,
    markupPrice: "10.15",
    minSalesPrice: 15,
    weightParam: "KG",
    weightValues: 5.1,
    volumeCbm: 3,
    supplier:3
    itemBrand:2
    accountName:2
    upcNo: "3",
    mpnNo: "3",
    eanNo: "3",
    isbnNo: "3",
    itemBarcode: "3",
    warrantyMonth: 10,
    stockInHand: 3,
    initialStockEntry: "2020-10-29T07:53:33.156157+00:00"
    reorderPoint: 3,
    maxStockNo: 5,
    leadTimeDays: 2,
    allowSalesCommision: true,
    commissionPerItem: 3,
    commissionPercentage: "10.14",
    tags: "ninth item tag"
  })
  {
    items{
      id
      name
    }
  }
}

mutation ItemDelete{
  deleteItem(id: 3)
  {
    items{
      id
      name
    }
  }
}

#APB-11
# Item Group
query allItemGroup{
  itemGroup{
    id
    name
    isActive
    description
    SKU
    itemType{
      id
    }
    volumeCbm
    supplier{
      id
    }
    itemBrand{
      id
    }
    upcNo
    itemBarcode
    warrantyMonth
    accountNameId{
      id
    }
    tags
  }
}

mutation ItemGroupCreation{
  createItemGroup(input:{
    isActive: true,
    name: "second item Group",
    description: "Second item Group description",
    SKU: "10",
    itemType: 1
    volumeCbm: 2.1,
    supplier:3
    itemBrand:2
    accountName:2
    upcNo: "3",
    warrantyMonth: 10,
    tags: "Second item group tags"
  })
  
 { 
  itemGroup{
    id
    name
    isActive
  }
	}
}

mutation ItemGroupUpdate{
  updateItemGroup(id: 2, input:{
    isActive: true,
    name: "second item Group udpated",
    itemBarcode: "3",
    description: "Second item Group description updated",
    SKU: "10",
    itemType: 1
    volumeCbm: 2.1,
    supplier:3
    itemBrand:2
    accountNameId:2
    upcNo: "3",
    warrantyMonth: 10,
    tags: "Second item group tags upated"
  })
  
 { 
  itemGroup{
    id
    name
    isActive
  }
	}
}

mutation ItemGroupDelete{
	deleteItemGroup(id: 2)
  {
     itemGroup{
      id
      name
    }
  }
}

# Item Group Mapping
query allItemGroupMapping{
  itemGroupMapping{
    id
    item{
      id
      name
    }
    itemGroup{
      id
      name
    }
    quantity
  }
}

mutation{
  createItemGroupMapping(data: {
  	items:[
    {
      isActive:true,
    name: "fourth item",
    description: "fourth item description",
    SKU: "10",
    itemTypeId: 1
    itemCategory:2
    purchasePrice: 12.50,
    salesPrice: 20,
    markupPrice: "10.15",
    minSalesPrice: 15,
    weightParam: "KG",
    weightValues: 5.1,
    volumeCbm: 3,
    supplier:3
    itemBrand:2
    accountName:2
    upcNo: "3",
    mpnNo: "3",
    eanNo: "3",
    isbnNo: "3",
    itemBarcode: "3",
    warrantyMonth: 10,
    stockInHand: 3,
    initialStockEntry: "2020-10-29T07:53:33.156157+00:00"
    reorderPoint: 3,
    maxStockNo: 5,
    leadTimeDays: 2,
    allowSalesCommision: true,
    commissionPerItem: 3,
    commissionPercentage: "10.14",
    tags: "fourth item tag"
    },
        {
      isActive:true,
    name: "fifth item",
    description: "fifth item description",
    SKU: "10",
    itemTypeId: 1
    itemCategoryId:2
    purchasePrice: 12.50,
    salesPrice: 20,
    markupPrice: "10.15",
    minSalesPrice: 15,
    weightParam: "KG",
    weightValues: 5.1,
    volumeCbm: 3,
    supplierId:3
    itemBrandId:2
    accountNameId:2
    upcNo: "3",
    mpnNo: "3",
    eanNo: "3",
    isbnNo: "3",
    itemBarcode: "3",
    warrantyMonth: 10,
    stockInHand: 3,
    initialStockEntry: "2020-10-29T07:53:33.156157+00:00"
    reorderPoint: 3,
    maxStockNo: 5,
    leadTimeDays: 2,
    allowSalesCommision: true,
    commissionPerItem: 3,
    commissionPercentage: "10.14",
    tags: "fifth item tag"
    }
    ], 
    mappingQuantity: 2,
    itemGroups:{
      isActive: true,
    name: "thirs item Group",
    description: "third item Group description",
    SKU: "10",
    itemTypeId:1,
    volumeCbm: 2.1,
    supplier:3,
    itemBrand:2,
    accountNameId:2,
    upcNo: "3",
    warrantyMonth: 10,
    tags: "third item group tags"
    }
  }){
    itemGroupMapping{
      id
    }
  }
}


mutation itemGroupMappingUpdate{
  updateItemGroupMapping(data:
    {
      id: 1,
      items:15,
      itemGroups:8,
      mappingQuantity: 5
    })
 {
  itemsGroupMapping{
    id
    item{
      id
      name
    }
    itemGroup{
      id
      name
    }
  }
}
}

mutation deleteItemGroupMapping{
  deleteItemGroupMapping(id:5){
    itemGroupMapping{
      id
    }
  }
}


#APB-12
# Inventory Adjustment
query allInventoryAdjustment{
  inventoryAdjustment{
    id
    adjustmentReferenceNo
    timeLog
    causeOfAction
    accName{
      id
    }
    comments
  }
}


mutation InventoryAdjustmentCreation{
  createInventoryAdjustment(input: {
    isActive: true
    timeLog: "2020-10-30T12:50:55.744054+00:00"
    adjustmentReferenceNo: "Second inventory adjustment"
    causeOfAction: "Second inventory adjustment cause of action"
    accName: 2
    comments: "Second inventory ajdustment comments"
  })
  {
    inventoryAdjustment{
      id
    }
  }
}

mutation InventoryAdjustmentUpdate{
  updateInventoryAdjustment(id:1, input: {
    isActive: true
    timeLog: "2020-10-30T12:50:55.744054+00:00"
    adjustmentReferenceNo: "First inventory adjustment"
    causeOfAction: "First inventory adjustment cause of action"
    accName: 2
    comments: "First inventory ajdustment comments"
  })
  {
    inventoryAdjustment{
      id
    }
  }
}

mutation InventoryAdjustmentDelete{
  deleteInventoryAdjustment(id:2){
    inventoryAdjustment{
      id
    }
  }
}

# Inventory Adjustment Items
query allInventoryAdjustmentItems{
  inventoryAdjustmentItems{
    id
    inventoryAdjustment{
      id
      adjustmentReferenceNo
    }
    itemId{
      id
      name
    }
    quantityOrValue
    value
  }
}

mutation InventoryAdjustmentItemsCreation{
  createInventoryAdjustmentItems(input: {
    quantityOrValue: true
    value: 2
    inventoryAdjustment: 1
    itemId: 2
  })
  {
    inventoryAdjustmentItems{
      id
      value
    }
  }
}

mutation InventoryAdjustmentItemsUpdate{
  updateInventoryAdjustmentItems(id:2, input:{
    quantityOrValue: true
    value: 5
    inventoryAdjustment: 1
    itemId: 2
  })
  {
    inventoryAdjustmentItems{
      id
      value
    }
  }
}

mutation InventoryAdjustmentItemsDelete{
  deleteInventoryAdjustmentItems(id:2)
  {
    inventoryAdjustmentItems{
      id
      value
    }
  }
}

# Storage Location
query	allStorageLocation{
  storageLocation{
    id
    name
    address
    city
    isActive
    country
    {
    	id
      name
    }
    state
  	zipcode
    notes
  }
}


mutation StorageLocationCreation{
  createStorageLocation(input: {
    isActive: true
    address: "Second storage address"
    name: "Second Storage Location"
    city: "Tokyo",
    countryId: 1
    state: "Kansas"
    zipcode: "123"
    notes: "Second storage note"
  })
  {
    storageLocation{
      id
      name
    }
  }
}

mutation StorageLocationUpdate{
  updateStorageLocation(id:3, input:{
    isActive: true
   	address: "Third storage address"
    name: "Third Storage Location"
    city: "Tokyo",
    countryId: 1
    state: "Kansas"
    zipcode: "123"
    notes: "Third storage note"
  })
  {
      storageLocation{
      id
      name
    }
  }
}

mutation StorageLocationDelete{
  deleteStorageLocation(id:2)
  {
    storageLocation{
      id
      name
    }
  }
}

#APB-13
# Item Storage
query allItemStorage{
  itemStorage{
    id
    storageLocation{
      id
      name
    }
    notes
    lotNumber
    barcode
  }
}

mutation ItemStorageCreation{
  createItemStorage(input: {
    isActive: true
    lotNumber: "Second Item storage"
    barcode: "Second item storage barcode"
    notes: "Second item storage note"
    storageLocation: 1
  })
  {
    itemStorage{
    		id
    }
  }
}

mutation ItemStorageUpdate{
  updateItemStorage(id:1, input: {
    isActive: true
    lotNumber: "First Item storage lot Number"
    barcode: "First item storage barcode"
    notes: "First item storage note"
    storageLocation: 3
  })
  {
    itemStorage{
    		id
    }
  }
}

mutation ItemStorageDeletion{
  deleteItemStorage(id:3){
    itemStorage{
    		id
    }
  }
}

# Item Storage Mapping 
query allItemStorageMapping{
  itemStorageMapping{
    id
    itemId{
      id
      name
    }
    itemStorage{
      id
      lotNumber
      storageLocation{
        id
      }
    }
    quantity
    volume
  }
}

mutation ItemStorageMappingCreation{
  createItemStorageMapping(data: {
    items:[
    {
      isActive:true,
    name: "item storage first item",
    description: "item storage first item description",
    SKU: "10",
    itemTypeId: 1
    itemCategoryId:2
    purchasePrice: 12.50,
    salesPrice: 20,
    markupPrice: "10.15",
    minSalesPrice: 15,
    weightParam: "KG",
    weightValues: 5.1,
    volumeCbm: 3,
    supplierId:3
    itemBrandId:2
    accountNameId:2
    upcNo: "3",
    mpnNo: "3",
    eanNo: "3",
    isbnNo: "3",
    itemBarcode: "3",
    warrantyMonth: 10,
    stockInHand: 3,
    initialStockEntry: "2020-10-29T07:53:33.156157+00:00"
    reorderPoint: 3,
    maxStockNo: 5,
    leadTimeDays: 2,
    allowSalesCommision: true,
    commissionPerItem: 3,
    commissionPercentage: "10.14",
    tags: "item storage first item tag"
    },
        {
      isActive:true,
    name: "item storage second item",
    description: "item storage second item description",
    SKU: "10",
    itemTypeId: 1
    itemCategoryId:2
    purchasePrice: 12.50,
    salesPrice: 20,
    markupPrice: "10.15",
    minSalesPrice: 15,
    weightParam: "KG",
    weightValues: 5.1,
    volumeCbm: 3,
    supplierId:3
    itemBrandId:2
    accountNameId:2
    upcNo: "3",
    mpnNo: "3",
    eanNo: "3",
    isbnNo: "3",
    itemBarcode: "3",
    warrantyMonth: 10,
    stockInHand: 3,
    initialStockEntry: "2020-10-29T07:53:33.156157+00:00"
    reorderPoint: 3,
    maxStockNo: 5,
    leadTimeDays: 2,
    allowSalesCommision: true,
    commissionPerItem: 3,
    commissionPercentage: "10.14",
    tags: "item storage second item tag"
    }
    ], 
    quantity: 3
    volume: "second item storage Mapping volume 2"
    itemStorage:{
      isActive: true,
    	lotNumber: "fourth item storage lot number"
      storageLocationId: 3
      barcode: "fourth item storage barcode"
      notes: "fourth item storage notes"
    }
  })
  {
    itemStorageMapping{
    id
    itemId{
      id
    }
    itemStorage{
      id
    }
    quantity
    volume
  }
  }
}


mutation deleteItemStorageMapping{
  deleteItemStorageMapping(id:3){
    itemStorageMapping{
      id
    }
  }
}

mutation ItemStorageMappingUpdate{
   updateItemStorageMapping(data:
    {
      id: 1,
      items:16,
      itemStorage:4,
      quantity: 5
      volume: "First item storage mapping volume updated"
    })
 {
  itemStorageMapping{
    id
    item{
      id
      name
    }
    itemStorage{
      id
    }
  }
}
}

#APB-14
# Item Transfer
query allItemTransfer{
  itemTransfer{
    id
    isActive
    timeLog
    referenceNo
    fromStorageLocation{
      id
      name
    }
    toStorageLocation{
      id
      name
    }
    shoppingCarrier{
      id
      companyName
    }
    shippingMethod
    shipmentTrackingNo
    shipmentCost
    bilable
    notes
  }
}

mutation itemTransferCreation{
  createItemTransfer(input:{
    isActive: true,
    timeLog: "2020-11-02T11:55:26.687208+00:00"
    referenceNo: "second Item transfer reference"
    fromStorageLocationId: 3
    toStorageLocationId: 1
    shoppingCarrier:1
    shipmentCost:10
    shipmentTrackingNo: "111"
    shippingMethod: 3
    bilable: false
    notes: "second item transfer reference"
  })
  {
    itemTransfer{
      id
    }
  }
}

mutation itemTransferUpdate{
  updateItemTransfer(id: 2, input:{
    isActive: true,
    timeLog: "2020-11-02T11:55:26.687208+00:00"
    referenceNo: "First Item transfer reference"
    fromStorageLocationId: 3
    toStorageLocationId: 1
    shoppingCarrier:1
    shipmentCost:10
    shipmentTrackingNo: "111"
    shippingMethod: 3
    bilable: false
    notes: "First item transfer reference"
  })
  {
    itemTransfer{
      id
    }
  }
}

mutation itemTransferDeletion{
  deleteItemTransfer(id:3)
  {
		itemTransfer{
      id
    }
  }
}

#Item Transfer Mapping
query allItemTransferMapping{
  itemTransferMapping{
    id
    item{
      id
    }
    itemTransfer{
      id
    }
    quantity
    volume
  }
}


mutation ItemTransferMappingCreation{
  createItemTransferMapping(data: {
    items:[
    {
      isActive:true,
    name: "item transfer first item",
    description: "item transfer first item description",
    SKU: "10",
    itemTypeId: 1
    itemCategoryId:2
    purchasePrice: 12.50,
    salesPrice: 20,
    markupPrice: "10.15",
    minSalesPrice: 15,
    weightParam: "KG",
    weightValues: 5.1,
    volumeCbm: 3,
    supplierId:3
    itemBrandId:2
    accountNameId:2
    upcNo: "3",
    mpnNo: "3",
    eanNo: "3",
    isbnNo: "3",
    itemBarcode: "3",
    warrantyMonth: 10,
    stockInHand: 3,
    initialStockEntry: "2020-10-29T07:53:33.156157+00:00"
    reorderPoint: 3,
    maxStockNo: 5,
    leadTimeDays: 2,
    allowSalesCommision: true,
    commissionPerItem: 3,
    commissionPercentage: "10.14",
    tags: "item transfer first item tag"
    },
        {
      isActive:true,
    name: "item transfer second item",
    description: "item transfer second item description",
    SKU: "10",
    itemTypeId: 1
    itemCategoryId:2
    purchasePrice: 12.50,
    salesPrice: 20,
    markupPrice: "10.15",
    minSalesPrice: 15,
    weightParam: "KG",
    weightValues: 5.1,
    volumeCbm: 3,
    supplierId:3
    itemBrandId:2
    accountNameId:2
    upcNo: "3",
    mpnNo: "3",
    eanNo: "3",
    isbnNo: "3",
    itemBarcode: "3",
    warrantyMonth: 10,
    stockInHand: 3,
    initialStockEntry: "2020-10-29T07:53:33.156157+00:00"
    reorderPoint: 3,
    maxStockNo: 5,
    leadTimeDays: 2,
    allowSalesCommision: true,
    commissionPerItem: 3,
    commissionPercentage: "10.14",
    tags: "item transfer second item tag"
    }
    ], 
    quantity: 3
    volume: "Second item transfer Mapping volume"
    itemTransfer:{
      isActive: true,
    	timeLog: "2020-10-29T07:53:33.156157+00:00"
      fromStorageLocationId: 3
      toStorageLocationId: 1
      shoppingCarrier: 1
      shipmentTrackingNo: "first item transfer track no from item transfer mapping"
      shipmentCost: 12.34
      bilable: false
      referenceNo: "first item transfer reference no from item transfer mapping"
      notes: "first item transfer notes from item transfer mapping"
    }
  })
  {
    itemTransferMapping{
    id
    item{
      id
    }
    itemTransfer{
      id
    }
    quantity
    volume
  }
  }
}

mutation deleteItemTransferMapping{
  deleteItemTransferMapping(id:5){
    itemTransferMapping{
      id
    }
  }
}

mutation ItemTransferMappingUpdate{
   updateItemTransferMapping(data:
    {
      id: 1,
      items:16,
      itemTransfer:4,
      quantity: 5
      volume: "First item transfer mapping volume updated"
    })
 {
  itemTransferMapping{
    id
    item{
      id
      name
    }
    itemTransfer{
      id
    }
  }
}
}
""" 