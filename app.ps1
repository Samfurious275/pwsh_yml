$appUrl = "https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.4.8/npp.8.4.8.Installer.x64.exe"
$output = "/home/samrider/Downloads/notepad++.exe"
Write-Host "$output"
Invoke-WebRequest -Uri $appUrl -OutFile $output

