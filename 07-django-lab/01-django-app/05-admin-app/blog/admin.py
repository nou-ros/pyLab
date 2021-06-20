from django.contrib import admin
from django.db.models import query
from django.utils import timezone

from django_summernote.admin import SummernoteModelAdmin

from django.db.models import Count

# Register your models here.
from blog.models import Blog, Comment, Category

from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter

from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter

from import_export.admin import ImportExportModelAdmin

from blog.resources import CommentResource

# 15 inlines for related field in parent page
# display comments(child) in Blog page(parent)
# we can also use admin.StackedInline
class CommentInline(admin.TabularInline):
    model = Comment
    fields = ('text', 'is_active')
    extra = 0 # make extra comment option to none default is 3
    # 16 collapse a section
    classes = ('collapse', )


# customize blog model in admin dashboard
class BlogAdmin(SummernoteModelAdmin):
    # 1. fields to display
    list_display = ('title', 'date_created', 'last_modified', 'is_draft',
     'days_since_creation', 'time_since_created', 'no_of_comments')
    # 2. filter list data (#20 date range filter by third party)
    list_filter = ('is_draft', 'date_created', ('date_created', DateRangeFilter), ('last_modified', DateTimeRangeFilter),)
    # 3. search data
    search_fields = ('title',)
    

    # 4. ordering data for every user
    # ordering = ('title', '-date_created')

    # provide user specific ordering
    def get_ordering(self, request):
        if request.user.is_superuser:
            return ('-date_created',)
        return ('title', '-date_created')

    # 5. prepopulate a filed
    prepopulated_fields = {'slug': ('title', )} 

    # 6. pagination - default is 100 items
    list_per_page = 50

    # 8. custom action method 
    def set_blogs_to_publish(self, request, queryset):
        count = queryset.update(is_draft=False)
        # to provide a message after each update
        self.message_user(request, '{} blogs have been published.'.format(count))
    
    # custom name to action method
    set_blogs_to_publish.short_description = "Mark blogs as published"
    
    # drop down actions of admin
    actions = ('set_blogs_to_publish',)


    # 9. navigation in dashboard by date_hierarchy
    date_hierarchy = 'date_created'

    # 10. model form styling with field layouts
    # fields = ('title', 'body', 'slug') # to hide a value
    # fields = (('title', 'is_draft'), 'body', 'slug') # to set values in same row

    # 11 model form styling with fieldsets (it is a touple of touple) 
    # we must not use fields(alone) if we are using fieldsets
    # we can have classes to sytle the fields sets using css.
    fieldsets = (
        ('General', {
            'fields': (('title',  'slug'), 'body'),
            'description': 'Common Options For Blogs',
            'classes' : ('collapse', ) #to collapse the fieldset
        }),
        ('Advanced', {
            'fields': ('is_draft', 'categories'),
            'description': 'Intermideate Options For Blogs',
            'classes': ('collapse',)
        })
    )

    # 12 custom model method field for field list. same can be done from model(see in model same function)
    def time_since_created(self, blog):
        diff = timezone.now() - blog.date_created
        return diff.days


    # 13 Rich text editor in admin (djangosummernote - thirdparty)
    summernote_fields = ('body',)

    # adding the inline from 15
    inlines = (CommentInline, )


    # 17 overriding changlist queryset to add a child model count
    def get_queryset(self, request) :
        queryset = super().get_queryset(request)
        # for each blog element annotate will add something say the number of comments
        queryset = queryset.annotate(comments_count=Count('comments')) # comments is the related name
        return queryset
    
    # extend of 17
    def no_of_comments(self, blog):
        return blog.comments_count

    # extend of 17 providing default sorting to the custom list field
    no_of_comments.admin_order_field = 'comments_count'

    # 18 many to many field styling for related field
    # filter_horizontal = ('categories', )
    filter_vertical = ('categories', )

    # 23 hide the delete selected option(1st method) 
    def get_actions(self, request):
        actions = super().get_actions(request)
        try:
            del actions['delete_selected']
        except KeyError:
            pass
        return actions
    
    # 24 hide delete a specific blog section
    def has_delete_permission(self, request, obj=None):
        return False 


# 14 one to many field relation model
class CommentAdmin(ImportExportModelAdmin):
    list_display = ('blog', 'text', 'date_created', 'is_active')

    # to edit list fields 
    list_editable = ('is_active',)

    list_per_page = 20

    # 19 dropdown list filtering with third party
    list_filter = (
        ('blog', RelatedDropdownFilter),
        ) 

    # 21 use of the import-export pkg
    resource_class = CommentResource

    #22 search by id for related field(default is a dropdown)
    raw_id_fields = ('blog', ) 
    
class CategoryAdmin(admin.ModelAdmin):
    pass




admin.site.register(Blog, BlogAdmin)

admin.site.register(Comment, CommentAdmin)

admin.site.register(Category, CategoryAdmin)
