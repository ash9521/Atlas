from pathlib import Path

from openpyxl import Workbook

from atlas.discovery.connectors import ExcelConnector
from atlas.discovery.models import InputSource


def test_excel_connector(tmp_path: Path):
    workbook = Workbook()
    worksheet = workbook.active

    worksheet.append(
        [
            "Company",
            "Country",
        ],
    )

    worksheet.append(
        [
            "ABC Imports",
            "Germany",
        ],
    )

    file_path = tmp_path / "buyers.xlsx"
    workbook.save(file_path)
    workbook.close()

    connector = ExcelConnector()

    source = InputSource.create(
        source_type="file",
        location=str(file_path),
    )

    observations = connector.acquire(source)

    assert len(observations) == 1
    assert observations[0].connector == "excel"
    assert observations[0].payload["Company"] == "ABC Imports"
    assert observations[0].payload["Country"] == "Germany"
