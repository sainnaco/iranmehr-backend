from django.db import models
from django.db.models.lookups import LessThan
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.urls import reverse
from django.utils.html import format_html
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from categories.models import Category
from extensions.utils import jalali_converter

User = get_user_model()

class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش‌نویس'),		 # draft
        ('p', "منتشر شده"),		 # publish
    )

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL,
                               related_name='articles', verbose_name="نویسنده")
    title = models.CharField(max_length=200,null=True,blank=True, verbose_name="عنوان مقاله")
    slug = models.SlugField(max_length=100, unique=True,
                            verbose_name="اسلاگ مقاله")
    article_category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL,
                                 verbose_name=" دسته‌بندی اصلی", related_name="articles")
    description =RichTextUploadingField(null=True,blank=True,verbose_name="محتوا")
    # thumbnails = models.ImageField(upload_to="images/article",blank=True,null=True,verbose_name="تصویر ۶۴۰x۳۶۰ مقاله")
    thumbnail = models.ImageField(default='test.png',null=True,blank=True,upload_to="images/article",verbose_name='عکس بند انگشتی')
    publish = models.DateTimeField(
        default=timezone.now, verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default='d', verbose_name="وضعیت")
    view_count = models.IntegerField(default=1,blank=True,null=True ,verbose_name='تعداد بازدید')

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ['-publish']

    objects = ArticleManager()

    def __str__(self):
        return self.title

    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description = "زمان انتشار"

    def thumbnail_tag(self):
        if self.thumbnail:
            return format_html("<img width=100 height=75 style='border-radius: 5px;' src='{}'>".format(self.thumbnail.url))
    thumbnail_tag.short_description = "عکس"

    # def preview_url(self):
    #     return format_html("<a href='{}' target='blank'>پیش‌نمایش</a>".format(reverse("article:preview-detail", kwargs={'slug': self.slug})))
    # preview_url.short_description = "پیش‌نمایش"

    # def save(self, *args, **kwargs):
    #     if self.status == "d":
    #         for comment in self.comments.active():
    #             comment.status = False
    #             comment.save()
    #     super(Article, self).save(*args, **kwargs)



    # def save(self, *args, **kwargs):
    #     if not self.status:
    #         for article in self.articles.published():
    #             article.status = 'd'
    #             article.save()
    #     super(Category, self).save(*args, **kwargs)

# class Priority(models.Model):
#     level_one = models.BooleanField(default=True,verbose_name='اولویت عادی')
#     level_two = models.BooleanField(default=False,verbose_name='اولویت متوسط')
#     level_tree = models.BooleanField(default=False,verbose_name='اولویت مهم')
#     level_four = models.BooleanField(default=False,verbose_name='الویت بسیار مهم')

#     def __str__(self):
#         if self.level_four :
#             return 'بسیار مهم'
#         elif self.level_tree :
#             return 'مهم'
#         elif self.level_two :
#             return 'نسبتا مهم'
#         else :
#             return 'عادی'  



# class IpAddress(models.Model):
#     pub_date = models.DateTimeField('زمان اولین بازدید')
#     ip_address = models.GenericIPAddressField(verbose_name='آدرس')

#     class Meta:
#         verbose_name = "آی‌پی"
#         verbose_name_plural = "آی‌پی ها"
#         ordering = ['pub_date']

#     def __str__(self):
#         return self.ip_address


# class ArticleHit(models.Model):
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)
#     ip_address = models.ForeignKey(IpAddress, on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)


# class CommentManager(models.Manager):
# 	def active(self):
# 		return self.filter(status=True)

# class Comment(models.Model):
# 	article = models.ForeignKey(Article, null=True, on_delete=models.SET_NULL, related_name="comments", verbose_name="مقاله")
# 	user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="comments", verbose_name="کاربر")
# 	content =models.TextField(null=True,blank=True)
#     # RichTextField(verbose_name="دیدگاه")
# 	author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="answers", verbose_name="پاسخ‌دهنده")
# 	answer =models.TextField(null=True,blank=True)
#     # RichTextField(blank=True, verbose_name="پاسخ")
# 	created = models.DateTimeField(auto_now_add=True)
# 	updated = models.DateTimeField(auto_now=True)
# 	status = models.BooleanField(default=False, verbose_name="تایید")

# 	class Meta:
# 		verbose_name = "دیدگاه"
# 		verbose_name_plural = "دیدگاه‌ها"
# 		ordering = ['-created']

# 	objects = CommentManager()

# 	def save(self, *args, **kwargs):
# 		if self.article and self.user and self.content and not self.author and not self.answer and not self.status:
# 			email = EmailMessage(
# 				"دیدگاه جدید",
# 				"<p style='direction: rtl;text-align: right;'>سلام، دیدگاه جدیدی برای مقاله ات هست: <a href='https://silicium.ir/admin/article/comment/?article__author__id__exact={}&status__exact=0'>مشاهده</a></p>".format(self.article.author.pk),
# 				to=[self.article.author.email]
# 			)
# 			email.content_subtype = "html"
# 			email.send()
# 		elif self.article and self.user and self.content and self.status and (not self.author or not self.answer):
# 			email = EmailMessage(
# 				"دیدگاه شما تایید شد (:",
# 				"<p style='direction: rtl;text-align: right;'>سلام، دیدگاه شما که مدتی قبل برامون نوشته بودید، تایید شد: <a href='https://silicium.ir{}'>مشاهده</a><br>ممنون از دیدگاهتون</p>".format(reverse("article:detail", kwargs={'slug': self.article.slug})),
# 				to=[self.user.email]
# 			)
# 			email.content_subtype = "html"
# 			email.send()
# 		elif self.article and self.user and self.content and self.status and self.author and self.answer:
# 			email = EmailMessage(
# 				"به دیدگاه شما پاسخ دادیم (:",
# 				"<p style='direction: rtl;text-align: right;'>سلام، دیدگاه شما که مدتی قبل برامون نوشته بودید، تایید شد و بهش پاسخ دادیم: <a href='https://silicium.ir{}'>مشاهده</a><br>ممنون از دیدگاهتون</p>".format(reverse("article:detail", kwargs={'slug': self.article.slug})),
# 				to=[self.user.email]
# 			)
# 			email.content_subtype = "html"
# 			email.send()
# 		super(Comment, self).save(*args, **kwargs)