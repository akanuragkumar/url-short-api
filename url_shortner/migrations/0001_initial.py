from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=10000)),
                ('uuid', models.CharField(max_length=10, unique=True)),
                ('total_hit', models.IntegerField(default=0, blank=True)),
                ('hourly_hit', models.IntegerField(default=0, blank=True))
            ],
        ),
    ]
