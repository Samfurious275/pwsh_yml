$source = "/home/samrider/Downloads"
$backupDir = "/home/samrider/Music"
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$backupPath = "$backupDir/Music/$timestamp"

Copy-Item -Path $source -Destination $backupPath -Recurse
Compress-Archive -Path $backupPath -Destination "$backupPath.zip" -Force
Remove-Item -Path $backupPath -Recurse
