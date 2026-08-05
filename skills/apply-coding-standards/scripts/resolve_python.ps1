param(
    [string]$ProjectPath = (Get-Location).Path
)

$candidates = @()

foreach ($environmentName in @('.venv', 'venv', 'env')) {
    $candidates += [PSCustomObject]@{
        Executable = (Join-Path $ProjectPath "$environmentName\Scripts\python.exe")
        Arguments = @()
        Source = "project $environmentName"
    }
}

if ($env:VIRTUAL_ENV) {
    $candidates += [PSCustomObject]@{
        Executable = (Join-Path $env:VIRTUAL_ENV 'Scripts\python.exe')
        Arguments = @()
        Source = 'active virtualenv'
    }
}

if ($env:CONDA_PREFIX) {
    $candidates += [PSCustomObject]@{
        Executable = (Join-Path $env:CONDA_PREFIX 'python.exe')
        Arguments = @()
        Source = 'active conda environment'
    }
}

if ($env:USERPROFILE) {
    $codexRuntime = Join-Path $env:USERPROFILE '.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
    $candidates += [PSCustomObject]@{
        Executable = $codexRuntime
        Arguments = @()
        Source = 'Codex Desktop runtime'
    }
}

foreach ($commandName in @('python.exe', 'python')) {
    $command = Get-Command $commandName -ErrorAction SilentlyContinue
    if ($command) {
        $candidates += [PSCustomObject]@{
            Executable = $command.Source
            Arguments = @()
            Source = "PATH command $commandName"
        }
    }
}

$launcher = Get-Command 'py.exe' -ErrorAction SilentlyContinue
if ($launcher) {
    $candidates += [PSCustomObject]@{
        Executable = $launcher.Source
        Arguments = @('-3')
        Source = 'Python launcher'
    }
}

$seen = @{}
foreach ($candidate in $candidates) {
    if (-not (Test-Path -LiteralPath $candidate.Executable)) {
        continue
    }

    $key = "$($candidate.Executable)|$($candidate.Arguments -join ' ')"
    if ($seen.ContainsKey($key)) {
        continue
    }
    $seen[$key] = $true

    try {
        $version = & $candidate.Executable @($candidate.Arguments) '--version' 2>&1
    }
    catch {
        continue
    }

    if ($LASTEXITCODE -eq 0) {
        [PSCustomObject]@{
            executable = $candidate.Executable
            arguments = $candidate.Arguments
            source = $candidate.Source
            version = ($version -join ' ').Trim()
        } | ConvertTo-Json -Compress
        exit 0
    }
}

Write-Error 'No working local Python interpreter was found. Create or activate a project virtual environment, then rerun this resolver once.'
exit 1
