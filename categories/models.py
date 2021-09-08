from django.db import models

class Category(models.Model):
    main_category = models.ForeignKey('MainCategory' , null=True, on_delete=models.SET_NULL,verbose_name='دسته بندی اصلی')
    sub_category = models.ManyToManyField('SubCategory',blank=True,verbose_name='دسته بندی های فرعی')
        

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"


    def __str__(self):
        return 'دسته بندی'

class MainCategory(models.Model):
    main_category = models.CharField(max_length=250,blank=True,null=True ,verbose_name='دسته بندی اصلی')
    class Meta:
        verbose_name = "دسته بندی اصلی"
        verbose_name_plural = "دسته بندی های اصلی"

    def __str__(self):
        return self.main_category

class SubCategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)


class SubCategory(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان دسته‌بندی")
    slug = models.SlugField(max_length=100, unique=True,
                            verbose_name="اسلاگ دسته‌بندی")
    status = models.BooleanField(
        default=True, verbose_name="آیا نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن")

    class Meta:
        verbose_name = " دسته‌بندی فرعی"
        verbose_name_plural = "دسته‌بندی های فرعی"
        ordering = ['position']

    def __str__(self):
        return self.title

    objects = SubCategoryManager()


