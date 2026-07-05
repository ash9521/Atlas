import uuid

from atlas.brain.models import Company
from atlas.brain.repositories import CompanyRepository


def test_repository_is_empty() -> None:
    repository = CompanyRepository()

    assert repository.list_all() == ()


def test_get_company() -> None:
    company = Company.create("Acme Foods")

    repository = CompanyRepository([company])

    assert repository.get(company.id) == company


def test_exists() -> None:
    company = Company.create("Acme Foods")

    repository = CompanyRepository([company])

    assert repository.exists(company.id)


def test_missing_company_returns_none() -> None:
    repository = CompanyRepository()

    assert repository.get(uuid.uuid4()) is None
