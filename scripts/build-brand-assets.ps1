param(
  [string]$SourceRoot = ""
)

$ErrorActionPreference = "Stop"
$repo = Split-Path $PSScriptRoot -Parent
if (-not $SourceRoot) {
  $SourceRoot = Join-Path (Split-Path $repo -Parent) "rollershow"
}

$assets = Join-Path $repo "brand-assets"
$logoDir = Join-Path $assets "logo"
$iconDir = Join-Path $assets "icons"
$photoDir = Join-Path $assets "photography"
$downloadDir = Join-Path $repo "downloads"
New-Item -ItemType Directory -Force $logoDir, $iconDir, $photoDir, $downloadDir | Out-Null

$utf8 = New-Object System.Text.UTF8Encoding($false)
$animated = Join-Path $logoDir "rollershow-logo-animated-tinta.svg"
$sourceLogo = Join-Path $SourceRoot "img\logo.svg"
if (Test-Path -LiteralPath $sourceLogo) {
  Copy-Item -LiteralPath $sourceLogo -Destination $animated -Force
} elseif (-not (Test-Path -LiteralPath $animated)) {
  throw "Falta el maestro local del logo: $animated"
}

$svg = [IO.File]::ReadAllText($animated)
$static = [regex]::Replace($svg, '<script\b[^>]*>[\s\S]*?</script>', '')
$static = $static -replace '<svg ', '<svg fill="#1C1816" '
[IO.File]::WriteAllText((Join-Path $logoDir "rollershow-logo-static-tinta.svg"), $static, $utf8)
$white = $static -replace 'fill="#1C1816"', 'fill="#FFFFFF"'
[IO.File]::WriteAllText((Join-Path $logoDir "rollershow-logo-static-blanco.svg"), $white, $utf8)

$photoSources = @{
  "blackout-gris-bedroom-reference.jpg" = "blackout-gris-bedroom.jpg"
  "sunscreen-living-bright-reference.jpg" = "sunscreen-living-bright.jpg"
}
foreach ($targetName in $photoSources.Keys) {
  $target = Join-Path $photoDir $targetName
  $source = Join-Path (Join-Path $SourceRoot "img") $photoSources[$targetName]
  if (Test-Path -LiteralPath $source) {
    Copy-Item -LiteralPath $source -Destination $target -Force
  } elseif (-not (Test-Path -LiteralPath $target)) {
    throw "Falta la fotografia canonica: $source"
  }
}

$manual = [IO.File]::ReadAllText((Join-Path $repo "index.html"))
$matches = [regex]::Matches($manual, '<span class="icon-item"><svg viewBox="0 0 24 24">([\s\S]*?)</svg>([^<]+)</span>')
if ($matches.Count -ne 16) {
  throw "Se esperaban 16 iconos en el manual y se encontraron $($matches.Count)."
}
$slugs = @("roller","tradicional","vertical","horizontal","ambiente","luz","medida","presupuesto","pago","fabricacion","entrega","instalacion","cuidado","garantia","posventa","consulta")
for ($i = 0; $i -lt $matches.Count; $i++) {
  $match = $matches[$i]
  $label = [System.Net.WebUtility]::HtmlDecode($match.Groups[2].Value.Trim())
  $slug = $slugs[$i]
  $icon = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#1C1816" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">' + $match.Groups[1].Value + '</svg>'
  [IO.File]::WriteAllText((Join-Path $iconDir "$slug.svg"), $icon, $utf8)
}

$files = Get-ChildItem -LiteralPath $assets -Recurse -File | Where-Object Name -Ne "manifest.json" | Sort-Object FullName
$manifestFiles = foreach ($file in $files) {
  [ordered]@{
    path = $file.FullName.Substring($assets.Length + 1).Replace('\','/')
    bytes = $file.Length
    sha256 = (Get-FileHash -LiteralPath $file.FullName -Algorithm SHA256).Hash.ToLowerInvariant()
  }
}
$manifest = [ordered]@{
  package = "RollerShow Brand Assets"
  version = "1.1.2"
  manualVersion = "2.2"
  generatedAt = (Get-Date).ToString("yyyy-MM-dd")
  canonicalLogoSource = "https://assets.rollershow.com.ar/2021/img/rs_logo_animado_b.svg"
  compactMarkStatus = "No existe isotipo o favicon compacto aprobado. No recortar letras del wordmark."
  files = $manifestFiles
}
[IO.File]::WriteAllText((Join-Path $assets "manifest.json"), ($manifest | ConvertTo-Json -Depth 5), $utf8)

$zip = Join-Path $downloadDir "rollershow-brand-assets-v1.1.2.zip"
if (Test-Path -LiteralPath $zip) { Remove-Item -LiteralPath $zip -Force }
Compress-Archive -Path (Join-Path $assets "*") -DestinationPath $zip -CompressionLevel Optimal
Write-Output "Brand assets listos: $zip"
