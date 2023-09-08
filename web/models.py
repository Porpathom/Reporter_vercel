from django.db import models
from django.forms import ModelForm

CATEGORY_CHOICES = [
    (1,'ข่าวกีฬา'),
    (2,'ข่าวบันเทิง'),
    (3,'ข่าวการเมือง'),
    (4,'ข่าวอาชญากรรม')
]

# Create your models here.
class Reporter(models.Model):
    
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    

    class Meta:
        verbose_name = "Reporter"
        verbose_name_plural = "Reporters"

    def __str__(self):
        return self.first_name + " "+self.last_name

    def get_absolute_url(self):
        return reversed("Reporter_detail", kwargs={"pk": self.pk})

class Art(models.Model):
    
    head_line = models.CharField(max_length=255)
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=1)
    pub_date = models.DateTimeField(auto_now=True)
    pub_data = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE, default=1)
    

    class Meta:
        verbose_name = "Art"
        verbose_name_plural = "Arts"

    def __str__(self):
        return self.head_line

    def get_absolute_url(self):
        return reversed ("Art_detail", kwargs={"pk": self.pk})

class ReporterForm(ModelForm):
    """Form definition for Reporter."""

    class Meta:
        """Meta definition for Reporterform."""

        model = Reporter
        fields = ('first_name', 'last_name', 'email')


class ArtForm(ModelForm):
    """Form definition for Art."""

    class Meta:
        """Meta definition for Artform."""

        model = Art
        fields = ('head_line', 'pub_data', 'category', 'reporter')
