from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.id) + "-" + self.name


class Blog(models.Model):
    header = models.CharField("Başlık", max_length=50, blank=False, null=False)
    post = models.TextField("Gönderi", blank=False, null=False)
    create_date = models.DateTimeField(
        "Oluşturulma Tarihi", blank=True, auto_now=True)
    author = models.CharField("Yazar", max_length=20, blank=False, null=False)
    tag = models.ForeignKey(
        Tag, on_delete=models.CASCADE, verbose_name="Etiket", default=0)

    def __str__(self):
        return self.header + "-" + str(self.create_date) + "-" + self.author + "-" + self.tag.name


class Comment(models.Model):
    text = models.TextField("Yazı", blank=False, null=False)
    create_date = models.DateTimeField("Oluşturulma Tarihi", auto_now=True)
    author = models.CharField("Yazar", max_length=20, blank=False, null=False)
    author_email = models.EmailField(
        "Yazar Email", max_length=30, blank=False, null=False)
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, verbose_name="Blog")

    def __str__(self):
        return self.blog.header + "-" + self.author + "-" + str(self.create_date)
