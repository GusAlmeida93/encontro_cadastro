from datetime import date, datetime, time, timezone as dt_timezone
from io import StringIO
from unittest import mock

from django.contrib.auth.models import User
from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse

from .models import Cadastro


def create_cadastro(associado, rede="Agafarma", mesa="1"):
    return Cadastro.objects.create(associado=associado, rede=rede, mesa=mesa)


class CadastroModelTests(TestCase):
    def test_dia_and_hora_default_to_the_current_local_date_and_time(self):
        # 01:30 UTC on Oct 25 is still 22:30 on Oct 24 in São Paulo.
        now = datetime(2026, 10, 25, 1, 30, 45, 123456, tzinfo=dt_timezone.utc)
        with mock.patch("django.utils.timezone.now", return_value=now):
            cadastro = Cadastro()
        self.assertEqual(cadastro.dia, date(2026, 10, 24))
        self.assertEqual(cadastro.hora, time(22, 30, 45))

    def test_str(self):
        cadastro = Cadastro(associado="Sanofi", rede="Agafarma")
        self.assertEqual(str(cadastro), "Sanofi - Agafarma")

    def test_choices_are_unique_and_alphabetical(self):
        for name in ("associado", "rede"):
            values = [value for value, _ in Cadastro._meta.get_field(name).choices]
            self.assertEqual(values, sorted(set(values), key=str.casefold), name)

    def test_migrations_match_models(self):
        try:
            call_command("makemigrations", "--check", "--dry-run", stdout=StringIO())
        except SystemExit:
            self.fail("Model changes are missing a migration; run makemigrations.")


class HomeViewTests(TestCase):
    def test_lists_cadastros_by_associado(self):
        for associado in ("Sanofi", "Ache", "Medley"):
            create_cadastro(associado)
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            [cadastro.associado for cadastro in response.context["cadastros"]],
            ["Ache", "Medley", "Sanofi"],
        )
        self.assertContains(response, "/static/febrafar.png")

    def test_shows_fifteen_per_page(self):
        for mesa in range(1, 17):
            create_cadastro("Sanofi", mesa=str(mesa))
        page1 = self.client.get(reverse("home")).context["cadastros"]
        page2 = self.client.get(reverse("home"), {"page": 2}).context["cadastros"]
        self.assertEqual(len(page1), 15)
        self.assertEqual(len(page2), 1)
        self.assertEqual(len({cadastro.pk for cadastro in [*page1, *page2]}), 16)

    def test_invalid_page_shows_the_first_page(self):
        for mesa in range(1, 17):
            create_cadastro("Sanofi", mesa=str(mesa))
        response = self.client.get(reverse("home"), {"page": "abc"})
        self.assertEqual(response.context["cadastros"].number, 1)

    def test_out_of_range_page_shows_the_last_page(self):
        for mesa in range(1, 17):
            create_cadastro("Sanofi", mesa=str(mesa))
        response = self.client.get(reverse("home"), {"page": 99})
        self.assertEqual(response.context["cadastros"].number, 2)


class AdminTests(TestCase):
    def test_add_form_prefills_the_current_local_date_and_time(self):
        user = User.objects.create_superuser("admin", "admin@example.com", "unused")
        self.client.force_login(user)
        now = datetime(2026, 10, 25, 15, 30, 45, tzinfo=dt_timezone.utc)
        with mock.patch("django.utils.timezone.now", return_value=now):
            response = self.client.get(reverse("admin:cadastro_cadastro_add"))
        self.assertContains(response, 'name="dia" value="2026-10-25"')
        self.assertContains(response, 'name="hora" value="12:30:45"')
