$inputDir = "."
$extension = ".ide4"
$searchKey = "DataLink"
$newValue = 'TCP/IP'
$outputDir = "C:\Users\creddy\OneDrive - IDEX Corporation\Documents\Migrate KK to KK 2.0\KK_2_0"
# Get-ChildItem -Path $folder -Filter *$extension | Where-Object { !$_.PSIsContainer } | Select-Object FullName

if (!(Test-Path $inputDir)) {
    Write-Host "Input directory does not exist"
    exit
}
  
if (!(Test-Path $outputDir)) {
    Write-Host "Output directory does not exist"
    exit
}

$fileList = Get-ChildItem -Path $inputDir -File -Filter "*$extension"

$fileArray = @()
foreach ($file in $fileList) {
    $fileArray += $file.Name
}

foreach ($file in $fileArray) {
    Write-Host $file



    if (Test-Path $file) {
        # Read the content of the file
        $content = Get-Content $file -Raw | ForEach-Object {
            if ($_ -match "($searchKey)\s*=\s*(.*)") {
                # Modify the content at the specified location
                $_ -replace "($searchKey)\s*=\s*(.*)", "`$1 = $newValue"
            }
            else {
                $_
            }
        }

        $outputFilePath = Join-Path $outputDir $file
        Write-Host "output file path is $outputFilePath"

        # Save the modified content back to the file
        Set-Content -Path $outputFilePath -Value $content

        # Save the modified content back to the file
        # Set-Content $file $content

        Write-Host "The value of key '$searchKey' in file '$file' has been updated to '$newValue'."
    }
    else {
        Write-Host "The specified file '$file' does not exist."
    }
}


## List directory, Filter based on extensions, Store file list in array, read file, search content, modify content, write file and test path