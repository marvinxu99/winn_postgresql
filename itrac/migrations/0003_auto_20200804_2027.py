# Generated by Django 3.0.7 on 2020-08-05 03:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('itrac', '0002_auto_20200520_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
                'ordering': ['title'],
            },
        ),
        migrations.RemoveField(
            model_name='reply',
            name='author',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='comment',
        ),
        migrations.AlterModelOptions(
            name='issue',
            options={'ordering': ['title'], 'verbose_name': 'issue', 'verbose_name_plural': 'issues'},
        ),
        migrations.RemoveField(
            model_name='issue',
            name='tag',
        ),
        migrations.AddField(
            model_name='issue',
            name='issue_prefix',
            field=models.CharField(default='WINN', max_length=20),
        ),
        migrations.AddField(
            model_name='issue',
            name='slug',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='issue',
            name='updated_by',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='issue_updated_by', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='issue',
            name='description',
            field=models.TextField(blank=True, max_length=4000),
        ),
        migrations.AlterField(
            model_name='issue',
            name='issue_type',
            field=models.CharField(choices=[('01', 'Break/fix'), ('02', 'New feature'), ('03', 'Optimization')], default='01', max_length=2),
        ),
        migrations.AlterField(
            model_name='issue',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='issue',
            name='resolved_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('01', 'Open'), ('02', 'Investigate'), ('03', 'Await approval'), ('04', 'Build in progress'), ('05', 'Validate in progress'), ('06', 'Complete'), ('07', 'Closed')], default='01', max_length=2),
        ),
        migrations.AlterField(
            model_name='issue',
            name='upvotes',
            field=models.IntegerField(default=0, verbose_name='likes'),
        ),
        migrations.AlterField(
            model_name='savedissue',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_savedissues', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='issue',
            index=models.Index(fields=['title'], name='itrac_issue_title_8c63b4_idx'),
        ),
        migrations.DeleteModel(
            name='Reply',
        ),
        migrations.AddIndex(
            model_name='tag',
            index=models.Index(fields=['title'], name='itrac_tag_title_c88491_idx'),
        ),
        migrations.AddField(
            model_name='issue',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='issues', to='itrac.Tag'),
        ),
    ]
