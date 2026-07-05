$folders = @(
    "E:\Projects\Atlas\src",
    "E:\Projects\Atlas\src\atlas",
    "E:\Projects\Atlas\src\atlas\brain",
    "E:\Projects\Atlas\src\atlas\brain\models",
    "E:\Projects\Atlas\src\atlas\brain\repositories",
    "E:\Projects\Atlas\src\atlas\brain\services",
    "E:\Projects\Atlas\src\atlas\core",
    "E:\Projects\Atlas\src\atlas\discovery",
    "E:\Projects\Atlas\src\atlas\verification",
    "E:\Projects\Atlas\src\atlas\api",
    "E:\Projects\Atlas\tests"
)

Write-Host ""
Write-Host "====================================="
Write-Host " Atlas - Folder Bootstrap"
Write-Host "====================================="
Write-Host ""

foreach ($folder in $folders) {
    if (-not (Test-Path $folder)) {
        New-Item -ItemType Directory -Path $folder | Out-Null
        Write-Host "[CREATED] $folder"
    }
    else {
        Write-Host "[EXISTS ] $folder"
    }
}

Write-Host ""
Write-Host "====================================="
Write-Host " Folder Bootstrap Complete"
Write-Host "====================================="
