from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from module import ModuleViews


urlpatterns = [
    path('modules/add_module', ModuleViews.add_module, name = "add_module"),
    path('add_module_save', ModuleViews.add_module_save),
    path('modules/modules', ModuleViews.manage_modules ,name ="manage_modules"),
    path('delete_module/<str:id_>', ModuleViews.delete_module, name="delete_module"),
    path('edit_module_save', ModuleViews.edit_module_save),
    path('edit_module/<str:id_>', ModuleViews.edit_module),
    path('modules/add_element_module', ModuleViews.add_element_module , name="add_element_module"),
    path('modules/add_element_module_save', ModuleViews.add_element_module_save),
    path('modules/elements_module', ModuleViews.manage_elem_modules ,name ="manage_elem_modules"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


