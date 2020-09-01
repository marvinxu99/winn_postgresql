# Generated by Django 3.0.7 on 2020-09-01 05:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('itrac', '0003_auto_20200828_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='issue_type',
            field=models.CharField(choices=[('01', 'Break/fix'), ('02', 'New feature'), ('03', 'Optimization'), ('04', 'Task')], default='01', max_length=2),
        ),
        migrations.CreateModel(
            name='IssueToIssueLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_from_type', models.CharField(choices=[('01', 'relates to'), ('02', 'blocks'), ('03', 'is blocked by'), ('04', 'causes'), ('05', 'is caused by'), ('06', 'clones'), ('07', 'is cloned by'), ('08', 'duplicates'), ('09', 'is duplicated by')], default='01', max_length=2)),
                ('link_to_type', models.CharField(choices=[('01', 'relates to'), ('02', 'blocks'), ('03', 'is blocked by'), ('04', 'causes'), ('05', 'is caused by'), ('06', 'clones'), ('07', 'is cloned by'), ('08', 'duplicates'), ('09', 'is duplicated by')], default='01', max_length=2)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('linked_from_issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='linked_to_issues', to='itrac.Issue')),
                ('linked_to_issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='linked_from_issues', to='itrac.Issue')),
                ('updated_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'itrac_issue_issue_link',
            },
        ),
    ]
