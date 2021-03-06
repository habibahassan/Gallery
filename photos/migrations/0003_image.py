# Generated by Django 2.1 on 2020-02-29 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=60)),
                ('image_description', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(default='DEFAULT VALUE', upload_to='images/')),
                ('category', models.ManyToManyField(to='photos.Category')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.Location')),
            ],
        ),
    ]
