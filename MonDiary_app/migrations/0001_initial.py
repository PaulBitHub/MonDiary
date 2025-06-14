# Generated by Django 5.1.4 on 2025-06-03 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Diary",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "income_source",
                    models.CharField(max_length=200, verbose_name="Статья дохода"),
                ),
                (
                    "expense_source",
                    models.CharField(max_length=200, verbose_name="Статья расхода"),
                ),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Сумма"
                    ),
                ),
                (
                    "comment",
                    models.TextField(blank=True, null=True, verbose_name="Комментарий"),
                ),
                ("operation_date", models.DateTimeField(verbose_name="Дата операции")),
            ],
            options={
                "verbose_name": "Запись в дневнике",
                "verbose_name_plural": "Записи в дневнике",
            },
        ),
    ]
