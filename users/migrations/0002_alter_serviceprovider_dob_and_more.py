# Generated by Django 4.2.7 on 2023-12-15 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceprovider',
            name='DOB',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='Gender',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='add',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='adhar',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='alt_number',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='bar_certificate',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='college',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='company',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='country',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='course_desc',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='father_first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='father_last_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='interest',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='pin_code',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='work_as',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='work_desc',
            field=models.TextField(null=True),
        ),
    ]
