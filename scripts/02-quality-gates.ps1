$ProjectRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
Set-Location $ProjectRoot

$Python = Join-Path $ProjectRoot ".venv\Scripts\python.exe"

if (-not (Test-Path $Python)) {
    Write-Host ""
    Write-Host "=========================================" -ForegroundColor Red
    Write-Host "❌ Virtual environment not found" -ForegroundColor Red
    Write-Host "=========================================" -ForegroundColor Red
    Write-Host ""
    Write-Host "Expected:" $Python
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""
Write-Host "========================================="
Write-Host " Atlas Quality Gates"
Write-Host "========================================="
Write-Host ""

Write-Host "Using Python:"
Write-Host $Python
Write-Host ""

Write-Host "[1/3] Running pytest..." -ForegroundColor Cyan
& $Python -m pytest

if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "❌ pytest FAILED" -ForegroundColor Red
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit $LASTEXITCODE
}

Write-Host ""
Write-Host "[2/3] Running mypy..." -ForegroundColor Cyan
& $Python -m mypy src

if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "❌ mypy FAILED" -ForegroundColor Red
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit $LASTEXITCODE
}

Write-Host ""
Write-Host "[3/3] Running ruff..." -ForegroundColor Cyan
& $Python -m ruff check .

if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "❌ ruff FAILED" -ForegroundColor Red
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit $LASTEXITCODE
}

Write-Host ""
Write-Host "========================================="
Write-Host "✅ ALL QUALITY GATES PASSED" -ForegroundColor Green
Write-Host "=========================================" -ForegroundColor Green
Write-Host ""

git status

Write-Host ""
Read-Host "Quality gates complete. Press Enter to exit"
