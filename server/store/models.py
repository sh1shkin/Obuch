from django.db import models # импорт пакета models

# Create your models here.
# models == table


class ProductCategory(models.Model): #для того чтобы пайтон понял, что мы создаем модель мы должны насследовать от абстактного класса Model 
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)
    # null разрешает нам хранить занчение null в колонке
    # blank позволяет нам быть полю пустым
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=512)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    #max_digits = поле позволяет нам поределить максимальное число символов до запятой
    #decimal_places = поле позволяет нам определить число элементов после запятой
    quantity = models.PositiveIntegerField(default=0)
    #PositiveIntegerField - класс который соответсвует unsigned integer, поле default - говорит нам о том какое значение харится
    # по умолчанию
    image = models.ImageField(upload_to='products_images')
    #imageField - по сути класс котоый позволяет обрабатывать картинки в Django upload_to - указывает на директорию куда будут сохраняться наши картинки
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
    #Cascade - все связанные с этой сущностью сущности будут удалены при удалении этой сущностью
    #PROTECT - защищает удаление родительского объекта, если с ним связаны другие объекты
    def __str__(self):
        return self.name