Set-Location $PSScriptRoot\..

Write-Host ""
Write-Host "========================================="
Write-Host " Atlas Quality Gates"
Write-Host "========================================="
Write-Host ""

Write-Host "[1/3] Running pytest..." -ForegroundColor Cyan
python -m pytest

if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "❌ pytest FAILED" -ForegroundColor Red
    exit $LASTEXITCODE
}

Write-Host ""
Write-Host "[2/3] Running mypy..." -ForegroundColor Cyan
python -m mypy src

if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "❌ mypy FAILED" -ForegroundColor Red
    exit $LASTEXITCODE
}

Write-Host ""
Write-Host "[3/3] Running ruff..." -ForegroundColor Cyan
python -m ruff check .

if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "❌ ruff FAILED" -ForegroundColor Red
    exit $LASTEXITCODE
}

Write-Host ""
Write-Host "========================================="
Write-Host "✅ ALL QUALITY GATES PASSED"
Write-Host "=========================================" -ForegroundColor Green
Write-Host ""

git status
