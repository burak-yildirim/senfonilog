from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id) + "-" + self.name


class Blog(models.Model):
    header = models.CharField("Başlık", max_length=50)
    post = models.TextField("Gönderi")
    create_date = models.DateTimeField("Oluşturulma Tarihi", auto_now=True)
    author = models.CharField("Yazar", max_length=20)
    tag = models.ForeignKey(
        Tag, on_delete=models.CASCADE, verbose_name="Etiket", default=0)

    def __str__(self):
        return self.header + "-" + str(self.create_date) + "-" + self.author + "-" + self.tag.name


class Comment(models.Model):
    text = models.TextField("Yazı")
    create_date = models.DateTimeField("Oluşturulma Tarihi", auto_now=True)
    author = models.CharField("Yazar", max_length=20)
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, verbose_name="Blog")

    def __str__(self):
        return self.blog.header + "-" + self.author + "-" + str(self.create_date)
