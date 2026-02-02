PROGRAM simpson
implicit none

INTEGER :: n, i, ios
REAL :: a, b, h, x, suma, integral
REAL :: dummy

! Abrir archivo de salida
open(unit=10, file="C:\\Users\\abbya\\OneDrive\\Desktop\\datos.dat", &
     status="replace", action="write", iostat=ios)

if (ios /= 0) then
    print *, "ERROR al abrir el archivo. IOSTAT =", ios
    stop
end if

! Leer datos
print *, "Ingrese limite inferior 'a':"
read *, a

print *, "Ingrese limite superior 'b':"
read *, b

print *, "Ingrese cantidad de subintervalos 'n' (par):"
read *, n

if (mod(n,2) /= 0) then
    print *, "n debe ser par"
    stop
end if

h = (b - a)/n
suma = f(a) + f(b)

! Escribir primer punto
write(10,*) a, f(a)

do i = 1, n-1
    x = a + i*h
    write(10,*) x, f(x)
    if (mod(i,2) == 0) then
        suma = suma + 2*f(x)
    else
        suma = suma + 4*f(x)
    end if
end do

! Escribir último punto
write(10,*) b, f(b)

integral = suma*h/3.0
print *, "Integral =", integral

close(10)

print *, "Datos escritos en datos.dat. Presione Enter para salir."
read *, dummy

contains

real function f(x)
real, intent(in) :: x
f = log( tan( 3.0*x**2 + 2.0 ) - cosh( 3.0*x**2 + 2.0 ) )
end function f

END PROGRAM simpson

