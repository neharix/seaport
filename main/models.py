from django.db import models


# Create your models here.
class New(models.Model):
    title = models.CharField("Sözbaşy", max_length=500)
    image = models.ImageField("Surat", upload_to="news/")
    content = models.TextField()  # add ckeditor field
    posted_at = models.DateTimeField("Neşir edilen wagty", auto_now_add=True)

    class Meta:
        verbose_name = "täzelik"
        verbose_name_plural = "täzelikler"

    def __str__(self):
        return self.title


class Terminal(models.Model):
    name = models.CharField("Ady", max_length=100)

    class Meta:
        verbose_name = "terminal"
        verbose_name_plural = "terminallar"

    def __str__(self):
        return self.name


class Services(models.Model):
    name = models.CharField("Ady", max_length=100)

    class Meta:
        verbose_name = "hyzmat"
        verbose_name_plural = "hyzmatlar"

    def __str__(self):
        return self.name


# class TerminalContent(models.Model):
#     image
