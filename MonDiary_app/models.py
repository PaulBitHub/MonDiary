from django.db import models

class Diary(models.Model):
    income_source = models.CharField(max_length=200, verbose_name="Статья дохода")
    expense_source = models.CharField(max_length=200, verbose_name="Статья расхода")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")
    comment = models.TextField(blank=True, null=True, verbose_name="Комментарий")
    operation_date = models.DateTimeField(verbose_name="Дата операции")

    def __str__(self):
        return f"{self.operation_date} - {self.income_source or self.expense_source} - {self.amount}"

    class Meta:
        verbose_name = "Запись в дневнике"
        verbose_name_plural = "Записи в дневнике"
