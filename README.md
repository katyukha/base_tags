# Generic tags (base_tags)

Base tags implementation for Odoo

Consists of set of modules to add tags to standard Odoo models.

## Project moved

See [crnd-inc/generic-addons](https://github.com/crnd-inc/generic-addons) for last version.

Project was moved there and renamed to `generic_tag`

There are versions for 9-12.

Supported last 2-3 versions.

## At this moment there are modules to add tags for models:

  - account.invoice model
  - product.product model
  
## Compatability:

  - Odoo version 7.0: *works fine*
  - Odoo version 8.0 and higher: *not tested*
  
## Usage

To add tags to your model You need to folow folowing simple steps:

1. Add ```base_tags``` module as dependency for your module

2. Use inherit from ```"res.tag.mixin"``` to get tags functionality to Your model, like:

   ```python
    class Product(orm.Model):
        _name = "product.product"
        _inherit = ["product.product",
                    "res.tag.mixin"]
    Product()
   ```
3. Add record to taggable models registry:
   
   ```xml
    <record model="res.tag.model" id="res_tag_model_product_product">
      <field name="name">Product</field>
      <field name="model">product.product</field>
    </record>
    ```
4. Now You can use ```tag_ids``` field in Your views for Your model:

   - search view:
    
    ```xml
    <field name="tag_ids" string="Tag"
           filter_domain="['|',('tag_ids.name','ilike',self),('tag_ids.code','ilike',self)]"/>
    <field name="no_tag_id" string="No tag"/>  <!-- For invers searching (items that do not contain tag)-->
    ```
   - tree view:
  
    ```xml
    <field name="tag_ids" widget="many2many_tags" placeholder="Tags..."/>
    ```
   - form view:
    
    ```xml
    <field name="tag_ids"
           widget="many2many_tags"
           placeholder="Tags..."
           context="{'default_model': 'product.product'}"/>
    ```
    
    Pay attention on context field. This will allow to avoid tag form popup when adding tag from form field
    
## Future plans

- custom widget to show help/comment on tags mous over
- ability to show tags same in form view and in tree/list view
- make tags colored (any tag could have ovn color to fill backround in)
