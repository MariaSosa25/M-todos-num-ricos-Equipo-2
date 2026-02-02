PROGRAM simpson
implicit none
INTEGER:: n, i
REAL:: a,b,h,x,suma,int

print *, "Ingrese l¡mite inferior 'a':"
read *, a

print *, "Ahora el l¡mite superior 'b':"
read *, b

print *, "Por £ltimo, la cantidad de subintervalos 'n':"
read *, n

if (mod(n,2) /=0) then
    print*, "n debe ser par"
    stop
end if

h= (b-a)/n
suma= f(a)+ f(b)

do i=1, n-1
    x= a +i*h
    if (mod(i,2)==0) then
        suma= suma +2*f(x)
    else
        suma=suma + 4*f(x)
    end if
end do

int= suma*h/3.0

print *, "Integral =", int

PAUSE

contains

real function f(x)
real, intent(in)::x

f = (1/(sqrt(5-7*x**2)))

end function


END PROGRAM



