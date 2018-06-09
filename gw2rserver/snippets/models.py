from django.db import models


class Snippet(models.Model):
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=100, blank=True, default='')
    project = models.CharField(choices=[('Project','Project')], default='python', max_length=100)
    materials = models.CharField(max_length=100, blank=True, default='')
    CR = models.TextField()
    DR = models.TextField()

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        super(Snippet, self).save(*args, **kwargs)

class CheckVoucher(models.Model):
    owner = models.TextField()
    particulars = models.TextField()
    supplier = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    cvno = models.TextField()
    amount = models.TextField()

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        super(CheckVoucher, self).save(*args, **kwargs)
        