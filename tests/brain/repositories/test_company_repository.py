from atlas.brain.models import Company
from atlas.brain.repositories import CompanyRepository


def test_get_company() -> None:
    company = Company.create(
        legal_name="ABC Imports",
    )

    repository = CompanyRepository([company])

    assert repository.get(company.id) == company


def test_exists_company() -> None:
    company = Company.create(
        legal_name="ABC Imports",
    )

    repository = CompanyRepository([company])

    assert repository.exists(company.id)


def test_list_all() -> None:
    company = Company.create(
        legal_name="ABC Imports",
    )

    repository = CompanyRepository([company])

    assert repository.list_all() == (company,)


def test_find_by_legal_name_returns_company() -> None:
    company = Company.create(
        legal_name="ABC Imports",
    )

    repository = CompanyRepository([company])

    assert repository.find_by_legal_name("ABC Imports") == company


def test_find_by_legal_name_returns_none() -> None:
    repository = CompanyRepository()

    assert repository.find_by_legal_name("Unknown") is None
