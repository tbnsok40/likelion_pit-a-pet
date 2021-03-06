# Generated by Django 2.2.10 on 2020-06-05 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regiprofile',
            name='pet_age',
            field=models.IntegerField(null=True, verbose_name='3. 펫 나이'),
        ),
        migrations.AlterField(
            model_name='regiprofile',
            name='pet_gender',
            field=models.CharField(choices=[('남', '남'), ('여', '여'), ('중성', '중성')], max_length=2, null=True, verbose_name='성별'),
        ),
        migrations.AlterField(
            model_name='regiprofile',
            name='pet_image',
            field=models.ImageField(null=True, upload_to='', verbose_name='4. 프로필 사진'),
        ),
        migrations.AlterField(
            model_name='regiprofile',
            name='pet_intro',
            field=models.TextField(max_length=100, null=True, verbose_name='5. 소개'),
        ),
        migrations.AlterField(
            model_name='regiprofile',
            name='pet_name',
            field=models.CharField(max_length=20, null=True, verbose_name='1. 펫 이름'),
        ),
        migrations.AlterField(
            model_name='regiprofile',
            name='pet_type',
            field=models.CharField(max_length=20, null=True, verbose_name='2. 펫 종류'),
        ),
    ]
