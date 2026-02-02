PROGRAM simpson3
implicit none

INTEGER :: n, i, ios
REAL :: a, b, h, x, suma, integral

! Archivo seguro en Escritorio de Windows moderno
open(unit=10, file="C:\\Users\\abbya\\OneDrive\\Desktop\\datos.dat", &
     status="replace", action="write", iostat=ios)

if (ios /= 0) then
    print *, "ERROR al abrir el archivo. IOSTAT =", ios
    stop
else
    print *, "Archivo abierto correctamente"
end if

print *, "Ingrese limite inferior a:"
read *, a

print *, "Ingrese limite superior b:"
read *, b

print *, "Ingrese cantidad de subintervalos n:"
read *, n

if (mod(n,3) /= 0) then
    print *, "n debe ser multiplo de 3"
    stop
end if

h = (b - a) / n
suma = f(a) + f(b)

write(10,*) a, f(a)

do i = 1, n-1
    x = a + i*h
    write(10,*) x, f(x)
    if (mod(i,3) == 0) then
        suma = suma + 2.0*f(x)
    else
        suma = suma + 3.0*f(x)
    end if
end do

write(10,*) b, f(b)

integral = suma * (3.0*h/8.0)
print *, "Integral =", integral

close(10)

contains
real function f(x)
    real, intent(in) :: x
    f = x * asinh(x**2 + 3)
end function f

END PROGRAM simpson3

