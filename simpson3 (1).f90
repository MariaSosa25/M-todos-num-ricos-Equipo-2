PROGRAM simpson3
implicit none
INTEGER:: n, i
REAL:: a,b,h,x,suma,int

print *, "Ingrese l¡mite inferior 'a':"
read *, a

print *, "Ahora el l¡mite superior 'b':"
read *, b

print *, "Por £ltimo, la cantidad de subintervalos 'n':"
read *, n

if (mod(n,3) /=0) then
    print*, "n debe ser m£ltiplo de 3"
    stop
end if

h= (b-a)/n
suma= f(a)+ f(b)

do i=1, n-1
    x = a + i*h

    if (mod(i,3)==0) then
        suma = suma + 2*f(x)
    else
        suma = suma + 3*f(x)
    end if
end do

int= suma*(3.0*h/8.0)

print *, "Integral =", int

PAUSE

contains

real function f(x)
real, intent(in)::x

f = (1/(sqrt(5-7*x**2)))

end function


END PROGRAM
