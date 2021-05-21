#Angel Marcelo Martínez Hernandez 1804972#




function show_ppal_menu
{
param (
[string]$Title = 'Menú'
)
cls
Write-Host "================ $Title ================"
 
Write-Host "1: Ver-StatusPerfil"
Write-Host "2: Cambiar-StatusPerfil"
Write-Host "3: Ver-PerfilRedActual"
Write-Host "4: Cambiar-PerfilRedActual "
Write-Host "5: Ver-ReglasBloqueo"
Write-Host "6: Agregar-ReglasBloqueo "
Write-Host "7: Eliminar-ReglasBloqueo "
Write-Host "Q: Press 'Q' to quit."
}

do
{
show_ppal_menu
$input = Read-Host "Selecciona una opción"
switch ($input)
{
'1' {
cls
'Has seleccionado la opción Ver-StatusPerfil'

 Ver-StatusPerfil

} '2' {
cls
'Has seleccionado la opción Cambiar-StatusPerfil'

Cambiar-StatusPerfil

} '3' {
cls
'Has seleccionado la opción Ver-PerfilRedActua'

Ver-PerfilRedActual

} '4' {
cls
'Has seleccionado la opción #4'

Cambiar-PerfilRedActual


}'5' {
cls
'Has seleccionado la opción Ver-ReglasBloqueo'

Ver-ReglasBloqueo


}'6' {
cls
'Has seleccionado la opción Agregar-ReglasBloqueo'

Agregar-ReglasBloqueo


}'7' {
cls
'Has seleccionado la opción Eliminar-ReglasBloqueo'

Eliminar-ReglasBloqueo


}'q' {
return
}
}
pause
}
until ($input -eq 'q')