from django.contrib import admin

from api.models import *

# Register your models here.
admin.site.register(Supplier)
admin.site.register(SupplierAdditionalContacts)
admin.site.register(Country)
admin.site.register(SupplierAddress)
admin.site.register(Clients)
admin.site.register(ClientAdditionalContacts)
admin.site.register(ClientAddress)
admin.site.register(SupplierDetails)
admin.site.register(PaymentTerms)
admin.site.register(Currency)
admin.site.register(PaymentMethods)
admin.site.register(ClientDetails)
admin.site.register(ItemType)
admin.site.register(ItemCategory)
admin.site.register(ItemBrands)
admin.site.register(HeadOfAccounts)
admin.site.register(AccountType)
admin.site.register(AccountName)
admin.site.register(Items)
admin.site.register(ItemsGroup)
admin.site.register(ItemGroupMapping)
admin.site.register(InventoryAdjustment)
admin.site.register(InventoryAdjustmentItems)
admin.site.register(StorageLocation)
admin.site.register(ItemStorage)
admin.site.register(ItemStorageMapping)
admin.site.register(ItemTransfer)
admin.site.register(ItemTransferMapping)